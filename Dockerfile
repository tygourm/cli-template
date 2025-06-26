ARG BASE_IMAGE=python:3.13-slim-bookworm
ARG USER=cli-template
ARG GROUP=cli-template


### Install stage ###
FROM $BASE_IMAGE AS installer

RUN pip install uv
WORKDIR /app

COPY uv.lock .
COPY pyproject.toml .

RUN uv export -o requirements.txt --no-emit-package cli-template && \
    pip wheel -r requirements.txt -w /wheels --no-cache-dir --no-deps


### Build stage ###
FROM $BASE_IMAGE AS builder

RUN pip install build hatchling
WORKDIR /app

COPY . .

RUN python -m build -w -nx -o /wheels


### Run stage ###
FROM $BASE_IMAGE
ARG GROUP
ARG USER

RUN groupadd $GROUP && \
    useradd -m -g $GROUP -u 1000 $USER
WORKDIR /home/$USER/app

COPY --from=installer /wheels /wheels
RUN pip install /wheels/* --no-cache-dir --no-deps && \
    rm -rf /wheels

COPY --from=builder /wheels /wheels
RUN pip install /wheels/* --no-cache-dir --no-deps && \
    rm -rf /wheels

RUN chown -R $USER:$GROUP /home/$USER
USER $USER
CMD ["bash"]
