# Based on https://stackoverflow.com/a/64642121
FROM python:3.11.5-slim-bookworm as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock README.md ./
COPY generated ./generated
COPY src ./src
RUN poetry config virtualenvs.in-project true && \
    poetry install --only=main --no-root && \
    poetry build

FROM base as final

COPY --from=builder /app/.venv ./.venv
COPY --from=builder /app/generated ./generated
COPY --from=builder /app/dist .

RUN ./.venv/bin/pip install *.whl

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD [ "bash", "-c", "echo \"immich-scripts works!\"; echo \"Please specify a command\""]