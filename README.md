# adapter-http

Decision OS / AuthGate **execution adapter** for generic HTTP/REST. It exposes an
outbound HTTP request as a **governed tool**: the request is the effect *behind* a
Policy Enforcement Point and runs only when the `decision-os-min` kernel
authorizes the action. The adapter holds **no authority** of its own and never
bypasses the kernel — every call is authorized and audited.

> Part of the Decision OS — governed by the Legitimacy ⊥ Authority pipeline
> (FDK legitimacy → AuthGate authority). Adapters adapt tools into governed
> effects and hold **no authority** of their own.

## What it adapts

| Tool | Capability | Effect |
|------|------------|--------|
| `http_request` | `tool:http_request` | Perform an HTTP request (`method`, `url`, optional `body`) |

## Install

```bash
pip install -e .          # brings in decision-os-min
# for development:
pip install -e ".[dev]"   # + pytest, ruff, mypy
```

## Usage

```python
from decision_os_min import Governor, set_actor
from dos_adapter_http import governed_tools

policy = {"grants": {"agent:ops": ["tool:http_request"]}, "default": "deny"}
gov = Governor(policy, audit_path="audit.jsonl")
tools = governed_tools(gov)

set_actor("agent:ops")
tools["http_request"]("GET", "https://example.com")   # runs only if the kernel ALLOWs
```

An actor without the matching grant raises `GovernanceRefused` before the request
runs.

## Status & limitations

**Experimental / interface-only.** The tool body is an honest stub that returns a
string describing the intended request — it does **not** perform a real HTTP call
(e.g. via `httpx`/`requests`) yet. Wire a real client at the `# TODO` marker in
`dos_adapter_http/__init__.py`. What is real today is the governance wiring: the
capability→tool mapping and the fail-closed authorization boundary.

Note: this is a single coarse-grained `http_request` tool. It does not
distinguish methods or hosts at the capability level; if you need per-host or
per-method policy, model that in the kernel policy or split the tool. This is
reference software — review and test before any production use.

## License

PolyForm Noncommercial 1.0.0 (see `LICENSE`).
