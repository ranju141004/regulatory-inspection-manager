# SECURITY REVIEW

## Threats Identified

1. Prompt Injection
- Malicious prompts may manipulate AI behavior.

2. SQL Injection
- Unsafe query handling can expose database data.

3. XSS Attacks
- HTML/JS input may execute in frontend.

4. Rate Limit Abuse
- Excessive requests may overload AI service.

5. JWT Token Theft
- Stolen tokens can bypass authentication.

## Mitigations

- Input sanitization
- Flask limiter
- JWT validation
- Secure headers
- Prepared statements