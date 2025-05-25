ARG BASE_IMAGE=python:3.13-slim-bookworm
ARG GROUP=cli-group
ARG USER=cli-user


### Build stage ###
FROM $BASE_IMAGE AS builder

# Setup
RUN pip install uv
WORKDIR /app

# Requirements
COPY uv.lock .
COPY pyproject.toml .
RUN uv pip compile pyproject.toml -o requirements.txt

# Dependencies
RUN pip install build && pip wheel --wheel-dir /wheels -r requirements.txt

# Build
COPY . .
RUN python -m build --wheel -o /wheels


### Run stage ###
FROM $BASE_IMAGE
ARG GROUP
ARG USER

# Setup
ENV PIP_NO_CACHE_DIR=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN groupadd $GROUP && useradd -g $GROUP -m -u 1000 $USER
WORKDIR /home/$USER

# Dependencies
COPY --from=builder /wheels /wheels
RUN pip install /wheels/*.whl && rm -rf /wheels

# Run
USER $USER
CMD ["/bin/bash"]
