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
    app()
