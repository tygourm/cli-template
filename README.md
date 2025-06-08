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

### Docker

```bash
# Build image
docker build -t cli-template .
```

```bash
# Run container
docker run -it --rm cli-template
```

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
