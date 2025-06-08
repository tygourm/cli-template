# cli-template

Yet another template.

!!! note "Design principles"

    - **DRY** Don't Repeat Yourself
    - **KISS** Keep It Simple, Stupid
    - **YAGNI** You Ain't Gonna Need It
    - **SOLID** Single responsibility, Open/closed, Liskov
    substitution, Interface segregation, Dependency inversion

## Prerequisites

This project uses [uv](https://docs.astral.sh/uv) as a Python
package and project manager.

## Setup

```bash
uv sync --all-groups --frozen
```

This command will create a virtual environment and install the
project dependencies. You need to activate the virtual
environment before continuing.

```bash
source .venv/bin/activate
```

!!! tip "Python & VS Code"

    - If dependencies are not recognized in VS Code, you can run
    the command `Ctrl+Shift+P > Python: Select Interpreter` and
    select `.venv/bin/python`.
    - After updating the dependencies, you can run the command
    `Ctrl+Shift+P > Developer: Reload Window` to refresh the
    development environment.

## Usage

### App

```bash
# Run app
uv run main.py # Fail
uv run main.py --help
```

### CLI

```bash
# Run CLI
cli-template # Fail
cli-template --help
```

```bash
# Install completion
cli-template --install-completion
source ~/.bashrc
```

```bash
# Use completion
cli [TAB] # ✨ cli-template
cli-template [TAB][TAB] # ✨ goodbye  hello
```

### Test

This project uses [pytest](https://pypi.org/project/pytest) for
testing and [pytest-cov](https://pypi.org/project/pytest-cov) for
code coverage.

```bash
pytest -p no:cacheprovider
```

!!! info

    The `-p no:cacheprovider` option prevents pytest from using
    the cache, which make the results more reliable. This is
    recommended for development but not mandatory, the CI will
    use it anyway.

### Docker

```bash
# Build image
docker build -t cli-template .
```

```bash
# Run container
docker run -it --rm cli-template
```

!!! info

    The `--rm` automatically removes the container and its
    associated anonymous volumes when it exits.

You can install and use completion inside the running container.

```bash
# Install completion
cli-template --install-completion
source ~/.bashrc
```

```bash
# Use completion
cli [TAB] # ✨ cli-template
cli-template [TAB][TAB] # ✨ goodbye  hello
```

## Miscellaneous

### Docs

This project uses
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material)
as a documentation framework.

```bash
# Serve docs
mkdocs serve
```

```bash
# Build docs
mkdocs build
```

### Lint / Format

This project uses [Ruff](https://docs.astral.sh/ruff) as a Python
linter and code formatter.

```bash
ruff check --no-cache # Lint
ruff format --no-cache # Format
```

!!! info

    - The `--no-cache` option prevents Ruff from using the cache,
    which make the results more reliable. This is recommended for
    development but not mandatory, the CI will use it anyway.
    - The `Ruff` version of the project must match the version
    shipped in the `charliermarsh.ruff` VS Code extension.
