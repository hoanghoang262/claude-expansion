# Phân tích tái cấu trúc hệ thống thanh toán

## Nhiệm vụ: "refactor toàn bộ payment system"

---

## Quyết định: Route đến **Phase 1: Analysis/Discovery**

### Lý do:

**1. Thiếu thông tin đầu vào**
- Không có file input nào được cung cấp
- Không có context về hệ thống payment hiện tại
- Chưa xác định được: codebase ở đâu? Ngôn ngữ? Framework? Kiến trúc?

**2. Nguyên tắc phân tích trước hành động**
- Không thể refactor một hệ thống chưa hiểu rõ
- Cần xác định:
  - Các module/component liên quan đến payment
  - Dependencies và integrations (Stripe, PayPal, v.v.)
  - Business logic và edge cases
  - Technical debt và issues hiện tại

**3. Quy trình Workflow từ CLAUDE.md**
- **Workflow:** Context → implement → validate
- Phase đầu tiên luôn là thu thập Context trước

---

## Kết luận

**Phase: Analysis/Discovery**

Việc refactor toàn bộ hệ thống thanh toán đòi hỏi phải hiểu rõ hiện trạng trước. Giai đoạn Analysis sẽ:
- Scan và identify tất cả payment-related code
- Map các dependencies và integrations
- Đánh giá scope và complexity
- Đề xuất approach phù hợp

Chỉ sau khi có đầy đủ thông tin từ phase này, mới có thể lên kế hoạch và thực hiện refactor một cách hiệu quả.
