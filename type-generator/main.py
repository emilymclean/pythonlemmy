import os
import sys
from typing import Optional, Tuple

from tree_sitter import Parser, Language
import tree_sitter_typescript as ts_typescript
from src import ModelVisitor, EnumVisitor, HttpVisitor

parser = Parser()
parser.set_language(Language(ts_typescript.language_typescript(), "TypeScript"))
model_dir = "../src/main/java/cl/emilym/jlemmy/model/"
retrofit_dir = "../src/main/java/cl/emilym/jlemmy/"


def generate_types():
    files = os.listdir(f"{current_dir()}lemmy-js-client/src/types/")
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    for file in files:
        if file.endswith("Id.ts"):
            continue
        with open(f"{current_dir()}lemmy-js-client/src/types/{file}", "r") as f:
            result = parse_model(f.read())
            if result is None:
                continue
            with open(f"{model_dir}/{result[0]}.java", "w") as f:
                f.write(result[1])


def parse_model(model_contents: str) -> Optional[Tuple[str, str]]:
    tree = parser.parse(bytes(model_contents, "utf-8"))
    if "export type" in model_contents:
        visitor = EnumVisitor(tree)
        result = visitor.build()
        return visitor.enum_name, result
    if "export interface" in model_contents:
        visitor = ModelVisitor(tree)
        result = visitor.build()
        return visitor.class_name, result
    return None


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
    generate_retrofit()
    generate_types()
