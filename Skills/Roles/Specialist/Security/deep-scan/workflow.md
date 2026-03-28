---
description: Toàn diện pipeline bảo mật: Recon -> Secret Scan -> SAST -> Report
---

# Workflow: `/deep-scan`

Sử dụng workflow này để thực hiện một cuộc kiểm tra bảo mật tổng thể cho một repository hoặc mục tiêu.

## Các bước thực hiện:

### 1. Trinh sát (Reconnaissance)
- [ ] Kiểm tra cấu trúc repo, xác định tech stack.
- [ ] Liệt kê các điểm đầu vào dữ liệu (API endpoints, UI forms, Webhooks).

### 2. Quét thông tin nhạy cảm (Secret Audit)
- [ ] Chạy lệnh quét Regex cho các mẫu: `api_key`, `secret`, `password`, `token`.
- [ ] Kiểm tra các file cấu hình (`.env`, `config.yml`, `settings.py`).
// turbo
- [ ] Tổng hợp danh sách các secret nghi vấn (không hiển thị full key trong log).

### 3. Phân tích mã nguồn (SAST)
- [ ] Tìm kiếm các pattern nguy hiểm: `eval()`, `os.system()`, concat chuỗi trong SQL.
- [ ] Kiểm tra lỗi logic trong xử lý phân quyền (Middleware, Auth guards).

### 4. Kiểm tra thư viện (Dependency Audit)
- [ ] Chạy `npm audit` hoặc `pip-audit` (nếu có công cụ).
- [ ] Đối soát phiên bản thư viện với dữ liệu CVE.

### 5. Tổng hợp báo cáo (Reporting)
- [ ] Xếp hạng lỗi theo mức độ: **Critical**, **High**, **Medium**, **Low**.
- [ ] Đề xuất bản vá cho các lỗi nghiêm trọng nhất.

## Lệnh thực thi:
Bạn (BOT) cần thực hiện từng bước trên và cập nhật trạng thái cho User sau mỗi bước.
