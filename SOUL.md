# SOUL.md — Why We Work This Way

> Philosophy behind the Orchestrator-driven architecture.

---

## The Problem We Solve

AI agents are powerful but naturally chaotic. Given freedom without structure, they skip architecture, forget documentation, invent schemas on the fly, and push code that "works" but was never tested against the requirements it was supposed to satisfy.

This control plane exists to impose **discipline without bureaucracy** — structured execution packets, continuous verification, and tight lifecycle boundaries — so AI moves fast without leaving a trail of technical debt.

---

## What We Believe

**Design before code.** The architect sketches, the designer specifies, then the builder builds. Reversing this sequence is how you accumulate expensive corrections instead of cheap revisions.

**Humans decide; Algorithms orchestrate.** The human CEO sets direction via `task.yaml`. The orchestrator isolates the LLM executors to their specific roles, pushing back on bad ideas, enforcing verification boundaries, and producing professional work.

**Documentation is not an afterthought.** A feature without updated documentation is an incomplete feature. Not 90% done — incomplete.

**Tight Boundaries.** An omnipotent AI trying to do everything produces mediocre everything. The orchestrator limits context size and role definition strictly. This prevents context-collapse and hallucination.

**Context is finite and precious.** Every token wasted on redundant rules is a token stolen from problem-solving. We keep protocols lean and use RAG-like compilers to inject context just-in-time.

---

## What We Refuse

- **The "just build it" instinct.** Skipping design to start coding sooner is a loan at a very bad interest rate.
- **Scope creep dressed as progress.** Saying "not now" is a feature, not a failure.
- **Silent failures.** A task that finishes without verification and a clean execution report is a failed task.
- **Infinite loops.** The orchestrator enforces strict retry limits. If verification consistently fails, execution is halted and escalated back to the human.

---

*Built with discipline. Operated with respect. Delivered with craft.*
