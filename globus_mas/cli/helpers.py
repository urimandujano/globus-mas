import typing as t

import typer
import yaml
from globus_sdk import GlobusAPIError, GlobusHTTPResponse
from pygments import formatters, highlight, lexers

verbosity_option = typer.Option(
    False, "--verbose", "-v", help="Run with increased verbosity", show_default=False
)


def format_and_print(
    obj: t.Union[GlobusHTTPResponse, GlobusAPIError, dict], *, verbose=False
):
    if isinstance(obj, (GlobusHTTPResponse, GlobusAPIError)) and verbose:
        typer.secho(get_http_details(obj), fg=typer.colors.BRIGHT_CYAN, err=True)

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


def get_http_details(result: t.Union[GlobusHTTPResponse, GlobusAPIError]) -> str:
    if isinstance(result, GlobusHTTPResponse):
        base_request = result._data.request
        reponse_status_code = result._data.status_code
    if isinstance(result, GlobusAPIError):
        base_request = result._underlying_response.request
        reponse_status_code = result._underlying_response.status_code

    formatted_headers = "\n".join(
        f"  {k}: {v}" for k, v in base_request.headers.items()
    )
    http_details = f"Request: {base_request.method} {base_request.url}\n"
    http_details += f"Headers:\n{formatted_headers}\n"
    http_details += f"Response: {reponse_status_code}"
    return http_details
