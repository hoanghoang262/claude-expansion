# Authentication Options Research

## Overview
This document surveys modern authentication options for web applications as of 2026.

---

## 1. OAuth 2.0 / OpenID Connect (OIDC)

### OAuth 2.0
- **What**: Authorization framework enabling third-party access without sharing credentials
- **Best for**: Delegated authorization (e.g., "Login with Google/Facebook")
- **Flows**: Authorization Code, PKCE, Client Credentials, Device Code

### OpenID Connect (OIDC)
- **What**: Identity layer on top of OAuth 2.0
- **Best for**: User authentication + authorization
- **Features**: ID tokens, userinfo endpoint, session management

### Providers
- Auth0 (now Okta)
- Cognito (AWS)
- Clerk
- Supabase Auth
- Firebase Auth

---

## 2. JWT (JSON Web Tokens)

### Self-contained tokens
- **What**: Stateless tokens containing user claims
- **Best for**: Microservices, APIs, SPA
- **Pros**: No database lookup, scalable
- **Cons**: Cannot revoke easily, token size

### Implementation Patterns
- Access tokens (short-lived, 15min-1hr)
- Refresh tokens (long-lived, stored server-side)
- JWS (signed) vs JWE (encrypted)

---

## 3. Session-based Authentication

### Traditional Sessions
- **What**: Server-side session store with session ID in cookie
- **Best for**: Server-rendered apps, traditional web apps
- **Storage**: Memory, Redis, database

### Pros/Cons
| Pros | Cons |
|------|------|
| Easy to revoke | Session store required |
| Familiar pattern | CSRF protection needed |
| Server controls | Not ideal for distributed systems |

---

## 4. SSO (Single Sign-On)

### SAML 2.0
- **What**: XML-based protocol for enterprise SSO
- **Best for**: Enterprise, legacy integration
- **Complexity**: Higher setup complexity

### OIDC-based SSO
- **What**: Modern SSO using OIDC
- **Best for**: Modern cloud apps
- **Examples**: Google Workspace, Microsoft Entra ID

---

## 5. Passwordless Authentication

### Magic Links
- **What**: Email magic link for login
- **Best for**: Reduced friction

### Email/OTP
- **What**: One-time password via email/SMS
- **Best for**: Additional security layer

### WebAuthn / FIDO2
- **What**: Passwordless authentication using biometrics/hardware keys
- **Best for**: High security, phishing resistance
- **Examples**: YubiKey, Touch ID, Face ID

---

## 6. API Keys

### Use Cases
- Service-to-service communication
- Developer API access
- Machine-to-machine auth

### Considerations
- Rotation strategy
- Scoping (read-only, full access)
- Never expose in client-side code

---

## 7. Passkeys (WebAuthn)

### What
- Passwordless standard using cryptographic key pairs
- Replaces passwords entirely
- Phishing-resistant

### Adoption
- Supported by all major browsers
- Backed by Apple, Google, Microsoft

---

## Comparison Matrix

| Method | Security | UX | Complexity | Best For |
|--------|----------|-----|------------|----------|
| OAuth2/OIDC | High | Good | Medium | Modern apps |
| JWT | Medium | Good | Low | APIs, SPAs |
| Sessions | High | Good | Medium | Traditional web |
| SSO/SAML | High | Excellent | High | Enterprise |
| Passkeys | Highest | Excellent | Medium | Passwordless |
| API Keys | Low-Medium | N/A | Low | M2M |

---

## Recommendations by Use Case

### Startup/MVP
- OAuth2 providers (Clerk, Supabase, Auth0)
- Social login + email/password

### Enterprise
- OIDC with SSO
- MFA enforcement
- SAML for legacy integration

### API-heavy
- JWT with short-lived access tokens
- Refresh token rotation
- API keys for service auth

### High Security
- Passkeys/WebAuthn
- MFA required
- Biometric support
