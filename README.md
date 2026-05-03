# Secret Scanner CLI

A small command-line tool that scans project files for accidentally committed secrets such as API keys, tokens, and private-key blocks. It is designed as a practical security project for a software-development portfolio.

## Why This Project Exists

Developers sometimes commit credentials by accident. This tool helps catch suspicious secrets before code is pushed to GitHub.

It demonstrates:

- file traversal
- regular expressions
- command-line interface design
- JSON and text reports
- defensive masking of sensitive values
- unit tests for edge cases

## Quick Start

```bash
PYTHONPATH=src python -m secret_scanner scan examples/sample_project --no-fail
```

Write a JSON report:

```bash
PYTHONPATH=src python -m secret_scanner scan examples/sample_project --format json --out reports/findings.json
```

Run tests:

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

## Example Output

```text
2 finding(s)

examples/sample_project/.env.example:1 [MEDIUM] Environment assignment with secret-like name
  value: API_****************-key

examples/sample_project/config.py:1 [MEDIUM] Environment assignment with secret-like name
  value: PASS*****************word
```

## What It Detects

- AWS access key IDs
- GitHub-style tokens
- Slack-style tokens
- private-key block headers
- environment variables with secret-like names
- generic high-entropy tokens

## What This Shows

This repo shows practical security awareness, clean Python, CLI design, and careful testing. It is intentionally small enough to explain clearly in an interview.
