from typer.testing import CliRunner

from main import app


def test_app_requires_command(cli_runner: CliRunner) -> None:
    """Test that the app requires a command."""
    result = cli_runner.invoke(app)
    assert result.exit_code == 2
    assert "Missing command." in result.stderr


def test_app_has_help_option(cli_runner: CliRunner) -> None:
    """Test that the app has a help option."""
    result = cli_runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "cli-template 1.0.0" in result.stdout


def test_hello_command(cli_runner: CliRunner) -> None:
    """Test the hello command."""
    result = cli_runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.stdout

    result = cli_runner.invoke(app, ["hello", "tygourm"])
    assert result.exit_code == 0
    assert "Hello, tygourm!" in result.stdout


def test_goodbye_command(cli_runner: CliRunner) -> None:
    """Test the goodbye command."""
    result = cli_runner.invoke(app, ["goodbye"])
    assert result.exit_code == 0
    assert "Goodbye, World!" in result.stdout

    result = cli_runner.invoke(app, ["goodbye", "tygourm"])
    assert result.exit_code == 0
    assert "Goodbye, tygourm!" in result.stdout
