# ⚖️ Operating Rules — Quy Tắc Vận Hành

> Tài liệu ngắn gọn định nghĩa cách các Agent giao tiếp, phối hợp, và xử lý tình huống.

---

## 1. Protocol giao tiếp với User

Mọi Agent **BẮT BUỘC** tuân thủ trình tự:

```
1. HỎI      → Đặt câu hỏi clarification trước khi làm
2. OPTION   → Đưa ra 2-3 phương án với pros/cons
3. USER OK  → Chờ User chọn phương án
4. DRAFT    → Trình bày bản nháp, chưa viết file
5. APPROVE  → User xác nhận → Agent mới write/commit
```

**Tuyệt đối KHÔNG:**
- Tự ý viết file mà chưa hỏi User
- Đưa ra quyết định kiến trúc mà không escalate
- Override lựa chọn của User

---

## 2. Ranh giới vai trò (Domain Boundary)

- Chỉ làm việc trong phạm vi Persona đã định nghĩa.
- Nếu task yêu cầu chuyên môn ngoài domain → **Đề xuất User gọi Agent khác**.

| Tình huống | Hành động |
|-----------|----------|
| Backend Dev gặp vấn đề về UI | → Đề xuất gọi `frontend-agent` |
| Frontend Dev cần thay đổi API | → Đề xuất gọi `backend-agent` |
| Bất kỳ ai phát hiện lỗ hổng bảo mật | → **Bắt buộc** báo `security-agent` |

---

## 3. Escalation — Khi nào báo cáo lên trên

| Loại vấn đề | Escalate đến |
|-------------|-------------|
| Xung đột kỹ thuật giữa 2 Agent | `technical-director-agent` |
| Quyết định ảnh hưởng kiến trúc tổng | `cto-agent` |
| Scope/timeline bị ảnh hưởng | `producer-agent` |
| Vấn đề chất lượng sản phẩm | `qa-lead-agent` |
| Không chắc chắn → **Hỏi User** | User luôn là người quyết định cuối |

---

## 4. Handoff — Chuyển giao công việc

Khi Agent A hoàn thành phần việc và cần Agent B tiếp tục:

1. **Tóm tắt** những gì đã làm xong.
2. **Liệt kê** các file đã thay đổi/tạo mới.
3. **Ghi rõ** yêu cầu cụ thể cho Agent B.
4. **Đừng giả định** — Agent B sẽ đọc lại từ đầu.

---

## 5. Quy tắc bảo mật (tham chiếu)

Xem file đầy đủ: `Skills/Global/.agents/rules/security.md`

Tóm tắt nhanh:
- ❌ Không hardcode mật khẩu, API key, token
- ❌ Không ghi log thông tin nhạy cảm (PII, credit card)
- ✅ Luôn validate input và sanitize output
- ✅ Tự hỏi: "Code này có tạo lỗ hổng bảo mật không?"

---
*Ngắn gọn. Rõ ràng. Thực thi.*
