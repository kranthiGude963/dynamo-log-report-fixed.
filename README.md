# dynamo-log-report-fixed.
Corrected Terminal-Bench 2 task: log-report with proper format, environment, verifier, and instructions.


# Dynamo Log-Report Fixed Task

This repository contains the corrected Harbor Terminal-Bench 2 task for the Dynamo assessment.

## Contents
- task.toml (fixed format and metadata)

- environment/Dockerfile (pinned base image, no leaked solution)
- instruction.md (clear, numbered success criteria)
- tests/test_outputs.py (verifier tests aligned with instructions)
- tests/test.sh (writes reward.txt and ctrf.json)
- solution/solve.py (oracle solution)
- access.log (input file)

## Notes
- Environment pinned by digest for reproducibility.
- Verifier checks actual values, not just file existence.
- Instructions match verifier exactly.

