# Global Security Rules (Antigravity-Style)

Mọi hành động của BOT trong workspace này PHẢI tuân thủ các quy tắc sau:

## 1. Xác thực và Phân quyền (Auth)
- **KHÔNG BAO GIỜ** hardcode mật khẩu, API keys, hoặc tokens vào mã nguồn.
- Sử dụng biến môi trường (`ENV`) hoặc Secret Manager.
- Luôn kiểm tra quyền truy cập (Authorization) tại các API endpoints.

## 2. Xử lý dữ liệu (Data Handling)
- **Input Validation**: Luôn validate dữ liệu đầu vào (kiểu dữ liệu, độ dài, whitelist patterns).
- **Output Sanitization**: Escape dữ liệu trước khi render lên UI (chặn XSS).
- **HTTPS Only**: Ưu tiên sử dụng HTTPS cho mọi giao thức kết nối.

## 3. Quản lý File
- Luôn validate tên file và extension khi có chức năng Upload.
- Chặn Path Traversal bằng cách không sử dụng trực tiếp input của user vào đường dẫn file hệ thống.

## 4. Ghi log và Xử lý lỗi
- Không ghi logs thông tin nhạy cảm (Credit card, Password, Full PII).
- Tắt chế độ "Debug" hoặc "Verbose error" tại môi trường sản xuất để tránh lộ cấu trúc hệ thống.

## 5. Quy trình làm việc (Strict Protocol)
- Đối với mọi task lập trình, BOT nên tự vấn: "Liệu code này có tạo ra lỗ hổng bảo mật nào không?"
- Nếu task liên quan đến bảo mật, BOT **BẮT BUỘC** kích hoạt `Security Engineer` skill.
