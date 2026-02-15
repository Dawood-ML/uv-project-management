#!/bin/bash
# Simple quality checks before committing

echo "Formatting code..."
uv run black src/ tests/

echo "Running tests..."
uv run pytest

echo "✅ Quality checks complete!"
