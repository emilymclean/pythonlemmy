import os
import sys
from typing import Optional, Tuple

from tree_sitter import Parser, Language
import tree_sitter_typescript as ts_typescript
from src import ModelVisitor, EnumVisitor, HttpVisitor, ClassType

parser = Parser()
parser.set_language(Language(ts_typescript.language_typescript(), "TypeScript"))
model_dir = "./test_output"
retrofit_dir = "../src/main/java/cl/emilym/jlemmy/"

view_header = """
from typing import Optional

from .objects import *
from .utils import call_with_filtered_kwargs


class ViewObject(object):
    \"\"\" ViewObject: parent object to all view-related objects \"\"\"

    def __init__(self, view: dict) -> None:
        self._view = view
        self.parse()
""".strip()

object_header = """
from typing import Optional
from dataclasses import dataclass
""".strip()

responses_header = """
from typing import Optional
import requests

from .views import *
from .objects import *
""".strip()

enum_names = []

objects = []
responses = []
views = []


def generate_types():
    files = os.listdir(f"{current_dir()}lemmy-js-client/src/types/")
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    for file in files:
        if file.endswith("Id.ts"):
            continue
        with open(f"{current_dir()}lemmy-js-client/src/types/{file}", "r") as f:
            parse_enum(f.read())

    for file in files:
        if file.endswith("Id.ts"):
            continue
        with open(f"{current_dir()}lemmy-js-client/src/types/{file}", "r") as f:
            parse_model(f.read())

    with open(f"{model_dir}/views.py", "w") as f:
        f.write(view_header)
        f.write("\n\n\n")
        f.write("\n\n\n".join(views))
        f.write("\n")
    with open(f"{model_dir}/objects.py", "w") as f:
        f.write(object_header)
        f.write("\n\n\n")
        f.write("\n\n\n".join(objects))
        f.write("\n")
    with open(f"{model_dir}/responses.py", "w") as f:
        f.write(responses_header)
        f.write("\n\n\n")
        f.write("\n\n\n".join(responses))
        f.write("\n")


def parse_enum(model_contents: str):
    tree = parser.parse(bytes(model_contents, "utf-8"))

    if "export type" not in model_contents:
        return

    visitor = EnumVisitor(tree)
    result = visitor.build()

    enum_names.append(visitor.enum_name)

def parse_model(model_contents: str):
    tree = parser.parse(bytes(model_contents, "utf-8"))

    if "export interface" not in model_contents:
        return
    visitor = ModelVisitor(tree, enum_names)
    result = visitor.build()
    if visitor.class_type == ClassType.VIEW:
        views.append(result)
    elif visitor.class_type == ClassType.RESPONSE:
        responses.append(result)
    elif visitor.class_type == ClassType.OBJECT:
        objects.append(result)


def generate_retrofit():
    if not os.path.exists(retrofit_dir):
        os.makedirs(retrofit_dir)
    with open(f"{current_dir()}{retrofit_dir}/LemmyApi.java", "w") as f:
        f.write(parse_retrofit())


def parse_retrofit() -> str:
    with open(f"{current_dir()}lemmy-js-client/src/http.ts", "r") as f:
        tree = parser.parse(bytes(f.read(), "utf-8"))
        visitor = HttpVisitor(tree)
        return visitor.build()


def current_dir():
    return sys.argv[0][:-len("main.py")]


if __name__ == '__main__':
    print(current_dir())
    # generate_retrofit()
    generate_types()
