# Security Policy — ANTLR4_JSBach

## Reporting a Vulnerability
If you discover a security vulnerability, please email polcg10@gmail.com. Do not open a public issue.

## Security Considerations
- This is an academic ANTLR4-based music interpreter written in Python.
- It has no network or web components.
- The interpreter invokes external processes (LilyPond, Timidity, FFmpeg) to render and play music. Only run trusted `.jsbach` input files, as malicious input could potentially craft dangerous arguments to these subprocesses.
- Not intended for use with untrusted input or in production environments.
