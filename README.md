# cli-template

Yet another template.

## Prerequisites

This project uses [uv](https://docs.astral.sh/uv) as a Python package and
project manager.

## Development

### Dependencies

Install Python dependencies.

```bash
uv sync --all-groups --frozen
```

Activate the virtual environment.

```bash
source .venv/bin/activate
```

### App

```bash
python main.py
```

### CLI

You can run the `cli-template` command, and install completion.

```bash
cli-template
```

```bash
cli-template --install-completion
source ~/.bashrc
```

Now, tab completion is available `cli-template [TAB][TAB] ✨`.

### Test

This project uses [pytest](https://pypi.org/project/pytest) for testing and
[pytest-cov](https://pypi.org/project/pytest-cov) for code coverage.

```bash
pytest -p no:cacheprovider
```

## Deployment

Build the image.

```bash
docker build -t cli-template .
```

Run the container.

```bash
docker run -it --rm cli-template
```

Inside of the container, you can run the `cli-template` command, and install
completion.

```bash
# Install completion
cli-template --install-completion
source ~/.bashrc
```

Now, tab completion is available `cli-template [TAB][TAB] ✨`.

## Miscellaneous

### Docs

This project uses
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material) as a
documentation framework.

```bash
# Serve docs
mkdocs serve
```

```bash
# Build docs
mkdocs build
```

### Lint / Format

This project uses [Ruff](https://docs.astral.sh/ruff) as a Python linter and
code formatter.

```bash
ruff check --no-cache # Lint
ruff format --no-cache # Format
```
