import textwrap
from datetime import datetime, timezone
from typing import List

from ..models import EnumProperty


class EnumGenerator:
    _indent_char = "\t"

    _enum_name: str
    _types: List[EnumProperty] = []

    def __init__(self, enum_name: str, types: List[EnumProperty]):
        self._enum_name = enum_name
        self._types = types

    def build(self) -> str:
        return f"""
public enum {self._enum_name} {{
{textwrap.indent(self._generate_enum_list(), self._indent_char)}
}}
            """.strip()

    def _generate_enum_list(self) -> str:
        lines = []
        for prop in self._types:
            lines.append(f"""
{prop.api_name}
                """.strip())

        return ",\n".join(lines)