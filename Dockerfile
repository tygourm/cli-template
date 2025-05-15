FROM python:3.13-slim-bookworm

# Setup
WORKDIR /app
RUN pip install uv
ENV UV_SYSTEM_PYTHON=1

# Install dependencies
COPY uv.lock .
COPY pyproject.toml .
RUN uv sync --locked --compile-bytecode

# Copy sources
COPY . .

# Build
RUN uv pip install .
