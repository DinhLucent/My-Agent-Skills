# Agents-of-SHIELD: V2 Orchestrator

**A local control plane for autonomous development.**

This repository implements a local, CLI-driven orchestrator that routes natural language tasks to specialized agent profiles, executing them within a strict `compile -> plan -> execute -> verify` loop.

> **Note:** This repository previously used a manual "Task Hub" approach with individual human-managed agents. **The V2 architecture has automated this.** Agents are now logical roles executing within the `run_orchestrator.py` lifecycle.

---

## 🚀 Quick Start (V2 Workflow)

The V2 Orchestrator relies on three primary commands:

### 1. Compile Context
Generate the vector and structural indexes required by the Orchestrator.
```bash
python run_orchestrator.py compile
```
- Parses `manifest.yaml` to build the `role_index.json`.
- Compiles the project structure into `module_index.json`.
- Snapshots `DASHBOARD.md` for project context.

### 2. Define your Task
Copy `templates/task.yaml` and define the objective.
- Mention target files in `inputs.related_paths`.
- Provide concrete `acceptance_criteria`.
- Supply the `primary_commands` the agent must run to succeed.

### 3. Plan & Preview
See how the Orchestrator classifies the task, roles it, and builds the packet.
```bash
python run_orchestrator.py plan path/to/your/task.yaml
```

### 4. Execute
Run the end-to-end loop (Execution → Verification → Handoff/Done).
```bash
python run_orchestrator.py run path/to/your/task.yaml
```

---

## 🧠 System Architecture

The control plane (`control_plane/`) automates the following steps:

1. **Classifier**: Determines task type and priority.
2. **Router**: Maps the task to a role defined in `manifest.yaml`.
3. **Retriever**: Injects relevant files, tests, and documentation into the prompt.
4. **Context Builder**: Assembles a stateless "Task Packet".
5. **Execution**: The agent runs terminal commands (`metadata.execution`) locally.
6. **Verification**: The system checks `acceptance_criteria` against the execution trace.
7. **Retry/Handoff**: Automatically loops.

The orchestrator outputs its state and metrics to `runtime/` (and human-readable reports to `.hub/`).

---

## 📂 Key Directories

- **`control_plane/`**: The core execution engine.
- **`manifest.yaml`**: The skill and role configuration file parsed by the compiler.
- **`templates/`**: Boilerplates for packets, tasks, and reports.
- **`runtime/state/`**: Ephemeral data where the orchestrator saves active packets and execution traces.
- **`.hub/`**: Export directory where the orchestrator outputs human-readable statuses (`active/`, `done/`, `handoffs/`). *Do not edit files here manually.*

---

## 📚 Essential Reading

- [CHEATSHEET.md](CHEATSHEET.md): The essential reference for running tasks.
- [OPERATING_RULES.md](OPERATING_RULES.md): Security and code execution constraints.
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md): How the orchestrator binds to your Git lifecycle.
- [SOUL.md](SOUL.md): The philosophy of constrained orchestration.
