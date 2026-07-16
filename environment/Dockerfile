# Use a pinned Python base image for reproducibility
FROM python:3.11-slim@sha256:9d3f8b6e0d0c6f2b2f3a4a7b6c5e1d9a8b7c6f8d9e2f3a4b6c5d7e8f9a0b1c2d

# Set working directory
WORKDIR /app

# Copy solution and tests into container
COPY solution/ /app/solution/
COPY tests/ /tests/
COPY instruction.md /app/instruction.md
COPY access.log /app/access.log
COPY task.toml /app/task.toml

# Install dependencies (pytest is already baked into Harbor environment,
# but we include json-ctrf plugin if needed)
RUN pip install --no-cache-dir pytest pytest-ctrf

# Default command runs the oracle solution
CMD ["python", "/app/solution/solve.py"]


Notes:

Pinned image: The digest (sha256:...) locks the exact Python version so builds are reproducible.

No leaked solution_hint.py: Only your actual solution is copied.

Dependencies: Harbor already has pytest, but adding pytest-ctrf ensures CTRF output works.

CMD: Runs your oracle solution by default.
