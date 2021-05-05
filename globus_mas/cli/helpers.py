import typing as t

import typer
import yaml
from globus_sdk import GlobusAPIError, GlobusHTTPResponse
from pygments import formatters, highlight, lexers


def format_and_print(obj: t.Union[GlobusHTTPResponse, GlobusAPIError, dict]):
    if isinstance(obj, GlobusHTTPResponse):
        result = obj.data
    elif isinstance(obj, GlobusAPIError):
        result = obj.raw_json if obj.raw_json else obj.raw_text
    else:
        result = obj

    results = yaml.dump(result, allow_unicode=True, sort_keys=False)
    colorful_results = highlight(
        results,
        lexers.YamlLexer(ensurenl=False),
        formatters.TerminalFormatter(),
    )
    typer.echo(colorful_results)
