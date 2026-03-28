---
description: Phân tích rủi ro Socratic trước khi code một tính năng mới
---

# Workflow: `/threat-model`

Sử dụng workflow này **TRƯỚC KHI** bắt đầu lập trình một tính năng mới có tính rủi ro cao (ví dụ: Thanh toán, Upload file, Quản lý User).

## Các bước thực hiện:

### 1. Phân tích tài sản (Assets)
- Đặt câu hỏi: "Tính năng này xử lý dữ liệu gì quý giá?" (PII, Credentials, Financial data).

### 2. Nhận diện tác nhân (Threat Actors)
- Đặt câu hỏi: "Ai có thể muốn tấn công tính năng này?" (Anonymous user, Authenticated user, Malicious admin).

### 3. Phác thảo Vector tấn công (Attack Vectors)
- Dự đoán: "Họ sẽ tấn công bằng cách nào?" (SQLi vào form, Path Traversal qua upload, Brute-force login).

### 4. Thiết kế rào chắn (Mitigations)
- Đề xuất các biện pháp phòng vệ ngay từ khâu thiết kế (Security by Design).

## Kết quả đầu ra:
Một bảng tóm tắt: **Rủi ro | Tác động | Biện pháp khắc phục**.
BOT phải yêu cầu User xác nhận bảng này trước khi viết code.
