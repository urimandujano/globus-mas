import typer

from globus_mas.cli import clients, groups, scopes, tokens
from globus_mas.cli.callbacks import version_callback

app = typer.Typer(
    help="A Globus-oriented CLI to facilitate everyday tasks",
    short_help="Globus Productivity CLI",
)
app.add_typer(groups.app, name="groups")
app.add_typer(scopes.app, name="scopes")
app.add_typer(clients.app, name="clients")
app.add_typer(tokens.app, name="tokens")


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-V",
        callback=version_callback,
        help="Print CLI version number and exit",
        is_eager=True,
    ),
):
    pass


if __name__ == "__main__":
    app()
