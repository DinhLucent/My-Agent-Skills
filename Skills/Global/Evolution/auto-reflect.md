---
description: Tự động phân tích task vừa chạy để sửa lỗi skill, lưu bài học, hoặc tạo workflow mới
---

# Workflow: `/auto-reflect` (Self-Evolution Loop)

> **Khi nào sử dụng?** 
> - Sau khi sửa xong 1 lỗi khó (bug phức tạp).
> - Sau khi cài đặt thành công 1 feature/tool mới nhưng phải qua nhiều bước.
> - Sau khi User yêu cầu "nhớ bài học này nhé", "rút kinh nghiệm", hoặc "analyze and improve".

## Các bước thực thi:

Bạn (BOT) cần thực hiện các phân tích sau một cách tuần tự (có thể làm song song nếu độc lập):

1. **Auto-Capture (Tạo Script / Workflow nếu có Pattern mới)**:
   - *Hành động*: Nhìn lại toàn bộ tool calls trong 10 bước gần nhất. Có thể đóng gói chúng thành một file markdown ngắn gọn trong `.agents/workflows/` không?
   - *Tiêu chí*: Nếu đây là 1 chuỗi lệnh cố định (ví dụ: clone -> install -> run build -> run test), hãy dùng `write_to_file` tạo ra 1 file `.agents/workflows/tên-workflow-mới.md`. Đặc biệt lưu ý thêm `// turbo` cho những bước an toàn.

2. **Auto-Fix (Sửa lỗi cho Skill/Workflow hiện tại)**:
   - *Hành động*: Nếu task vừa rồi bạn làm theo 1 workflow (hoặc skill trong `SKILL.md`) mà bị lỗi (ví dụ tool thay đổi cú pháp, API trả về khác ngày xưa), bạn PHẢI tự động `replace_file_content` hoặc `multi_replace_file_content` vào chính file `SKILL.md` / `workflow.md` đó để cập nhật sự thật mới nhất.
   - *Tiêu chí*: File phải được cập nhật ở block mô tả command hoặc parameters đã bị sai.

3. **Trích xuất Bài học (Extract Lessons)**:
   - *Hành động*: Dùng `write_to_file` (hoặc read trước rồi append/`multi_replace_file_content`) để cập nhật vào cuối file `tasks/lessons.md`.
   - *Format bắt buộc*: Tuân thủ chặt chẽ cấu trúc JSON/Markdown object đã định nghĩa trong `tasks/lessons.md` (Gồm Context, Issue, Solution, New Rule, Triggers).

4. **Báo cáo User**:
   - Sử dụng `notify_user` để hiển thị những gì đã được Cập Nhật / Đóng Gói (ví dụ: "Đã tạo workflow X", "Đã cập nhật bài học Y vào lessons.md"). Khuyến nghị tự hào về sự tối ưu này.
