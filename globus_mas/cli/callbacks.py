import typing as t

import typer

from globus_mas import __version__


def version_callback(display_version: bool):
    if display_version:
        typer.echo(f"globus-mas {__version__}")
        raise typer.Exit()


def uniqueify(values: t.List[str]):
    """
    Given a list of values, removes any duplicates.
    """
    return list(set(values))


def scope_suffix_validator(value: str):
    if value != value.lower():
        raise typer.BadParameter("Value must contain only lowercase letters.")

    copy = value.replace("_", "")
    if not copy.isalnum():
        raise typer.BadParameter("Value must contain only letters, numbers, or '_'.")
    return value
