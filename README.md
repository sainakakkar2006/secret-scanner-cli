# Secret Scanner CLI

This is a small command-line tool that scans files for things that look like accidentally committed secrets.

Examples of secrets are API keys, tokens, passwords, or private key headers. The tool does not prove something is definitely a real secret, but it can warn about suspicious text before code gets pushed to GitHub.

## Why I Made This

I wanted to make a small security-related project that was realistic for a student project.

The problem is simple: developers sometimes forget secrets in files like `.env`, config files, or scripts. This tool checks files and prints a report with anything suspicious.

## What It Practices

- reading files and folders
- regular expressions
- command-line arguments
- JSON and text output
- masking sensitive-looking values
- unit testing

## Quick Start

Scan the sample folder:

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

The value is masked on purpose so the tool does not print the whole suspicious string back to the terminal.

## What It Looks For

- secret-like environment variables
- private-key headers
- GitHub-style tokens
- Slack-style tokens
- AWS-style access key IDs
- long random-looking strings

## What I Learned

This project helped me practice making a useful CLI tool, writing tests around edge cases, and thinking about basic security habits in software projects.

