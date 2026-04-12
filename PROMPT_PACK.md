# PROMPT_PACK

Curated prompt templates for technical sessions.

Use this file when you want a prompt that is practical, scoped, and easy to reuse.

## How To Use

- Pick one primary goal per session.
- Copy one template.
- Fill the `[brackets]`.
- Keep constraints explicit.
- Ask for code references, not generic advice.

You can write the final prompt in Vietnamese or English. The structure matters more than the language.

## Model Guide

As of 2026-04-12.

These recommendations are inferred from official model positioning, not hard vendor rules.

Important note:

- "Antigravity" is a platform, not a model family.
- For Antigravity, the relevant model choices are Gemini models used in or around that platform.

| Task type | OpenAI | Antigravity / Gemini | MiniMax | Notes |
|-----------|--------|----------------------|---------|-------|
| Deep architecture review, redesign, hard root-cause work | `gpt-5.4` | `Gemini 3 Pro` | `MiniMax-M2.7` | Use the highest-quality model when the cost of being wrong is high. |
| Default coding, debug, review, spec writing | `gpt-5.4-mini` | `Gemini 3 Flash` | `MiniMax-M2.5` | Best default balance of quality, speed, and cost. |
| Fast triage, classify, summarize, extract, batch housekeeping | `gpt-5.4-nano` | `Gemini 3 Flash` | `MiniMax-M2.5-highspeed` | Prefer this lane for repeated low-risk tasks. |
| Agentic coding inside a coding shell or tool-driven environment | `gpt-5-codex` or `gpt-5.4-mini` | `Gemini 3 Flash` for speed, `Gemini 3 Pro` for harder planning | `MiniMax-M2.5` or `MiniMax-M2.7` | Choose the faster model for iteration, the stronger model for longer-horizon tasks. |
| Browser or computer-use workflows | `gpt-5.4-mini` or `gpt-5.4` with computer-use tools | `Gemini 2.5 Computer Use` via Antigravity | Use a dedicated browser-capable agent layer | Prefer models explicitly positioned for browser control. |
| UI or component generation | `gpt-5.4-mini` for most work, `gpt-5.4` for harder redesigns | `Gemini 3 Flash` or `Gemini 3 Pro` | `MiniMax-M2.5` or `MiniMax-M2.7` | UI tasks often benefit from a strong model plus a design system prompt. |

### Official References

