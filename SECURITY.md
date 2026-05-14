# Security Policy

## Current Status

This public repository is currently initialized for a safe baseline scaffold only.

Do not submit client data, professional data, evidence files, packet responses, secrets, credentials, database files, vector artifacts, or exported audit packets to this repository while it remains public.

## Reporting Security Issues

Report suspected security issues privately to the repository owner.

Do not open a public issue for:

- exposed secrets
- credentials
- access-control failures
- live data exposure
- evidence-file exposure
- client-specific information
- vulnerability details that could increase risk before remediation

## Prohibited Repository Content

Do not commit:

- client data
- professional roster data
- license records
- uploaded evidence
- exported audit packets containing live data
- .env files
- passwords
- API keys
- SMTP credentials
- database credentials
- private keys
- local PostgreSQL files
- SQLite files
- vector indexes
- generated caches

## Secret Handling

Secrets must be supplied through Docker Compose secrets, host secret files, or an approved deployment secret path.

.env.example may document variable names only. Real secret values are prohibited.

## AI Boundary

AI-assisted rules intelligence is required for the living rules engine, but AI authority is prohibited.

AI may not publish rules, approve or reject evidence, allocate evidence credit without review, change compliance status, send alerts without deterministic trigger data, submit filings, pay fees, sign, certify, attest, make penalty-of-perjury declarations, delete records, alter audit history, follow retrieved-document instructions, or bypass human review.

## Deterministic Authority

The deterministic evaluator remains the authority of record for compliance status.

Only human-approved rule versions, rule effective windows, person-rule assignments, reviewed evidence category allocations, deterministic evaluator outputs, approved exception or waiver decisions, and auditable human-review decisions may affect compliance status.

## Current Limit

This repository is not yet ready for build execution.

Codex remains closed.
