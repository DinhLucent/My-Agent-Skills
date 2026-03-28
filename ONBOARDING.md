# 🚀 Agent Onboarding Guide — Hướng Dẫn Nhận Việc

> Đây là tài liệu **bắt buộc** cho mọi Agent mới. Hoàn thành toàn bộ trước khi bắt đầu task đầu tiên.

---

## Giai đoạn 1: Nhận diện bản thân (Identity)

### 1.1 Đọc Manifest
- Mở `manifest.yaml` tại root.
- Tìm **Agent ID** của bạn (do User cung cấp hoặc tự xác định từ context).
- Ghi nhận:
  - `persona`: Đường dẫn đến file mô tả vai trò của bạn.
  - `skills`: Danh sách các kỹ năng bạn được phép sử dụng.

### 1.2 Đọc Persona
- Mở file Persona (ví dụ: `Skills/Roles/Development/backend-developer.md`).
- **Phải nắm rõ 3 điều:**
  1. **Trách nhiệm chính** — Bạn làm gì trong team.
  2. **Ranh giới** — Bạn KHÔNG được làm gì (ví dụ: Backend Developer không tự ý quyết định kiến trúc).
  3. **Delegation Map** — Khi cần hỗ trợ, chuyển tiếp cho Agent nào.

---

## Giai đoạn 2: Nạp kỹ năng (Skill Loading)

### 2.1 Load Skills chuyên môn
Với mỗi skill trong danh sách `skills` của manifest:
1. Mở folder tương ứng (ví dụ: `Skills/Roles/Development/api-design/`).
2. Đọc `SKILL.md` — chứa hướng dẫn kích hoạt, workflow, và ví dụ sử dụng.
3. Nếu có file `workflow.md` bên trong, đọc thêm để hiểu quy trình chi tiết.

### 2.2 Load Skills chung (Global)
Mọi Agent **bắt buộc** đọc:

| File | Mục đích |
|------|---------|
| `Skills/Global/.agents/rules/security.md` | Quy tắc bảo mật — KHÔNG BAO GIỜ vi phạm |
| `Skills/Global/Evolution/SKILL.md` | Quy trình tự học — chạy sau mỗi task khó |
| `Skills/Global/brainstorm/` | Kỹ năng động não — dùng khi cần sáng tạo |
| `Skills/Global/scope-check/` | Kiểm tra phạm vi — tránh làm quá yêu cầu |

---

## Giai đoạn 3: Hiểu quy tắc vận hành (Operating Rules)

Đọc kỹ file `OPERATING_RULES.md` tại root. Tóm tắt nhanh:

### Giao tiếp với User
```
HỎI → OPTION → APPROVE → THỰC THI
```
- Luôn hỏi rõ yêu cầu trước.
- Đưa ra 2-3 phương án.
- Chỉ viết file/code khi User đã đồng ý.

### Phối hợp giữa Agents
- **Không làm việc ngoài domain** của mình.
- **Khi cần chuyên môn khác** → Đề xuất User gọi Agent phù hợp (xem Delegation Map trong Persona).
- **Khi có xung đột kỹ thuật** → Escalate lên Technical Director hoặc CTO.

---

## ✅ Onboarding Checklist

**Agent PHẢI hoàn thành tất cả mục này trước khi bắt đầu:**

- [ ] Đã đọc `manifest.yaml` và xác nhận Agent ID
- [ ] Đã đọc file Persona — hiểu trách nhiệm và ranh giới
- [ ] Đã load toàn bộ Skills chuyên môn được phân công
- [ ] Đã đọc Global Security Rules (`security.md`)
- [ ] Đã hiểu quy trình Self-Evolution (`/auto-reflect`)
- [ ] Đã đọc `OPERATING_RULES.md` — hiểu protocol giao tiếp và escalation

---

## Sau khi Onboard xong

Bạn đã sẵn sàng nhận task đầu tiên! Nhớ:
- Mỗi output phải đạt **Diamond Standard** (rõ ràng, có cấu trúc, chuyên nghiệp).
- Sau mỗi task khó, chạy `/auto-reflect` để ghi lại bài học.
- Bạn là một phần của team — luôn tôn trọng domain của Agent khác.

---
*MyAgentSkills — Powering Autonomous Departments*
