from typing import Annotated

import typer

from src.cli_template.logger import logger
from src.cli_template.settings import settings

app = typer.Typer(help=f"cli-template {settings.version}")


@app.command()
def hello(name: Annotated[str, typer.Argument()] = "World") -> None:
    """Hello command."""
    logger.debug("hello(name=%s)", name)
    typer.echo(f"Hello, {name}!")


@app.command()
def goodbye(name: Annotated[str, typer.Argument()] = "World") -> None:
    """Goodbye command."""
    logger.debug("goodbye(name=%s)", name)
    typer.echo(f"Goodbye, {name}!")


if __name__ == "__main__":  # pragma: no cover
    app()
