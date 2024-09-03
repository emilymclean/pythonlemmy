import textwrap
from datetime import datetime, timezone
from typing import List

from ..models import EnumProperty


class EnumGenerator:
    _indent_char = "\t"
    _header = f"""
// This class was generated, do not modify it directly
package cl.emilym.jlemmy.model;

import com.google.gson.annotations.SerializedName;
        """

    _enum_name: str
    _types: List[EnumProperty] = []

    def __init__(self, enum_name: str, types: List[EnumProperty]):
        self._enum_name = enum_name
        self._types = types

    def build(self) -> str:
        return f"""
{self._header}
public enum {self._enum_name} {{
{textwrap.indent(self._generate_enum_list(), self._indent_char)}
}}
            """.strip()

    def _generate_enum_list(self) -> str:
        lines = []
        for prop in self._types:
            serialized_line = f"@SerializedName(\"{prop.api_name}\")" if prop.java_name != prop.api_name else ""
            lines.append(f"""
{serialized_line}
{prop.java_name}
                """.strip())

        return ",\n".join(lines)