# Security Policy

## Supported Versions

The following versions of this project are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0.0 | :x:                |

## Reporting a Vulnerability

We take the security of our observability and alerting infrastructure seriously. If you discover a vulnerability or security flaw, please report it responsibly.

### Disclosure Process

1. **Private Reporting**: Please **DO NOT** file a public GitHub issue. Send your vulnerability report directly via email to **[tayyabmasood911@gmail.com](mailto:tayyabmasood911@gmail.com)** with the subject line `[SECURITY] alertmanager-pagerduty-slack-routing Vulnerability`.
2. **Details to Include**:
   - Description of the vulnerability and attack vector.
   - Exact steps or minimal proof-of-concept (PoC) to reproduce.
   - Affected configuration components, receivers, or templates.
   - Proposed mitigation or remediation patch if available.
3. **Response Timelines**:
   - **Initial Acknowledgement**: Within 24 hours.
   - **Triage & Assessment**: Within 72 hours.
   - **Remediation & Advisory Release**: Coordinated fix within 14 business days.

## Security Controls & Best Practices

- **Zero Hardcoded Secrets**: Production webhook URLs, PagerDuty routing keys, and SMTP credentials must be passed via environment variables or secret management systems (Vault, AWS Secrets Manager, Kubernetes Secrets).
- **Transport Security**: All receiver communications require TLS 1.3 encryption.
- **Least-Privilege Alert Routing**: Webhook payloads are sanitized to prevent credential and PII leakage in incident channels.

## Safe Harbor

We consider security research conducted in good faith under this policy to be authorized. We will not pursue legal action against researchers who adhere to responsible disclosure principles.
