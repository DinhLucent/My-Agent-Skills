---
description: Quy trình chuyên sâu tìm kiếm và xác thực Secret bị lộ
---

# Workflow: `/secret-audit`

Sử dụng workflow này định kỳ hoặc khi nghi ngờ có rò rỉ thông tin nhạy cảm.

## Các bước thực hiện:

### 1. Quét diện rộng (Broad Scan)
- Sử dụng `grep` hoặc `find_by_name` để tìm các file nhạy cảm: `.pem`, `.key`, `.p12`, `id_rsa`.
- Quét các biến môi trường và file `.env.example`.

### 2. Phân tích Entropy (Entropy Analysis)
- Tìm các chuỗi có độ hỗn loạn cao (thường là API keys/Hashes).
- Tập trung vào các file code chính và logs.

### 3. Kiểm định (Validation)
- Thử kiểm tra định dạng của key (ví dụ: AWS key thường bắt đầu bằng `AKIA`).
- **Cảnh báo**: Tuyệt đối không thử gửi request thực tế bằng key tìm thấy trừ khi User yêu cầu rõ ràng.

### 4. Xử lý (Remediation)
- Đề xuất đưa file vào `.gitignore`.
- Hướng dẫn User cách revoking key và tạo key mới.
