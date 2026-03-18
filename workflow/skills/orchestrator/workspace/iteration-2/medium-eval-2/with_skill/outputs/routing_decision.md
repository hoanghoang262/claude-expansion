# Routing Decision

## Question
"không biết nên dùng Redis hay MongoDB" (don't know whether to use Redis or MongoDB)

## Recommended Phase: **Brainstorming**

### Rationale

1. **Auto-suggest brainstorm triggered**: User says "không biết" (don't know) — matches SKILL.md line 38-40: "User has vague idea", "User says not sure", "Multiple options possible"

2. **Nature of Question**: This is a **technical architecture decision** — the user is uncertain between two different technologies that serve different purposes:
   - Redis: in-memory key-value store, great for caching, pub/sub, session storage
   - MongoDB: document database, good for flexible schemas, primary data storage

3. **Required Approach**:
   - Need to explore the problem space before recommending a solution
   - The right choice depends on:
     * Data model (key-value vs document)
     * Use case (cache vs primary DB)
     * Query patterns
     * Scalability requirements
     * Persistence vs speed trade-offs

4. **Phase Alignment**:
   - "Brainstorming" skill uses Socratic design refinement — perfect for exploring design decisions
   - Helps user clarify requirements before jumping to a specific technology

### Alternative Phases Considered

- **Research**: Could work, but brainstorming is better when user is uncertain and needs help clarifying their needs first
- **Planning**: Not appropriate — no clear task yet, need to understand the problem first
- **Execute**: Not appropriate — not an implementation task
- **Understand**: Not appropriate — user is not asking to understand existing code

### Next Steps (for Brainstorming phase)

1. Explore user's specific use case:
   - What type of data are they storing?
   - Is this for caching or primary storage?
   - What are their read/write patterns?
   - What scale are they expecting?

2. Present trade-offs between Redis and MongoDB based on their answers

3. Help user make informed decision based on their specific needs
