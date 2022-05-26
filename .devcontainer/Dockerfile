ARG VARIANT=3.8-bullseye
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Send python logs to stdout/err
ENV PYTHONUNBUFFERED 1

# TODO: if you need node, add it version and install script here.

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install git