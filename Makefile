PYTHON ?= python

.PHONY: compile compile-roles compile-docs compile-skills build-indexes dashboard-snapshot orchestrate clean help

# ══════════════════════════════════════════════════════════
# Agents-of-SHIELD v2 — Local Control Plane
# ══════════════════════════════════════════════════════════

help: ## Show this help
	@echo.
	@echo   Agents-of-SHIELD v2 Control Plane
	@echo   ==================================
	@echo.
	@echo   make compile            Compile all knowledge indexes
	@echo   make compile-roles      Compile manifest.yaml -^> role_index.json
	@echo   make compile-docs       Compile markdown docs -^> fragments
	@echo   make compile-skills     Compile Skills/ -^> skill_index.json
	@echo   make build-indexes      Build module_index.json
	@echo   make dashboard-snapshot Parse DASHBOARD.md -^> JSON snapshot
	@echo   make orchestrate        Run orchestrator with sample task
	@echo   make clean              Remove all generated runtime/compiled files
	@echo.

compile: ## Compile all knowledge source → indexes
	$(PYTHON) run_orchestrator.py compile

compile-roles: ## Compile roles from manifest.yaml
	$(PYTHON) control_plane/compiler/compile_roles.py

compile-docs: ## Compile docs into JSON fragments
	$(PYTHON) control_plane/compiler/compile_docs.py

compile-skills: ## Compile skills from Skills/
	$(PYTHON) control_plane/compiler/compile_skills.py

build-indexes: ## Build module index from source tree
	$(PYTHON) control_plane/compiler/build_indexes.py

dashboard-snapshot: ## Parse DASHBOARD.md into JSON snapshot
	$(PYTHON) control_plane/compiler/dashboard_snapshot.py

orchestrate: ## Run orchestrator with default task
	$(PYTHON) run_orchestrator.py run

orchestrate-task: ## Run orchestrator with specific task: make orchestrate-task TASK=path/to/task.yaml
	$(PYTHON) run_orchestrator.py run $(TASK)

clean: ## Remove all generated runtime/compiled files
	@if exist runtime\cache rd /s /q runtime\cache
	@if exist runtime\reports rd /s /q runtime\reports
	@if exist "runtime\state\task_packets" rd /s /q "runtime\state\task_packets"
	@if exist "runtime\state\verification_reports" rd /s /q "runtime\state\verification_reports"
	@if exist knowledge\compiled rd /s /q knowledge\compiled
	@echo Cleaned runtime and compiled artifacts.
