.PHONY: install test lint format-check typecheck audit ci

install:
    pip install -e ".[dev]"

test:
    pytest

lint:
    ruff check src tests

format-check:
    ruff format --check src tests

typecheck:
    mypy src/clecmas

audit:
    pip-audit

ci: lint format-check typecheck test audit
