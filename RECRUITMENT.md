# 📋 Quy Trình Tuyển Dụng Agent (Recruitment Guide)

> Hướng dẫn chọn đúng Agent cho đúng vai trò, dựa trên điểm mạnh của từng loại AI.

---

## Nguyên tắc: Đúng người — Đúng việc

Mỗi AI model có điểm mạnh riêng. Chọn sai model = lãng phí token + output kém.

### Bảng phân loại Agent theo năng lực

| Tier | Vai trò phù hợp | Yêu cầu năng lực | Model khuyến nghị |
|------|-----------------|-------------------|-------------------|
| **Tier 1 — Leadership** | CTO, Technical Director, Producer | Tư duy chiến lược, phân tích trade-off, ra quyết định phức tạp | Claude Opus / GPT-4o / Gemini Pro |
| **Tier 2 — Department Lead** | Lead Programmer, PM, QA Lead, UX Designer | Phân tích sâu, review chất lượng, viết tài liệu kỹ thuật | Claude Sonnet / GPT-4o-mini |
| **Tier 3 — Specialist** | Backend, Frontend, Security, DevOps | Thực thi code, scan lỗi, chạy pipeline | Claude Sonnet / Gemini Flash / Haiku |
| **Tier 4 — Executor** | QA Tester, Community Manager, Data Entry | Task lặp đi lặp lại, format output, batch processing | Haiku / Gemini Flash / GPT-4o-mini |

---

## Quy trình 5 bước: Thuê Agent mới

### Bước 1: Xác định nhu cầu
Trả lời 3 câu hỏi:
- **Công việc cụ thể là gì?** (Ví dụ: "Cần AI review database schema")
- **Độ phức tạp ra sao?** → Chiến lược (Tier 1) hay Thực thi (Tier 3-4)?
- **Thuộc phòng ban nào?** → Architecture | Development | Quality | Management | Specialist

### Bước 2: Kiểm tra nhân sự hiện có
Mở `manifest.yaml` → Kiểm tra xem đã có Agent phù hợp chưa.
- **Có rồi?** → Gán thêm skill mới cho Agent đó.
- **Chưa có?** → Tiếp tục Bước 3.

### Bước 3: Tạo Persona cho Agent mới

```bash
# Copy template
cp templates/SKILL_TEMPLATE.md Skills/Roles/<PhongBan>/<ten-agent>.md
```

Persona **BẮT BUỘC** phải có:
- **Description**: Agent này làm gì, khi nào nên gọi.
- **Key Responsibilities**: 3-5 trách nhiệm chính, cụ thể.
- **Decision Framework**: Agent dùng tiêu chí gì để ra quyết định.
- **What This Agent Must NOT Do**: Ranh giới rõ ràng.
- **Delegation Map**: Phối hợp với ai, báo cáo ai, chuyển việc cho ai.

### Bước 4: Gán Skills
Kiểm tra kho kỹ năng hiện có:

```
Skills/Global/         → Kỹ năng chung (mọi Agent đều cần)
Skills/Roles/          → Kỹ năng chuyên môn theo phòng ban
```

- **Skill có sẵn?** → Gán trực tiếp vào manifest.
- **Skill chưa có?** → Tạo mới theo workflow `create-skill.md` trong `templates/`.

### Bước 5: Đăng ký vào Manifest

```yaml
# Thêm vào manifest.yaml
  - id: "dba-agent"
    name: "Database Administrator"
    persona: "Skills/Roles/Specialist/Data/dba.md"
    skills:
      - "Skills/Roles/Development/db-review"
      - "Skills/Roles/Quality/perf-profile"
```

---

## Checklist xác nhận tuyển dụng

- [ ] Persona file đã tạo với đầy đủ 5 mục bắt buộc
- [ ] Skills đã được gán (từ kho có sẵn hoặc tạo mới)
- [ ] Entry đã thêm vào `manifest.yaml`
- [ ] Tier đã xác định (chọn model phù hợp)

✅ Agent mới sẵn sàng onboard!
