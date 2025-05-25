# cli-template

Yet another template.

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

!!! note

    - If dependencies are not recognized in VS Code, you can run
    the command `Ctrl + Shift + P > Python: Select Interpreter`
    and select `.venv/bin/python`.
    - After updating the dependencies, you can run the command
    `Ctrl + Shift + P > Developer: Reload Window` to refresh the
    development environment.

## Usage

### Lint / Format

This project uses [Ruff](https://docs.astral.sh/ruff) as a Python
linter and code formatter.

```bash
ruff check --no-cache # Lint
ruff format --no-cache # Format
```

!!! note

    The `--no-cache` option prevents Ruff from using the cache,
    which make the results more reliable. This is recommended for
    developement but not mandatory, the CI will use it anyway.

### Test

This project uses [pytest](https://pypi.org/project/pytest) for
testing and [pytest-cov](https://pypi.org/project/pytest-cov) for
code coverage.

```bash
pytest -p no:cacheprovider
```

!!! note

    The `-p no:cacheprovider` option prevents pytest from using
    the cache, which make the results more reliable. This is
    recommended for developement but not mandatory, the CI will
    use it anyway.

### App

```bash
# Run app
uv run main.py # Fail
uv run main.py --help
```

```bash
# Hello command
uv run main.py hello # Hello, World!
uv run main.py hello tygourm # Hello, tygourm!
```

```bash
# Goodbye command
uv run main.py goodbye # Goodbye, World!
uv run main.py goodbye tygourm # Goodbye, tygourm!
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

### Docker

```bash
# Build image
docker build -t cli-template .
```

```bash
# Run container
docker run -it --rm cli-template
```

!!! note

    The `--rm` automatically remove the container and its
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

### Docs

```bash
# Serve docs
mkdocs serve
```

```bash
# Build docs
mkdocs build
```
