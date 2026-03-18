# Routing Decision

## Question
"không biết nên dùng Redis hay MongoDB" (don't know whether to use Redis or MongoDB)

## Recommended Phase: **Brainstorming**

### Rationale
1. **Nature of Question**: This is a **technical architecture/design decision** - not an implementation task, not a debugging task, not a code review.

2. **Required Approach**:
   - Need to explore the problem space before recommending a solution
   - Redis and MongoDB serve different purposes - the right choice depends on:
     * Data model (key-value vs document)
     * Use case (cache vs primary DB)
     * Query patterns
     * Scalability requirements

3. **Phase Alignment**:
   - "Brainstorming" skill uses Socratic design refinement - perfect for exploring design decisions
   - Helps user clarify requirements before jumping to a specific technology

### Alternative Phases Considered
- **Planning**: Not appropriate - no clear task yet, need to understand the problem first
- **Debugging**: Not appropriate - no bug to fix
- **Code Review**: Not appropriate - no code to review

### Next Steps (for Brainstorming phase)
1. Ask clarifying questions about:
   - Type of data (structured/unstructured)
   - Read/write patterns
   - Persistence requirements
   - Scale expectations
2. Present trade-offs between Redis and MongoDB
3. Help user make informed decision based on their specific needs
