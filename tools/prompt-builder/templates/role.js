window.promptRegistry = window.promptRegistry || [];

window.promptRegistry.push({
    id: "role_backend",
    title: "Backend Session",
    category: "Role",
    tags: ["backend", "api", "service"],
    description: "Use a backend-focused session shape for server-side work.",
    use_when: ["API work", "Validation", "Jobs", "Auth", "Data access"],
    avoid_when: ["Pure UI styling"],
    fields: [
        { id: "backend_feature", label: "Feature or issue", type: "textarea", required: true, placeholder: "Describe the backend task" },
        { id: "backend_area", label: "Backend area", type: "text", required: true, placeholder: "API / auth / jobs / integration / data model" },
        { id: "backend_constraints", label: "Constraints", type: "text", default: "No breaking API changes unless explicitly required" }
    ],
    template: `Act as a strong backend engineer working inside this repository.

Context:
- Feature or issue: {{backend_feature}}
- Backend area: {{backend_area}}
- Constraints: {{backend_constraints}}

Please:
1. Identify the backend code path involved.
2. Find the right service, handler, and validation boundaries.
3. Implement or propose the smallest clean change.
4. Add or suggest the right tests.
5. Call out rollout or migration risks.`
});

window.promptRegistry.push({
    id: "role_frontend",
    title: "Frontend Session",
    category: "Role",
    tags: ["frontend", "ui", "ux"],
    description: "Use a frontend-focused session shape for UI and interaction work.",
    use_when: ["UI features", "Component work", "Page redesign", "Forms"],
    avoid_when: ["Database or backend-only work"],
    fields: [
        { id: "frontend_feature", label: "Feature or issue", type: "textarea", required: true, placeholder: "Describe the UI task" },
        { id: "frontend_area", label: "UI area", type: "text", required: true, placeholder: "Page / component / form / state / performance" },
        { id: "frontend_constraints", label: "Constraints", type: "text", default: "Match existing UI language and keep it accessible" }
    ],
    template: `Act as a strong frontend engineer working inside this repository.

Context:
- Feature or issue: {{frontend_feature}}
- UI area: {{frontend_area}}
- Constraints: {{frontend_constraints}}

Please:
1. Find the best existing UI pattern in the repo.
2. Keep the UI consistent with the current visual language.
3. Implement or propose the smallest clean change.
4. Handle loading, empty, and error states.
5. Suggest visual or interaction risks to watch for.`
});

window.promptRegistry.push({
    id: "role_fullstack",
    title: "Fullstack Session",
    category: "Role",
    tags: ["fullstack", "e2e", "integration"],
    description: "Use a fullstack session shape for changes that cross frontend and backend.",
    use_when: ["End-to-end feature work", "Cross-layer bugfixes"],
    avoid_when: ["Only one layer is involved"],
    fields: [
        { id: "fullstack_feature", label: "Feature or issue", type: "textarea", required: true, placeholder: "Describe the end-to-end change" },
        { id: "fullstack_frontend", label: "Frontend surface", type: "text", placeholder: "Which page, component, route" },
        { id: "fullstack_backend", label: "Backend surface", type: "text", placeholder: "Which API, service, model" },
        { id: "fullstack_constraints", label: "Constraints", type: "text", default: "Prefer the smallest end-to-end slice that proves value" }
    ],
    template: `Act as a fullstack engineer for this change.

Context:
- Feature or issue: {{fullstack_feature}}
- Frontend surface: {{fullstack_frontend}}
- Backend surface: {{fullstack_backend}}
- Constraints: {{fullstack_constraints}}

Please:
1. Trace the end-to-end flow.
2. Split responsibilities cleanly between frontend and backend.
3. Avoid unnecessary coupling.
4. Implement or propose the smallest end-to-end slice that proves the feature.
5. Suggest the test plan across both layers.`
});

window.promptRegistry.push({
    id: "role_qa",
    title: "QA Session",
    category: "Role",
    tags: ["qa", "testing", "risk"],
    description: "Use a QA-focused session shape for risk-based testing and release checks.",
    use_when: ["Release checks", "Regression planning", "High-risk features"],
    avoid_when: ["Pure architecture design"],
    fields: [
        { id: "qa_feature", label: "Feature or issue", type: "textarea", required: true, placeholder: "Describe the feature or change under test" },
        { id: "qa_risks", label: "Risk areas", type: "list", placeholder: "Enter one risk area at a time" },
        { id: "qa_constraints", label: "Constraints", type: "text", default: "Prioritize the smallest useful test matrix" }
    ],
    template: `Act as a QA-minded engineer reviewing this change or feature.

Context:
- Feature or issue: {{qa_feature}}
- Constraints: {{qa_constraints}}

Risk areas:
{{qa_risks}}

Please:
1. Identify the highest-risk behaviors.
2. Suggest the minimum useful test matrix.
3. Separate smoke, regression, and edge-case coverage.
4. Call out likely flaky areas.
5. Tell me what should be manually verified before release.`
});
