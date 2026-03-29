# 📚 REFERENCE — Project Artifacts

> This file contains static reports and file listings. 
> DASHBOARD.md is only for active status and progress.

---

## 📅 SPRINT 1 BACKEND — Key Output Files

| Layer | File | Description |
|-------|------|-------------|
| Core | `src/lab_connector/core/models.py` | Pydantic models (ParsedResult, enums) |
| Core | `src/lab_connector/core/plugin_base.py` | AnalyzerPlugin ABC |
| Transport | `src/lab_connector/transport/base_transport.py` | BaseTransport ABC + ConnectionState |
| Transport | `src/lab_connector/transport/serial_transport.py` | Async pyserial + backoff |
| Transport | `src/lab_connector/transport/tcp_transport.py` | Async TCP client + server |
| Protocol | `src/lab_connector/protocol/astm_frame.py` | ASTM E1381 encode/decode |
| Protocol | `src/lab_connector/protocol/astm_codec.py` | Multi-frame session assembler |
| Plugin | `plugins/ca270/plugin.py` | CA270 AnalyzerPlugin |
| Plugin | `plugins/ca270/parser.py` | H/P/O/R/L record parser |
| Plugin | `plugins/ca270/test_code_map.yaml` | 19 test code mappings |
| Storage | `src/lab_connector/storage/raw_store.py` | SQLite (4 tables + replay queue) |
| Storage | `src/lab_connector/storage/file_store.py` | Binary archival disk store |
| Dispatch | `src/lab_connector/dispatch/mirth_dispatcher.py` | HTTP POST + retry + sync loop |
| Dispatch | `src/lab_connector/dispatch/offline_queue.py` | JSON offline fallback queue |
| Orchestration | `src/lab_connector/plugin_manager.py` | Plugin discovery + lifecycle |
| Config | `config/analyzers/ca270-lab-1.yaml` | Sample CA270 analyzer config |

---

## 📁 System Folders

| File | Purpose |
|------|---------|
| `.hub/backlog.yaml` | Task queue (source of truth) |
| `.hub/active/` | In-progress tasks |
| `.hub/done/` | Completed + reports |
| `.hub/handoffs/` | Agent-to-agent transfers |
| `idea_analyzerconnector.md` | Main design spec |
