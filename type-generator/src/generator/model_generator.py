import textwrap
from datetime import datetime, timezone
from typing import List

from ..models import Property


class ModelGenerator:
    _indent_char = "\t"
    _header = f"""
// This class was generated, do not modify it directly
package cl.emilym.jlemmy.model;

import com.google.gson.annotations.SerializedName;
        """

    _class_name: str
    _properties: List[Property] = []

    def __init__(self, class_name: str, properties: List[Property]):
        self._class_name = class_name
        self._properties = properties

    def build(self) -> str:
        return f"""
{self._header}
public class {self._class_name} {{
{textwrap.indent(self._generate_property_list(), self._indent_char)}

{textwrap.indent(self._generate_constructor(), self._indent_char)}

{textwrap.indent(self._generate_get_and_sets(), self._indent_char)}
}}
            """.strip()

    def _generate_property_list(self) -> str:
        lines = []
        for prop in self._properties:
            serialized_line = f"@SerializedName(\"{prop.api_name}\")" if prop.java_name != prop.api_name else ""
            lines.append(f"""
{serialized_line}
private {prop.type} {prop.java_name};
                """.strip())

        return "\n".join(lines)

    def _generate_constructor(self) -> str:
        return f"""
public {self._class_name}({", ".join([f"{prop.type} {prop.java_name}" for prop in self._properties])}) {{
{textwrap.indent(self._generate_constructor_assignments(), self._indent_char)}
}}
            """.strip()

    def _generate_constructor_assignments(self) -> str:
        return "\n".join([f"this.{prop.java_name} = {prop.java_name};" for prop in self._properties])

    def _generate_get_and_sets(self) -> str:
        return "\n\n".join([f"""
public {prop.type} get{prop.cap_java_name}() {{
    return {prop.java_name};
}}

public void set{prop.cap_java_name}({prop.type} {prop.java_name}) {{
    this.{prop.java_name} = {prop.java_name};
}}
            """.strip() for prop in self._properties])