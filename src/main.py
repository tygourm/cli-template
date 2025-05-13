from contextlib import suppress
from typing import Annotated

import typer

app = typer.Typer(add_completion=False)


@app.command()
def hello(name: Annotated[str, typer.Argument()] = "World") -> None:
    """Hello command."""
    typer.echo(f"Hello, {name}!")


@app.command()
def goodbye(name: Annotated[str, typer.Argument()] = "World") -> None:
    """Goodbye command."""
    typer.echo(f"Goodbye, {name}!")


if __name__ == "__main__":  # pragma: no cover
    with suppress(SystemExit):
        app(["--help"])

    while True:
        try:
            command: str = typer.prompt("Enter your command (Ctrl+C to exit)")
        except typer.Abort:
            typer.echo("\nExiting...")
            break
        with suppress(SystemExit):
            app(command.split())
