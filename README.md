# CI/CD Diagnosis Demo

This repository is used to demonstrate Kubiya's ability to troubleshoot CI/CD pipelines and analyze pull request changes.

## Features

- Kubernetes deployment YAML (in `k8s/`)
- Python app with simulated issues (`src/app.py`)
- Multi-step GitHub Actions workflow with potential failure points

## Known Issues

- The Kubernetes manifest may not pass validation
- The Python app has a function call mismatch
