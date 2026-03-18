# Tối ưu Performance API

## Câu trả lời

Để tối ưu performance của API, có thể áp dụng các chiến lược sau:

### 1. Caching
- Sử dụng Redis/Memcached để cache response
- Implement ETag, Last-Modified headers
- Cache tại nhiều level: CDN, API Gateway, Application

### 2. Database Optimization
- Tạo index cho các truy vấn thường xuyên
- Sử dụng query optimization (SELECT *, JOIN tối ưu)
- Implement pagination thay vì trả toàn bộ data
- Consider read replicas cho read-heavy APIs

### 3. Code Optimization
- Sử dụng async/await cho I/O operations
- Tránh N+1 query problem
- Implement batch processing
- Tối ưu serialization/deserialization

### 4. Network & Infrastructure
- Sử dụng HTTP/2, HTTP/3
- Enable gzip/brotli compression
- Sử dụng CDN cho static assets
- Implement rate limiting

### 5. API Design
- Sử dụng pagination
- Field filtering (chỉ lấy fields cần thiết)
- Implement webhook thay vì polling
- Batch endpoints cho multiple operations

---

## Phân tích Routing

### Phase được chọn: **"Implementation/Code Optimization Phase"**

### Lý do:

1. **Mức độ phức tạp**: Câu hỏi ở mức "medium-eval-5" - đây là câu hỏi về kỹ thuật tối ưu hóa, không phải basic concept hay high-level architecture.

2. **Bối cảnh thực tiễn**: Câu hỏi yêu cầu actionable solutions - phù hợp với implementation phase hơn là research hay planning phase.

3. **Kỳ vọng đầu ra**: Cần câu trả lời technical cụ thể (caching, database optimization, code patterns) - đây là work products của implementation phase.

4. **Workflow context**: Trong context của orchestrator evaluation, "medium" complexity thường map với các phase thực hiện công việc (do, implement) thay vì các phase planning hay analysis.

**Kết luận**: Route sang Implementation Phase vì đây là câu hỏi yêu cầu giải pháp kỹ thuật cụ thể để thực hiện, không phải giai đoạn phân tích hay lập kế hoạch.
