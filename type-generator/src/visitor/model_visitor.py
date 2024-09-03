import textwrap
from typing import List

from tree_sitter import Node, Tree
from ..models import Property
from ..util import to_lower_camel_case, to_camel_case, normalize_type
from ..generator.model_generator import ModelGenerator
from .visitor import Visitor


class ModelVisitor(Visitor):
    _encoding = "utf-8"
    _number_type = "long"

    class_name = ""
    _properties: List[Property] = []

    def __init__(self, tree: Tree):
        self.tree = tree
        self.class_name = ""
        self._properties = []

    def _generate(self) -> str:
        return ModelGenerator(self.class_name, self._properties).build()

    def visit_interface_declaration(self, node: Node):
        self.class_name = node.child_by_field_name("name").text.decode(self._encoding)
        self._accept_list(node.children)

    def visit_property_signature(self, node: Node):
        name = node.child_by_field_name("name").text.decode(self._encoding)

        self._properties.append(Property(
            name,
            to_lower_camel_case(name),
            to_camel_case(name),
            "Object"
        ))
        self._accept_list(node.children)

    def visit_type_annotation(self, node: Node):
        type_identifier = node.child(1).text.decode(self._encoding)
        if "<" in type_identifier:
            return self._accept(node.child(1))

        last_idx = len(self._properties) - 1

        self._properties[last_idx].type = normalize_type(type_identifier)

    def visit_generic_type(self, node: Node):
        last_idx = len(self._properties) - 1
        type_identifier = node.child(0).text.decode(self._encoding)
        type_parameter = normalize_type(node.child(1).child(1).text.decode(self._encoding))

        if type_identifier == "Array":
            out_type = f"{type_parameter}[]"
        else:
            raise f"Unhandled Type {type_identifier}!"

        self._properties[last_idx].type = out_type
