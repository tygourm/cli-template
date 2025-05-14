[![CI](https://github.com/tygourm/cli-template/actions/workflows/ci.yml/badge.svg)](https://github.com/tygourm/cli-template/actions/workflows/ci.yml)

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

### CLI

```bash
# Run CLI
uv run src/main.py

# Help
--help

# Hello command
hello # Hello, World!
hello tygourm # Hello, tygourm!

# Goodbye command
goodbye # Goodbye, World!
goodbye tygourm # Goodbye, tygourm!
```

### Docker

```bash
# Build image
docker build -t cli-template .

# Run container
docker run -it cli-template

# Inspect container
docker run -it cli-template /bin/bash
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
