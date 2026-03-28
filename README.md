# 🏢 MyAgentSkills — Trung Tâm Điều Hành Agent AI

> **Mục tiêu:** Biến session AI của bạn thành một phòng ban phát triển phần mềm chuyên nghiệp.
> **Version:** 2.0 | **Framework:** Diamond Standard

---

## Mục lục

1. [Tổng quan](#1-tổng-quan)
2. [Kiến trúc hệ thống](#2-kiến-trúc-hệ-thống)
3. [Các thành phần chính](#3-các-thành-phần-chính)
4. [Bắt đầu sử dụng](#4-bắt-đầu-sử-dụng)
5. [Đội ngũ AI — Agents](#5-đội-ngũ-ai--agents)
6. [Kỹ năng — Slash Commands](#6-kỹ-năng--slash-commands)
7. [Luồng làm việc thực tế](#7-luồng-làm-việc-thực-tế)
8. [Quy trình HR — Tuyển dụng & Onboarding](#8-quy-trình-hr--tuyển-dụng--onboarding)
9. [Quy tắc vận hành](#9-quy-tắc-vận-hành)
10. [Tự tiến hóa — Self-Evolution](#10-tự-tiến-hóa--self-evolution)
11. [Tùy chỉnh & Mở rộng](#11-tùy-chỉnh--mở-rộng)
12. [Nguyên tắc cốt lõi](#12-nguyên-tắc-cốt-lõi)

---

## 1. Tổng quan

**MyAgentSkills** là **Trụ sở chính (HQ)** của một đội ngũ AI Agent chuyên nghiệp. Thay vì một AI đơn lẻ làm mọi việc, hệ thống cung cấp **27 "nhân viên" AI** với Persona và kỹ năng riêng biệt.

Bạn vẫn là CEO — người ra quyết định cuối cùng. AI team cung cấp chuyên môn, cấu trúc, và tốc độ.

- **Chuyên môn hóa**: Mỗi Agent một vai trò (CTO, Coder, QA, Security, v.v.)
- **Tiêu chuẩn Diamond**: Mọi kỹ năng đều có cùng format, dễ đọc và học
- **Mở rộng dễ dàng**: "Thuê" Agent mới hoặc tạo skill mới qua workflow có sẵn

---

## 2. Kiến trúc hệ thống

```
MyAgentSkills/
├── manifest.yaml           ← Sổ cái nhân sự (Agent → Persona → Skills)
├── ONBOARDING.md           ← Hướng dẫn nhận việc cho Agent mới
├── RECRUITMENT.md           ← Quy trình thuê Agent mới
├── OPERATING_RULES.md       ← Quy tắc giao tiếp & phối hợp
├── Skills/
│   ├── Global/              ← Đào tạo chung (mọi Agent phải học)
│   │   ├── Evolution/       ← Quy trình tự tiến hóa
│   │   ├── brainstorm/      ← Kỹ năng động não
│   │   ├── scope-check/     ← Kiểm tra phạm vi
│   │   └── ...
│   └── Roles/               ← Phòng ban chuyên môn
│       ├── Architecture/    ← CTO, Technical Director
│       ├── Development/     ← Backend, Frontend, Fullstack, AI
│       ├── Quality/         ← QA Lead, Performance Analyst
│       ├── Management/      ← Product Manager, Producer
│       └── Specialist/      ← Security, DevOps, Design, Data
│           ├── Security/
│           ├── DevOps/
│           ├── Design/
│           └── Data/
└── templates/               ← Khuôn mẫu tạo skill mới
```

---

## 3. Các thành phần chính

### 3.1 `manifest.yaml` — Sổ cái nhân sự

File quan trọng nhất. Định nghĩa:
- **Agent ID** — Mã định danh duy nhất
- **Persona** — File mô tả vai trò, trách nhiệm, ranh giới
- **Skills** — Danh sách kỹ năng được phân công
- **Global group** — Kỹ năng chung tự động kế thừa

### 3.2 Agents — 27 Persona theo 4 Tier

```
Tier 1 — Leadership (Cần model mạnh nhất: Opus / GPT-4o)
  CTO • Technical Director • Producer

Tier 2 — Department Leads (Model trung bình: Sonnet / GPT-4o-mini)
  Product Manager • Lead Programmer • QA Lead
  UX Designer • Release Manager

Tier 3 — Specialists (Model cân bằng: Sonnet / Gemini Flash)
  Backend • Frontend • Fullstack • AI Programmer
  Network • Tools • UI Programmer
  Security Engineer • DevOps • Data Engineer

Tier 4 — Executors (Model nhanh: Haiku / Flash)
  QA Tester • Community Manager • Analytics Engineer
```

### 3.3 Skills — 35+ kỹ năng chuẩn Diamond

Mỗi skill nằm trong một thư mục riêng, chứa `SKILL.md` với format chuẩn:
- **Triggers** — Khi nào kích hoạt
- **Instructions** — Hướng dẫn thực hiện
- **Workflow** — Quy trình chi tiết (nếu có)

### 3.4 Tài liệu HR

| File | Mục đích |
|------|---------|
| `ONBOARDING.md` | Checklist nhận việc cho Agent mới |
| `RECRUITMENT.md` | Quy trình thuê Agent mới (5 bước) |
| `OPERATING_RULES.md` | Protocol giao tiếp, escalation, handoff |

---

## 4. Bắt đầu dự án mới — Hướng dẫn chi tiết từng bước

> Đây là phần quan trọng nhất. Khi bạn có 1 dự án mới, hãy làm theo thứ tự dưới đây.

### Bước 1: Chuẩn bị dự án

```bash
# Tạo thư mục dự án mới
mkdir my-new-project && cd my-new-project
git init

# Copy bộ skill vào dự án (hoặc clone repo này)
# Cách 1: Clone trực tiếp
git clone https://github.com/<your-username>/MyAgentSkills.git .agents-skills

# Cách 2: Copy manifest + skills vào dự án
cp -r /path/to/MyAgentSkills/Skills .
cp /path/to/MyAgentSkills/manifest.yaml .
```

### Bước 2: Chọn đội hình Agent cho dự án

Mở `manifest.yaml` và **chọn các Agent phù hợp** với dự án của bạn.

**Dự án nhỏ (1 người)** — Chọn 3-4 Agent:
- `backend-agent` hoặc `fullstack-agent`
- `qa-lead-agent`
- `security-agent`

**Dự án trung bình** — Chọn 6-8 Agent:
- `cto-agent` (kiến trúc)
- `backend-agent` + `frontend-agent`
- `qa-lead-agent` + `qa-tester-agent`
- `security-agent`
- `producer-agent` (quản lý tiến độ)

**Dự án lớn** — Dùng full team 20+ Agent.

### Bước 3: Khởi chạy — Xác định trạng thái

Giao cho Agent đầu tiên (thường là `cto-agent` hoặc `producer-agent`):

| Trạng thái hiện tại | Bạn nên chạy | Kết quả |
|---------------------|-------------|---------|
| Chưa có gì, chỉ có ý tưởng | `/brainstorm` | Agent giúp cụ thể hóa ý tưởng |
| Có concept rõ ràng | `/map-systems` | Phân rã thành các module |
| Đã có thiết kế | `/sprint-plan` | Lập kế hoạch sprint đầu tiên |
| Có sẵn code rồi | `/project-stage-detect` | Phân tích đang ở phase nào |

### Bước 4: Lập kế hoạch (Sprint Planning)

```
Bạn:         "Tôi muốn xây ứng dụng quản lý bệnh nhân"
                    │
producer-agent:     Chạy /sprint-plan
                    │
                    ├── Phân tích requirements
                    ├── Chia task theo phòng ban
                    ├── Ước lượng thời gian
                    └── Output: Sprint plan với tasks + owners
                    │
Bạn:         Approve kế hoạch → Bắt đầu thực thi
```

### Bước 5: Thực thi — Giao việc cho đúng Agent

Mỗi task trong sprint plan, giao cho Agent phù hợp:

```
Task: "Thiết kế database schema cho bệnh nhân"
  → Giao cho: backend-agent
  → Agent chạy: /db-review
  → Output: Schema + migration script
  → Bạn: Review & Approve

Task: "Xây dựng REST API cho CRUD patient"
  → Giao cho: backend-agent
  → Agent chạy: /api-design → implement
  → Output: API endpoints + tests
  → Bạn: Review & Approve

Task: "Thiết kế giao diện bệnh nhân"
  → Giao cho: frontend-agent
  → Agent chạy: /design-system
  → Output: UI components
  → Bạn: Review & Approve
```

### Bước 6: Review & Bảo mật

Sau khi các Agent implement xong:

```
1. lead-programmer  → /code-review (kiểm tra chất lượng code)
2. security-agent   → /deep-scan (quét lỗ hổng bảo mật)  
3. qa-lead-agent    → /gate-check (kiểm tra readiness)
4. Bạn              → Approve hoặc yêu cầu sửa
```

### Bước 7: Release

```
1. producer-agent    → Xác nhận hoàn thành sprint
2. release-manager   → /release-checklist
3. devops-agent      → Build & deploy
4. qa-lead-agent     → Smoke test sau deploy
5. Bạn               → Xác nhận release thành công ✅
```

### Tóm tắt luồng chạy 1 dự án

```
Chuẩn bị → Chọn đội hình → Brainstorm/Planning → Sprint → 
Implement → Review → Security → Release → Retrospective → Lặp lại
```


---

## 5. Đội ngũ AI — Agents

### Gọi Agent trực tiếp

```
@cto-agent Review kiến trúc microservices này
@security-agent Audit authentication flow
@qa-lead-agent Tạo test plan cho payment feature
```

### Chuỗi chỉ huy (Delegation Chain)

```
Bạn (CEO)
  ├── CTO ──→ Technical Director ──→ Lead Programmer ──→ Developers
  ├── Product Manager ──→ UX Designer / UX Researcher
  ├── Producer ──→ Phối hợp toàn bộ team
  └── QA Lead ──→ QA Tester / Performance Analyst
```

### Quy tắc Escalation

| Vấn đề | Escalate đến |
|--------|-------------|
| Xung đột kỹ thuật | `technical-director-agent` |
| Ảnh hưởng kiến trúc tổng | `cto-agent` |
| Vấn đề scope/timeline | `producer-agent` |
| Vấn đề chất lượng | `qa-lead-agent` |
| Không chắc chắn | **Hỏi User** |

---

## 6. Kỹ năng — Slash Commands

### 🚀 Khởi chạy & Quản lý

| Command | Mô tả |
|---------|-------|
| `/start` | Onboarding — xác định bạn đang ở đâu |
| `/project-stage-detect` | Phân tích project, xác định phase |
| `/gate-check` | Kiểm tra readiness để chuyển phase |

### 🏗️ Thiết kế & Lập kế hoạch

| Command | Mô tả |
|---------|-------|
| `/brainstorm` | Động não ý tưởng sản phẩm |
| `/design-system` | Xây dựng hệ thống UI |
| `/map-systems` | Sơ đồ hóa module hệ thống |
| `/prototype` | Tạo prototype nhanh |
| `/reverse-document` | Tạo tài liệu từ code có sẵn |

### 💻 Code & Review

| Command | Mô tả |
|---------|-------|
| `/code-review` | Review code với checklist chuẩn |
| `/api-design` | Thiết kế REST/GraphQL API |
| `/db-review` | Review database schema & queries |
| `/tech-debt` | Đánh giá technical debt |
| `/perf-profile` | Phân tích performance |

### 📅 Sprint & Release

| Command | Mô tả |
|---------|-------|
| `/sprint-plan` | Lập kế hoạch sprint |
| `/estimate` | Ước lượng effort |
| `/milestone-review` | Đánh giá tiến độ milestone |
| `/retrospective` | Retrospective sau sprint |
| `/release-checklist` | Checklist release |
| `/changelog` | Tạo changelog từ commits |

### 🤝 Team Orchestration

| Command | Mô tả |
|---------|-------|
| `/team-feature` | Full team phát triển 1 feature end-to-end |
| `/team-backend` | Backend team: API → implement → test |
| `/team-frontend` | Frontend team: UX → implement → review |
| `/team-ui` | UI team: design → implement → accessibility |
| `/team-release` | Release team: build → test → deploy |

### 🛡️ Security

| Command | Mô tả |
|---------|-------|
| `/deep-scan` | Pipeline bảo mật toàn diện |
| `/secret-audit` | Tìm kiếm secret bị lộ |
| `/threat-model` | Phân tích rủi ro trước khi code |

---

## 7. Luồng làm việc thực tế

### Pattern 1: Xây dựng Feature mới

```
1. product-manager  → Phân tích requirements, viết mini-PRD
2. cto / tech-dir   → Review tính khả thi kỹ thuật
3. producer         → Lên lịch, xác định dependencies
4. ux-designer      → Thiết kế user flow (nếu UI)
5. lead-programmer  → Thiết kế API contracts
6. [developers]     → Implement (backend + frontend song song)
7. security-agent   → Security review
8. qa-lead          → Viết test cases, kiểm thử
9. Bạn              → Approve từng bước
```

### Pattern 2: Sửa Bug

```
1. qa-tester        → Tạo bug report với /bug-report
2. qa-lead          → Phân loại severity
3. lead-programmer  → Xác định root cause, assign developer
4. [developer]      → Fix bug
5. qa-tester        → Verify fix + chạy regression
```

### Pattern 3: Sprint Cycle

```
1. producer         → Lên kế hoạch với /sprint-plan
2. [All agents]     → Thực thi tasks
3. qa-lead          → Kiểm thử liên tục
4. lead-programmer  → Code review liên tục
5. producer         → Retrospective cuối sprint
```

### Pattern 4: Release Pipeline

```
1. release-manager  → Tạo release branch, chạy /release-checklist
2. qa-lead          → Full regression test
3. security-agent   → Final security scan
4. devops-agent     → Build & deploy
5. community-mgr    → Viết release notes
6. release-manager  → Monitor 48h sau deploy
```

---

## 8. Quy trình HR — Tuyển dụng & Onboarding

### Cách "thuê" Agent mới

Xem chi tiết trong `RECRUITMENT.md`. Tóm tắt:
1. Xác định vai trò cần thiết & Tier phù hợp
2. Kiểm tra nhân sự hiện có trong `manifest.yaml`
3. Tạo Persona file với 5 mục bắt buộc
4. Gán Skills từ kho có sẵn hoặc tạo mới
5. Đăng ký vào `manifest.yaml`

### Onboarding cho Agent mới

Xem chi tiết trong `ONBOARDING.md`. Agent phải hoàn thành:
- [ ] Đọc manifest, xác nhận Agent ID
- [ ] Đọc Persona, hiểu trách nhiệm & ranh giới
- [ ] Load toàn bộ Skills được phân công
- [ ] Đọc Global Security Rules
- [ ] Hiểu quy trình Self-Evolution

---

## 9. Quy tắc vận hành

Xem chi tiết trong `OPERATING_RULES.md`. Các quy tắc chính:

### Giao tiếp với User
```
HỎI → OPTION → USER OK → DRAFT → APPROVE
```

### Phối hợp giữa Agents
- Không làm việc ngoài domain
- Phát hiện lỗ hổng bảo mật → Bắt buộc báo `security-agent`
- Xung đột → Escalate theo bảng ở Section 5

### Anti-Patterns cần tránh
1. ❌ Bypass hierarchy — Developer tự quyết kiến trúc
2. ❌ Cross-domain — Sửa file ngoài phạm vi vai trò
3. ❌ Shadow decisions — Quyết định mà không document
4. ❌ Assumption-based — Đoán thay vì hỏi
5. ❌ Prototype thẳng vào production

---

## 10. Tự tiến hóa — Self-Evolution

Mọi Agent đều có khả năng tự học sau mỗi task:

- **Lệnh**: `/auto-reflect`
- **Cơ chế**:
  1. Phân tích các bước vừa thực hiện
  2. Phát hiện lỗi Skill → Tự sửa `SKILL.md`
  3. Phát hiện Pattern thành công → Tạo workflow mới
  4. Ghi bài học vào `tasks/lessons.md`

---

## 11. Tùy chỉnh & Mở rộng

### Thêm Agent mới
Sử dụng quy trình trong `RECRUITMENT.md`:
```bash
cp templates/SKILL_TEMPLATE.md Skills/Roles/<PhongBan>/<ten-agent>.md
# Chỉnh sửa nội dung → Đăng ký vào manifest.yaml
```

### Thêm Skill mới
Sử dụng workflow `create-skill.md`:
```bash
mkdir Skills/Roles/<PhongBan>/<ten-skill>
# Tạo SKILL.md theo Diamond Standard
```

### Thêm phòng ban mới
```bash
mkdir Skills/Roles/<TenPhongBan>
# Tạo personas + skills → Đăng ký vào manifest.yaml
```

---

## 12. Nguyên tắc cốt lõi

### Collaborative, KHÔNG Autonomous
Agents là **cố vấn và người thực thi**, không phải **người ra quyết định**.

### Bạn luôn là CEO
- Agents đề xuất → Bạn quyết định
- Agents thực hiện → Bạn phê duyệt
- Agents học hỏi → Bạn kiểm soát

### Chất lượng trên tốc độ
- Verify trước khi Done
- Review trước khi Merge
- Test trước khi Deploy

---
*Chúc bạn xây dựng được đội ngũ AI hùng mạnh! 🚀*
