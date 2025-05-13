FROM python:3.13-slim-bookworm

# Setup
WORKDIR /app
RUN pip install uv

# Install dependencies
COPY uv.lock .
COPY pyproject.toml .
RUN uv sync --locked --compile-bytecode

# Copy sources
COPY . .

# Run CLI
CMD [ "uv", "run", "src/main.py" ]
