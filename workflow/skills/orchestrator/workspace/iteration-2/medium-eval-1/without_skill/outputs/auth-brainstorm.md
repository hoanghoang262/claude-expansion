# Brainstorm: Authentication Approaches

## Overview

Authentication (auth) là quá trình xác minh identity của user/entity. Có nhiều approaches khác nhau tùy vào use case.

---

## Các Authentication Methods

### 1. Session-based Authentication
- Server stores session in memory/database
- Session ID stored in cookie
- **Pros**: Simple, server controls logout
- **Cons**: Scalability issues, server-side state
- **Use case**: Traditional server-rendered web apps

### 2. Token-based Authentication (JWT)
- Access token + optional refresh token
- Stateless, scalable
- **Pros**: Great for APIs, microservices, SPAs
- **Cons**: Token revocation is hard, token size
- **Use case**: REST APIs, Mobile apps, SPAs

### 3. OAuth 2.0 / OIDC
- Delegated auth via third parties (Google, GitHub, etc.)
- **Pros**: No password management, trusted identity
- **Cons**: Dependency on external providers
- **Use case**: Social login, SSO

### 4. Passwordless Auth
- Magic links via email
- SMS/Email OTP
- **Pros**: No password fatigue, better security
- **Cons**: Email delivery issues
- **Use case**: Modern apps prioritizing UX

### 5. API Keys
- Static keys for machine-to-machine
- **Pros**: Simple
- **Cons**: No user-level permissions, hard to rotate
- **Use case**: Service-to-service, CI/CD

---

## Phase Routing Recommendation

**Recommended Phase: Implementation Phase**

### Why Implementation Phase?

1. **Auth là functional requirement rõ ràng** - Không cần thêm research hay analysis
2. **Đã có đủ context** - Iteration-2 implies đã qua planning
3. **Medium evaluation** - Cần show concrete code/output
4. **Orchestrator workflow** - Auth là core feature cần implement

### Alternative: Design Phase nếu:
- Chưa quyết định auth method
- Cần define auth flow chi tiết
- Cần technical design document trước

---

## Recommended Auth Architecture cho Workflow Orchestrator

```
Client / User
       │
       ▼
Auth Gateway (Layer)
    - JWT validation
    - Token refresh
       │
       ▼
Orchestrator Core
    - Workflow execution
    - Step management
    - State orchestration
```

### Suggested stack:
- JWT với short-lived access tokens (15 min)
- Refresh tokens với secure storage (HttpOnly cookies)
- OAuth 2.0 cho third-party integrations
