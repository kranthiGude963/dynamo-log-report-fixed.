#!/bin/bash
set -e

# Run pytest with CTRF output
pytest --ctrf -q tests/test_outputs.py > result.log || true

# Copy CTRF JSON to /app
if [ -f ctrf.json ]; then
  cp ctrf.json /app/ctrf.json
fi

# Determine reward: 1 if all tests passed, else 0
if grep -q "failed=0" result.log; then
  echo "1" > /app/reward.txt
else
  echo "0" > /app/reward.txt
fi