- OpenAI model selection: [Models](https://developers.openai.com/api/docs/models)
- OpenAI flagship model: [GPT-5.4](https://developers.openai.com/api/docs/models/gpt-5.4)
- OpenAI default mini: [GPT-5.4 mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini)
- OpenAI cheap bulk model: [GPT-5.4 nano](https://developers.openai.com/api/docs/models/gpt-5.4-nano)
- Google Antigravity + Gemini 3 overview: [Gemini 3](https://blog.google/products/gemini/gemini-3)
- Google fast coding lane: [Gemini 3 Flash](https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/)
- MiniMax strongest model: [MiniMax M2.7](https://www.minimax.io/models/text/m27)
- MiniMax default coding model: [MiniMax M2.5](https://www.minimax.io/models/text)

## Shared Session Header

Copy this at the top of most sessions.

```text
Context:
- Repo or project: [name or short description]
- System goal: [what the system does]
- My role: [owner / contributor / reviewer / maintainer]
- Current state: [what works, what is blocked]
- Constraints: [small patch only / no public API change / keep backward compatibility / no rewrite / ...]
- What I want from this session: [debug / review / spec / implementation / onboarding]

Working rules:
- Read real code before concluding
- Point to files, functions, and modules
- State assumptions clearly
- Call out bugs or architecture smells early
- Do not redesign the system unless I ask for redesign
```

## Core Prompt Modes

### 1. Onboarding

```text
I am joining this repository and need a practical technical onboarding.

Please do the following:
1. Explain what problem this repo solves.
2. Map the main architecture blocks.
3. Identify the entrypoints.
4. Trace the main end-to-end runtime flow.
5. Tell me which modules are core and which are support code.
6. If I want to work on [feature], tell me what files to read first.

Output:
- a short mental model
- the most important modules
- a recommended reading order for a new engineer
```

### 2. Debug

```text
I want to debug a specific issue without redesigning the system.

Information:
- Symptom: [describe bug]
- Expected behavior: [describe correct behavior]
- Reproduction: [steps]
- Logs or stack trace: [paste here]
- Suspected area: [optional]

Please:
1. Trace the most relevant code path.
2. Give 3-5 likely root causes in probability order.
3. Point to the files and functions I should read first.
4. Propose the smallest reasonable patch.
5. Call out regression risks.
6. Suggest tests if needed.
```

### 3. Review

```text
Review this change like a senior technical reviewer.

Focus on:
- correctness
- regression risk
- architectural fit
- missing tests

I want:
1. What the change is really doing
2. The biggest risks
3. What is fine as-is
4. What must be fixed before merge
```

### 4. Refactor

```text
I want a small, safe refactor without changing behavior.

Target:
- module or file: [path]
- problem: [too long / duplicate logic / mixed responsibilities / hard to test]
- constraints: [no public API change / no behavior change / minimal patch]

Please:
1. Identify the smallest high-value refactor.
2. Suggest the new boundaries.
3. Tell me what tests should exist first.
4. Give me a safe step-by-step plan.
```

### 5. Spec Writing

```text
I want a design spec that another team can implement.

Context:
- current system: [summary]
- what must stay: [summary]
- what must change: [summary]
- constraints: [deadline / compatibility / team size / rollout limits]

Please write:
1. Goals
2. Non-goals
3. Architecture
4. Module breakdown
5. Interfaces
6. State or data flow
7. Migration strategy
8. Acceptance criteria
```

## Common Build Prompts

These are the prompts that were missing from an analysis-heavy prompt pack.

### Add Component

```text
I want to add a new UI component.

Context:
- Stack: [React / Vue / Next.js / plain HTML / other]
- Design system: [shadcn / custom / Tailwind / none]
- Where it should live: [page, route, folder]
- Inputs and outputs: [props, events, data]
- Constraints: [match existing style / mobile-first / accessible / no new dependency / ...]

Please:
1. Find the best existing pattern in the repo.
2. Tell me which files to inspect first.
3. Implement the smallest clean version that fits the current codebase.
4. Add or update tests if appropriate.
5. Explain any styling or state-management decisions briefly.
```

### Add Page Or Screen

```text
I want to add a new page or screen.

Context:
- Route or screen name: [name]
- Goal of the page: [what users should do here]
- Data dependencies: [APIs, loaders, props, stores]
- UI constraints: [desktop/mobile, design system, auth, SEO]

Please:
1. Identify the routing and layout files involved.
2. Reuse existing patterns where possible.
3. Add the page with minimal unnecessary abstraction.
4. Wire data loading and empty/error states.
5. Tell me what should be tested manually and automatically.
```

### Add API Endpoint

```text
I want to add a new API endpoint.

Context:
- Framework: [FastAPI / Express / Django / Rails / other]
- Endpoint: [method + path]
- Input: [request body, params, auth]
- Output: [response shape]
- Constraints: [no breaking change / validate input / audit logging / rate limit / ...]

Please:
1. Find similar endpoints in the repo.
2. Identify the handler, service, and validation layers involved.
3. Implement the endpoint in the repo's existing style.
4. Add or update tests.
5. Call out any migration, auth, or rollout concerns.
```

### Add Form And Validation

```text
I want to add a form with validation.

Context:
- Form purpose: [what users submit]
- Fields: [list]
- Validation rules: [rules]
- Submission target: [endpoint or action]
- UX constraints: [inline errors / optimistic UI / debounce / accessibility]

Please:
1. Reuse the current form pattern in the codebase.
2. Keep validation rules close to the form or shared only if already common.
3. Implement success, loading, and error states.
4. Add tests for the critical validation behavior.
```

### Add Database Migration

```text
I want to add a database migration safely.

Context:
- Database: [Postgres / MySQL / SQLite / other]
- ORM or migration tool: [tool]
- Change: [new table / column / index / data backfill / constraint]
- Constraints: [zero downtime / backward compatibility / large table / rollback required]

Please:
1. Explain the blast radius.
2. Suggest the safest migration sequence.
3. Separate schema change from backfill if needed.
4. Tell me what to verify before and after deploy.
```

### Add Integration

```text
I want to integrate [service or SDK].

Context:
- Service: [name]
- Use case: [what the integration should do]
- Secrets or config: [env vars, auth method]
- Constraints: [sandbox first / no new infra / no blocking calls on request path / ...]

Please:
1. Find where similar integrations live in this repo.
2. Suggest the right boundary for this integration.
3. Implement the minimal safe version.
4. Add config validation and failure handling.
5. Tell me how to test it without breaking production.
```

### Add Tests

```text
I changed [feature or module] and want the right tests, not random tests.

Please:
1. Tell me what behavior matters most.
2. Suggest the minimum useful test plan.
3. Separate unit, integration, and end-to-end tests.
4. Prioritize regression protection over coverage vanity.
```

### Add CLI Command Or Script

```text
I want to add a new CLI command or utility script.

Context:
- Command name: [name]
- What it should do: [description]
- Inputs: [flags, args, config]
- Outputs: [stdout, files, reports]
- Constraints: [idempotent / safe by default / dry-run / no destructive default]

Please:
1. Find the best existing command pattern in the repo.
2. Keep the interface consistent with existing commands.
3. Add validation and clear error messages.
4. Suggest basic tests or smoke checks.
```

## Planning And Leadership Prompts

These prompts are for CTO-style planning, architecture decisions, and execution planning.

### CTO Improvement Plan For An Existing Repo

```text
I have inherited this repository and want to improve it deliberately, not randomly.

Please help me create a CTO-style improvement plan.

Context:
- What the repo does: [summary]
- Current strengths: [summary]
- Current pain points: [summary]
- Constraints: [small team / deadline / must keep compatibility / cannot pause delivery / ...]
- My priorities: [reliability / speed / architecture / onboarding / product quality / ...]

Please:
1. Assess the current system honestly.
2. Separate core strengths from technical debt.
3. Identify the top 3-5 leverage points.
4. Split the plan into quick wins, medium refactors, and major redesigns.
5. Tell me what should not be touched yet.
6. Give me a realistic execution order.
```

### Sprint Plan

```text
I want to turn the current priorities into a realistic sprint plan.

Context:
- Sprint length: [1 week / 2 weeks / other]
- Team shape: [backend / frontend / fullstack / QA / mixed]
- Current priorities: [list]
- Constraints: [release pressure / tech debt / blocked dependencies / ...]

Please:
1. Group the work into a coherent sprint.
2. Separate must-do from nice-to-have.
3. Identify dependencies and sequencing.
4. Suggest task granularity that is easy to assign.
5. Add clear acceptance criteria for each work item.
6. Call out the main sprint risks.
```

### Work Breakdown Structure

```text
I have a large technical initiative and need it split into executable tasks.

Initiative:
- [description]

Constraints:
- [deadline / team size / ownership / architecture boundaries / ...]

Please:
1. Break the initiative into workstreams.
2. Split each workstream into concrete tasks.
3. Mark dependencies.
4. Mark what can run in parallel.
5. Suggest the best execution order.
6. Keep task size practical for engineering work, not management theater.
```

### ADR

```text
I want to write an ADR for this technical decision.

Decision:
- [what we are deciding]

Context:
- Current system: [summary]
- Problem: [summary]
- Constraints: [cost / performance / compatibility / delivery / team skill / ...]
- Options considered: [A / B / C]

Please write:
1. Title
2. Status
3. Context
4. Decision
5. Alternatives considered
6. Consequences
7. Risks
8. Follow-up actions
```

### Technical Roadmap

```text
I want a technical roadmap for the next [time period].

Context:
- Product direction: [summary]
- Current engineering state: [summary]
- Known debt: [summary]
- Team constraints: [summary]

Please:
1. Organize the roadmap into phases.
2. Separate platform work from product work.
3. Explain why each phase is in that order.
4. Identify dependencies and risk.
5. Suggest milestones that are meaningful, not decorative.
```

## Role-Specific Session Prompts

Use these when you want the model to behave like a focused backend, frontend, fullstack, or QA partner.

### Backend Session

```text
Act as a strong backend engineer working inside this repository.

Context:
- Feature or issue: [description]
- Backend area: [API / data model / auth / jobs / caching / integration / other]
- Constraints: [no breaking API / performance-sensitive / backward compatible / ...]

Please:
1. Identify the backend code path involved.
2. Find the right service, handler, and validation boundaries.
3. Implement or propose the smallest clean change.
4. Add or suggest the right tests.
5. Call out rollout or migration risks.
```

### Frontend Session

```text
Act as a strong frontend engineer working inside this repository.

Context:
- Feature or issue: [description]
- UI area: [page / component / form / state / design system / performance]
- Constraints: [match existing UI / mobile-first / accessible / no design drift / ...]

Please:
1. Find the best existing UI pattern in the repo.
2. Keep the UI consistent with the current visual language.
3. Implement or propose the smallest clean change.
4. Handle loading, empty, and error states.
5. Suggest visual or interaction risks I should watch for.
```

### Fullstack Session

```text
Act as a fullstack engineer for this change.

Context:
- Feature or issue: [description]
- Frontend surface: [summary]
- Backend surface: [summary]
- Constraints: [delivery speed / backward compatibility / minimal schema churn / ...]

Please:
1. Trace the end-to-end flow.
2. Split responsibilities cleanly between frontend and backend.
3. Avoid unnecessary coupling.
4. Implement or propose the smallest end-to-end slice that proves the feature.
5. Suggest the test plan across both layers.
```

### QA Session

```text
Act as a QA-minded engineer reviewing this change or feature.

Context:
- Feature or issue: [description]
- Risk areas: [summary]
- Constraints: [time pressure / no full regression pass / release candidate / ...]

Please:
1. Identify the highest-risk behaviors.
2. Suggest the minimum useful test matrix.
3. Separate smoke, regression, and edge-case coverage.
4. Call out likely flaky areas.
5. Tell me what should be manually verified before release.
```

## High-Leverage Scenario Prompts

### Improve A Repo According To My Direction

```text
I have this repository and want to improve it according to my own direction, not just fix random bugs.

My direction:
- [faster development / better architecture / cleaner UI / stronger testing / better onboarding / lower ops risk / ...]

Context:
- What the repo does: [summary]
- What already works: [summary]
- What annoys me most: [summary]
- Constraints: [no rewrite / small team / active delivery / compatibility / ...]

Please:
1. Understand the current system first.
2. Tell me what is actually blocking my direction today.
3. Separate superficial cleanup from high-leverage changes.
4. Propose a phased improvement plan.
5. Suggest the first concrete change worth making now.
```

### Build From Zero

```text
I want to create a new technical system from zero.

Goal:
- [what I want to build]

Context:
- Users: [who it is for]
- Core use case: [main workflow]
- Constraints: [timeline / team size / stack preference / hosting / budget / compliance / ...]

Please:
1. Clarify the core scope.
2. Separate MVP from later expansion.
3. Propose the architecture that is simplest but still credible.
4. Suggest module boundaries and contracts.
5. Give me a phased implementation plan.
6. Tell me the biggest mistakes to avoid in version 1.
```

### Fix Issue

```text
I want to fix a real issue quickly and correctly.

Context:
- Issue: [bug / regression / incident / failing check / broken flow]
- Impact: [who or what is affected]
- Reproduction: [steps]
- Logs or evidence: [paste here]
- Constraints: [hotfix / no migration / no API break / patch today / ...]

Please:
1. Trace the code path.
2. Give likely root causes in probability order.
3. Identify the smallest safe fix.
4. Tell me what test should lock the fix in.
5. Call out any rollback or deployment considerations.
```

## Repo-Specific Agent Runtime Prompts

### Investigate Task Failure

```text
I am debugging a failed task run in the agent runtime.

Please inspect:
- task YAML
- task packet
- execution report
- verification report
- metrics
- done or handoff artifact

I want:
1. The actual failure point
2. Whether the problem is in execute, verify, retry, or state transition
3. The smallest next fix
```

### Investigate Verifier Failure

```text
A task executed, but verification failed.

Please:
1. Identify which checks failed.
2. Explain what evidence the verifier used.
3. Tell me whether the verifier is correct, too strict, or missing context.
4. Suggest whether to fix execution, verifier rules, or retry augmentation.
```

### Investigate Retry Loop

```text
The retry loop is not behaving as expected.

Please inspect:
- verification_report.json
- next_context_needs
- retry packet
- retry metrics
- task state history

I want:
1. Where retry is being decided
2. Why the retry was or was not useful
3. Whether the retry packet added the right context
4. The smallest change to improve retry quality
```

### Shrink Oversized Packets

```text
Task packets are getting too large.

Please:
1. Find what is being pulled into the packet.
2. Separate required context from default noise.
3. Point to the retriever or packet builder logic responsible.
4. Propose the smallest change that keeps correctness while reducing size.
```

### Migrate Execution Metadata To A Stronger Contract

```text
The executor currently depends on ad hoc execution metadata.

Please:
1. Analyze the current execution fields in task YAML.
2. Separate required, optional, and ambiguous fields.
3. Propose a stronger typed contract.
4. Suggest a migration path that does not break old tasks immediately.
```

## Meta Prompt

Use this when you do not know which mode to choose.

```text
I am not sure whether this is onboarding, debug, review, refactor, redesign, or spec writing.

Context:
- [short description]

Please:
1. Classify the situation
2. Choose the best mode
3. Solve it using that mode
4. Do not pull in unrelated work
```
