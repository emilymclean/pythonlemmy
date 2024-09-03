import textwrap
from typing import List

from ..models import Property, ApiMethod, HttpMethod


class RetrofitGenerator:
    _domain_match = [HttpMethod.GET, HttpMethod.POST, HttpMethod.PUT, HttpMethod.DELETE]
    _retrofit_match = ["GET", "POST", "PUT", "DELETE"]
    _indent_char = "\t"
    _header = f"""
// This class was generated, do not modify it directly
package cl.emilym.jlemmy;

import cl.emilym.jlemmy.model.*;
import retrofit2.*;
import retrofit2.http.*;
import java.util.List;
        """

    _methods: List[ApiMethod] = []

    def __init__(self, methods: List[ApiMethod]):
        self._methods = methods

    def build(self) -> str:
        return f"""
{self._header}
public interface LemmyApi {{
{textwrap.indent(self._generate_methods(), self._indent_char)}
}}
            """.strip()

    def _generate_methods(self) -> str:
        lines = []
        for method in self._methods:
            http_method = self._retrofit_match[self._domain_match.index(method.method)]
            input_type = f"{method.input} request" if method.input != "object" else ""
            line = f"""
@{http_method}("{method.url}")
Call<{method.output}> {method.name}({input_type});
            """.strip()
            lines.append(line)

        return "\n\n".join(lines)
