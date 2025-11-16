```text
Security Review — summary of measures applied

1) Settings
 - DEBUG is controlled by DJANGO_DEBUG env var. In production set DJANGO_DEBUG=0.
 - SESSION_COOKIE_SECURE = True, CSRF_COOKIE_SECURE = True (cookies sent only over HTTPS).
 - SESSION_COOKIE_HTTPONLY = True (mitigates XSS reading session cookie).
 - SECURE_SSL_REDIRECT = True (redirect HTTP to HTTPS).
 - HSTS enabled with SECURE_HSTS_SECONDS = 31536000, INCLUDE_SUBDOMAINS, PRELOAD.
 - SECURE_BROWSER_XSS_FILTER and SECURE_CONTENT_TYPE_NOSNIFF enabled.
 - X_FRAME_OPTIONS = 'DENY' to prevent framing/clickjacking.

2) Content Security Policy
 - django-csp middleware enabled. Example CSP_DEFAULT_SRC and specific CSP_SCRIPT_SRC/STYLE_SRC.
 - Optionally we add per-response CSP header in views as a reinforcement.

3) Templates and Views
 - All form templates include {% csrf_token %} to prevent CSRF attacks.
 - Use Django ModelForms (BookForm) for validation and to avoid raw SQL.
 - Use ORM filters (title__icontains) — no string formatting for SQL queries.
 - Escape user-provided values in templates (use {{ var|escape }} or rely on autoescape).

4) Deployment
 - Use SSL/TLS certificates (e.g., Let's Encrypt) and configure Nginx/Apache to terminate TLS.
 - Set SECURE_PROXY_SSL_HEADER if using a proxy/load-balancer.
 - Use environment variables for SECRET_KEY and database credentials.

Testing checklist:
 - With DEBUG=False verify site still serves and static files are served by webserver.
 - Test form submissions without CSRF token to confirm 403.
 - Inspect response headers for CSP and HSTS.
 - Use a browser or security scanner to test for common issues (XSS, insecure cookies, mixed content).
```
