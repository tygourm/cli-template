# cli-template

Yet another template.

## Prerequisites

This project uses [uv](https://docs.astral.sh/uv) as a package
and project manager.

## Setup

```bash
uv sync --frozen --all-groups
```

This command will create a virtual environment and install the
project dependencies. You need to activate the virtual
environment before continuing.

```bash
source .venv/bin/activate
```

## Usage

### Lint / Format

This project uses [Ruff](https://docs.astral.sh/ruff) as a linter
and code formatter.

```bash
ruff check --no-cache # Lint
ruff format --no-cache # Format
```

### Test

This project uses [pytest](https://pypi.org/project/pytest) for
testing and [pytest-cov](https://pypi.org/project/pytest-cov) for
code coverage.

```bash
pytest
```

### App

```bash
# Run app
uv run src/main.py # Fail
uv run src/main.py --help

# Hello command
uv run src/main.py hello # Hello, World!
uv run src/main.py hello tygourm # Hello, tygourm!

# Goodbye command
uv run src/main.py goodbye # Goodbye, World!
uv run src/main.py goodbye tygourm # Goodbye, tygourm!
```

### CLI

```bash
# Run CLI
cli-template # Fail
cli-template --help

# Install completion
cli-template --install-completion
source ~/.bashrc
cli-template [TAB][TAB]
```

### Docker

```bash
# Build image
docker build -t cli-template .

# Run container
docker run -it --rm cli-template /bin/bash

# Install completion
cli-template --install-completion
source ~/.bashrc
cli-template [TAB][TAB]
```

### Docs

```bash
# Create docs
mkdocs new .

# Serve docs
mkdocs serve

# Build docs
mkdocs build
```
