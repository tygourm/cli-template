ARG BASE_IMAGE=python:3.13-slim-bookworm
ARG GROUP=cli-group
ARG USER=cli-user


### Install stage ###
FROM $BASE_IMAGE AS installer

RUN pip install uv
WORKDIR /app

COPY uv.lock .
COPY pyproject.toml .
RUN uv pip compile pyproject.toml -o requirements.txt
RUN pip wheel --wheel-dir /wheels -r requirements.txt


### Build stage ###
FROM $BASE_IMAGE AS builder

RUN pip install build
WORKDIR /app

COPY . .
RUN python -m build --wheel -o /wheels


### Run stage ###
FROM $BASE_IMAGE
ARG GROUP
ARG USER

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN groupadd $GROUP && useradd -g $GROUP -m -u 1000 $USER
WORKDIR /home/$USER/app

COPY --from=installer /wheels /wheels
RUN pip install /wheels/*.whl --no-cache-dir --no-deps && rm -rf /wheels
COPY --from=builder /wheels /wheels
RUN pip install /wheels/*.whl --no-cache-dir --no-deps && rm -rf /wheels

RUN chown -R $USER:$GROUP /home/$USER
USER $USER
CMD ["/bin/bash"]
