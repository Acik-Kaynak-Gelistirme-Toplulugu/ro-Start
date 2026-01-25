# Security Policy

## 🔒 Security Commitment

We take the security of Ro-Start seriously. This document outlines our security practices and how to report vulnerabilities.

## 🛡️ Security Measures

### Input Sanitization

- All user inputs and system data are sanitized before being passed to JavaScript contexts
- Command-line arguments are validated against injection patterns
- Distribution IDs are validated using strict regex patterns

### Secure Subprocess Execution

- **No shell=True**: All subprocess calls use array arguments to prevent command injection
- Privilege escalation is handled securely through `pkexec` with validated commands
- Command arguments are never constructed from unsanitized user input

### Data Privacy

- **No external connections**: The application does not send any telemetry or analytics
- **Local-only**: All operations are performed locally on the user's machine
- **No tracking**: We do not collect, store, or transmit any user data
- System information is only gathered for local display purposes

### Logging

- Logs are stored locally in user-specific directories
- Rotating log files prevent disk space exhaustion (max 5MB × 3 backups)
- Sensitive information is never logged

## 📋 Supported Versions

We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.1.x   | :white_check_mark: |
| < 1.0   | :x:                |

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

1. **Do NOT** open a public issue
2. Contact us directly at: [security issue on GitHub](https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/ro-start/security/advisories/new)
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: varies based on severity
  - Critical: 1-3 days
  - High: 1-2 weeks
  - Medium: 2-4 weeks
  - Low: Next release cycle

## 🔐 Security Best Practices for Users

When using Ro-Start:

1. **Keep Updated**: Always use the latest version to receive security patches
2. **Verify Downloads**: Only download from official sources (GitHub releases or your distribution's repository)
3. **Review Permissions**: The application requires elevated privileges for system updates - this is expected behavior
4. **Check Logs**: Review log files in `~/.local/state/ro-start/logs/` (Linux) or `~/Library/Logs/ro-start/` (macOS) if you notice unusual behavior

## 🔍 Security Audit

Last security review: 2026-01-25

Key security features implemented:

- ✅ Input sanitization module
- ✅ Secure subprocess handling
- ✅ No external network requests
- ✅ XSS prevention in JavaScript injection
- ✅ Command injection prevention
- ✅ Secure logging practices

## 📚 Additional Resources

- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)

---

**Note**: This is a local system utility. It requires elevated privileges for system operations (updates, driver management). This is by design and necessary for the application's core functionality.
