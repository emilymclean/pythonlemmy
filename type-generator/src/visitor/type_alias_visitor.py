import textwrap
from typing import List

from tree_sitter import Node, Tree
from .visitor import Visitor
from ..models import EnumProperty
from ..util import to_enum_case


class TypeAliasVisitor(Visitor):
    _encoding = "utf-8"
    _number_type = "long"

    is_type_alias: bool
    type_alias_name = ""
    mapped_type = ""

    def __init__(self, tree: Tree):
        self.tree = tree
        self.is_type_alias = False
        self.type_alias_name = ""
        self.mapped_type = ""

    def visit_type_alias_declaration(self, node: Node):
        self.type_alias_name = node.child_by_field_name("name").text.decode(self._encoding)
        if node.child_by_field_name("value").type == "predefined_type":
            self.is_type_alias = True
            self._accept_list(node.children)

    def visit_predefined_type(self, node: Node):
        self.mapped_type = node.text.decode(self._encoding)
