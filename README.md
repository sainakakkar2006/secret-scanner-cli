# Secret Scanner CLI

**Catch leaked credentials before they reach a public repository.**

A DevSecOps command-line tool that scans a codebase for secret-like content — API keys, access tokens, passwords, private-key headers — masks the sensitive values in its output, and returns CI-friendly exit codes so pipelines can block a leaky commit automatically.

## What it detects

- Secret-like environment variable assignments (`API_KEY=...`, `PASSWORD=...`)
- Private-key headers (`-----BEGIN ... PRIVATE KEY-----`)
- GitHub-style and Slack-style tokens
- AWS-style access key IDs
- Long high-entropy strings that look like credentials

Findings are heuristic by design: the goal is to warn loudly before a push, not to prove a string is a live credential.

## Quick start

Scan the bundled sample project:

```bash
PYTHONPATH=src python -m secret_scanner scan examples/sample_project --no-fail
```

Write a JSON report (for CI artifacts or tooling):

```bash
PYTHONPATH=src python -m secret_scanner scan examples/sample_project --format json --out reports/findings.json
```

Run the test suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

### Example output

```
2 finding(s)

examples/sample_project/.env.example:1 [MEDIUM] Environment assignment with secret-like name
  value: API_****************-key

examples/sample_project/config.py:1 [MEDIUM] Environment assignment with secret-like name
  value: PASS*****************word
```

Values are **masked on purpose** — a secret scanner that echoes full secrets back to the terminal (or into CI logs) would become a leak vector itself.

## CI integration

By default the scanner exits non-zero when it finds anything, so a single line in a pipeline gates the build:

```yaml
- run: PYTHONPATH=src python -m secret_scanner scan .
```

Use `--no-fail` for report-only runs.

## Design notes

Detection rules are small, independent matchers (regex + entropy heuristics) that can be added or tuned without touching the scanning engine. Output masking and exit-code behavior are unit-tested edge cases, not afterthoughts — the failure modes of security tooling are exactly where it needs tests.

## License

MIT
