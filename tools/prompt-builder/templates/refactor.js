window.promptRegistry = window.promptRegistry || [];

window.promptRegistry.push({
    id: "refactor_clean",
    title: "Refactor Sạch (Clean Code)",
    category: "Refactor",
    tags: ["refactor", "clean-code", "quality"],
    description: "Làm gọn code rườm rà nhưng không đổi logic.",
    use_when: ["Gặp hàm 300 dòng", "Logic lồng nhau quá sâu"],
    fields: [
        { id: "module", label: "Module/File", type: "text", required: true },
        { id: "issue", label: "Vấn đề (Mùi code)", type: "select", options: ["Code quá dài", "Coupling quá cao", "Dính logic IO/Business", "Khó test"], default: "Code quá dài" }
    ],
    template: `Tôi muốn refactor code tại {{module}}. 
Vấn đề chính: {{issue}}.

Hãy:
1. Chỉ ra refactor nhỏ nhất nhưng mang lại giá trị cao về clarity
2. Đề xuất cách chia lại function/class (trước vs sau)
3. Nêu các bước refactor an toàn, đảm bảo không đổi behavior
4. Chỉ ra test cần chạy để kiểm tra.`
});

window.promptRegistry.push({
    id: "refactor_split",
    title: "Tách Module / Decoupling",
    category: "Refactor",
    tags: ["modular", "separation"],
    description: "Tách một file/class khổng lồ thành nhiều phần nhỏ.",
    use_when: ["Module 'làm cái gì cũng biết'", "File quá 1000 lines"],
    fields: [
        { id: "target", label: "Module khổng lồ", type: "text", required: true },
        { id: "new_boundaries", label: "Dự kiến các phần lẻ", type: "text" }
    ],
    template: `Module {{target}} đang quá to và ôm quá nhiều trách nhiệm. 
Dự kiến muốn tách thành: {{new_boundaries}}.

Hãy:
1. Phân tích trách nhiệm hiện tại của module
2. Đề xuất cách chia module hợp lý và khoa học
3. Xác định ranh giới (Boundary) và Interface mới giữa chúng
4. Đưa ra kế hoạch refactor theo từng phase nhỏ.`
});
