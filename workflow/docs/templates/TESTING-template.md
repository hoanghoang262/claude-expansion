# Testing Standards

**Lifespan: PERMANENT — NEVER DELETE**

## Test Strategy

### Unit Tests
- Coverage target: [X%]
- Framework: [Jest / Vitest / Pytest]
- Location: [alongside source / __tests__ folder]

### Integration Tests
- Framework: [Cypress / Playwright / supertest]
- Scope: [API endpoints, component interactions]

### E2E Tests
- Framework: [Cypress / Playwright]
- Scope: [critical user journeys only]

## Test Patterns

```typescript
// Arrange-Act-Assert pattern
describe('Feature', () => {
  it('should do X when Y', () => {
    // Arrange
    const input = ...

    // Act
    const result = ...

    // Assert
    expect(result).toBe(...)
  })
})
```

## Mocking Policy

- Mock external APIs
- Mock database calls
- Don't mock internal modules unnecessarily

## CI/CD

- Tests run on: [push / PR / deployment]
- Required to pass: [all / critical only]

---

*Update when testing approach changes. Log the reason for changes.*
