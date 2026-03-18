# Routing Decision

**Query:** "làm sao để tối ưu performance của API?"

## Analysis

| Aspect | Finding |
|--------|---------|
| **Intent** | Hỏi về cách thực hiện (how to) |
| **Topic** | Tối ưu hóa API performance |
| **Nature** | Câu hỏi kiến thức, cần khám phá nhiều phương pháp |

## Reasoning

1. **Không phải build/implement** - Không có yêu cầu tạo spec mới hoặc triển khai code
2. **Không phải fix bug** - Không có vấn đề cần sửa
3. **Không phải understand** - User đã biết rõ vấn đề (API performance), không cần phân tích thêm
4. **Phù hợp với Research** - Cần khám phá, so sánh các options (caching, indexing, pagination, load balancing, etc.)

## Route

**→ `references/research.md`**

### Why Research?

- User cần tìm hiểu các phương pháp tối ưu API
- Nhiều options khác nhau cần được phân tích, so sánh
- Query mang tính chất investigation hơn

## Next Phase After là implementation Research

Sau khi research xong, tùy thuộc vào yêu cầu cụ thể:
- Nếu cần spec → `spec-form.md`
- Nếu cần implement → `execute.md`
- Nếu chỉ cần kiến thức → trả lời trực tiếp cho user
