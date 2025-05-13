import pytest
from typer.testing import CliRunner


@pytest.fixture
def cli_runner() -> CliRunner:
    """Fixture for the CLI runner."""
    return CliRunner()
