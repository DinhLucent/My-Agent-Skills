window.promptRegistry = window.promptRegistry || [];

window.promptRegistry.push({
    id: "design_v2",
    title: "Thiết kế V2 / Redesign",
    category: "Design",
    tags: ["redesign", "v2", "spec"],
    description: "Lập spec cho phiên bản nâng cấp hoặc code lại module.",
    use_when: ["Hệ thống cũ quá tải", "Thêm feature lớn phá vỡ struct cũ"],
    avoid_when: ["Chỉ cần patch nhỏ"],
    fields: [
        { id: "current_state", label: "Hệ thống hiện tại", type: "textarea", required: true, placeholder: "Mô tả struct hiện tại..." },
        { id: "pain_points", label: "Điểm yếu/Nỗi đau", type: "textarea", required: true, placeholder: "Tại sao cần redesign?" },
        { id: "keep_list", label: "Thứ cần giữ lại", type: "text" }
    ],
    template: `Tôi muốn thiết kế bản V2 cho hệ thống.

Hệ hiện tại:
{{current_state}}

Vấn đề chính của bản hiện tại:
{{pain_points}}

Những gì tuyệt đối phải giữ lại:
{{keep_list}}

Hãy tạo design spec gồm:
1. Mục tiêu V2 và Non-goals
2. Kiến trúc khối (Block architecture)
3. Module breakdown chi tiết
4. Contract/Interface chính giữa các module
5. Data model hoặc State model
6. Luồng chạy chuẩn (Happy path)
7. Chiến lược Migration từ V1 sang V2
8. Definition of Done.`
});

window.promptRegistry.push({
    id: "design_compare",
    title: "So sánh phương án kiến trúc",
    category: "Design",
    tags: ["tradeoff", "comparison", "decision"],
    description: "Phân tích Trade-off giữa hai lựa chọn kỹ thuật.",
    use_when: ["Chọn giữa 2 framework/lib", "Chọn giữa 2 pattern"],
    fields: [
        { id: "option_a", label: "Phương án A", type: "textarea", required: true },
        { id: "option_b", label: "Phương án B", type: "textarea", required: true }
    ],
    template: `Tôi đang phân vân giữa 2 hướng kiến trúc. Hãy so sánh giúp tôi.

Phương án A:
{{option_a}}

Phương án B:
{{option_b}}

Tiêu chí so sánh:
- Độ phức tạp & chi phí vận hành
- Khả năng maintain & debug
- Tốc độ triển khai (Time to market)
- Độ an toàn khi migrate

Hãy:
1. So sánh từng tiêu chí cụ thể
2. Nêu tradeoff thực tế (được gì, mất gì)
3. Đề xuất phương án khuyên dùng và lý do.`
});
