import os
import sys
from typing import Optional, Tuple

import requests
import yaml
from openapi_parser.parser import OpenApiParser
from tree_sitter import Parser, Language
import tree_sitter_typescript as ts_typescript
from src import ModelVisitor, EnumVisitor, HttpVisitor, ClassType, ModelGenerator, HttpGenerator, Property, \
    TypeAliasVisitor

parser = Parser()
parser.set_language(Language(ts_typescript.language_typescript(), "TypeScript"))
model_dir = "../pythonlemmy"
# model_dir = "./test_output"

enum_names = []
type_aliases = {}

objects = {}
object_dependencies = {}
responses = {}
response_dependencies = {}
views = {}
view_dependencies = {}

openapi_docs = "https://raw.githubusercontent.com/MV-GH/lemmy_openapi_spec/master/lemmy_spec.yaml"


# From https://code.activestate.com/recipes/576570-dependency-resolver/
def dep(arg):
    '''
        Dependency resolver

    "arg" is a dependency dictionary in which
    the values are the dependencies of their respective keys.
    '''
    d=dict((k, set(arg[k])) for k in arg)
    r=[]
    while d:
        # values not in keys (items without dep)
        t=set(i for v in d.values() for i in v)-set(d.keys())
        # and keys without value (items without dep)
        t.update(k for k, v in d.items() if not v)
        # can be done right away
        r.append(t)
        # and cleaned up
        d=dict(((k, v-t) for k, v in d.items() if v))
    return r


def list_enums():
    types_dir = f"{current_dir()}lemmy-js-client/src/types/"
    files = os.listdir(types_dir)

    for file in files:
        with open(f"{types_dir}{file}", "r") as f:
            content = f.read()
        parse_enum(content)
        parse_type_alias(content)


def generate_types():
    types_dir = f"{current_dir()}lemmy-js-client/src/types/"

    files = os.listdir(types_dir)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    for file in files:
        file_without_extension = file[:-len(".ts")]
        if file_without_extension in enum_names or file_without_extension in type_aliases.keys():
            continue
        with open(f"{types_dir}{file}", "r") as f:
            parse_model(f.read())

    print(f"Object count = {len(objects)}, Response count = {len(responses)}, View count = {len(views)}")
    generate_file(f"./headers/object_header.py", "objects.py", objects, object_dependencies)
    generate_file(f"./headers/response_header.py", "responses.py", responses, response_dependencies)
    generate_file(f"./headers/view_header.py", "views.py", views, view_dependencies)


def generate_file(header_file_path: str, output_file_path: str, types: dict[str, str], dependencies: dict[str, str]):
    with open(header_file_path, "r") as f:
        header = f.read()

    dep_tree = dep(dependencies)

    with open(f"{model_dir}/{output_file_path}", "w") as f:
        f.write(header)
        for d in dep_tree:
            for r in d:
                if r not in types:
                    continue
                f.write(f"\n\n\n{types[r]}")
        f.write("\n")


def parse_enum(model_contents: str):
    tree = parser.parse(bytes(model_contents, "utf-8"))

    if "export type" not in model_contents:
        return

    visitor = EnumVisitor(tree)
    visitor.walk()

    if not visitor.is_enum:
        return

    enum_names.append(visitor.enum_name)


def parse_type_alias(model_contents: str):
    tree = parser.parse(bytes(model_contents, "utf-8"))

    if "export type" not in model_contents:
        return

    visitor = TypeAliasVisitor(tree)
    visitor.walk()

    if not visitor.is_type_alias:
        return

    type_aliases[visitor.type_alias_name] = visitor.mapped_type


def parse_model(model_contents: str):
    tree = parser.parse(bytes(model_contents, "utf-8"))

    if "export type" not in model_contents:
        return

    visitor = ModelVisitor(tree, enum_names, type_aliases)
    visitor.walk()
    result = ModelGenerator(visitor.class_name, visitor.properties, visitor.class_type).build()
    if visitor.class_type == ClassType.VIEW:
        views[visitor.class_name] = result
        view_dependencies[visitor.class_name] = visitor.dependencies
    elif visitor.class_type == ClassType.RESPONSE:
        responses[visitor.class_name] = result
        response_dependencies[visitor.class_name] = visitor.dependencies
    elif visitor.class_type == ClassType.OBJECT:
        objects[visitor.class_name] = result
        object_dependencies[visitor.class_name] = visitor.dependencies


def generate_http():
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    with open(f"./headers/lemmyhttp_header.py", "r") as f:
        http_header = f.read()

    with open(f"{model_dir}/lemmyhttp.py", "w") as f:
        f.write(http_header)
        f.write(parse_http())
        f.write("\n")


def parse_http() -> str:
    types_dir = f"{current_dir()}lemmy-js-client/src/types/"
    docs = get_docs()

    with open(f"{current_dir()}lemmy-js-client/src/http.ts", "r") as f:
        tree = parser.parse(bytes(f.read(), "utf-8"))
        visitor = HttpVisitor(tree)
        visitor.walk()
        result = HttpGenerator(visitor.methods, types_dir, enum_names, type_aliases, docs).build()
        return result


def current_dir():
    return sys.argv[0][:-len("main.py")]


def get_docs() -> Optional[OpenApiParser]:
    if openapi_docs is None:
        return None

    content = requests.get(openapi_docs).text

    openapi_parser = OpenApiParser(yaml.safe_load(content))
    openapi_parser.load_all()

    return openapi_parser


if __name__ == '__main__':
    print(current_dir())
    list_enums()
    generate_http()
    generate_types()
