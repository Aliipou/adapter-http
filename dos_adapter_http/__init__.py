"""Decision OS execution adapter for generic HTTP/REST. EXPERIMENTAL.

Provides governed tools for generic HTTP/REST. Each tool is the effect BEHIND the PEP: it
runs only when the kernel permits the action. The bodies are honest stubs — wire
the real generic HTTP/REST SDK where marked. This adapter holds NO authority and never
bypasses the kernel; `governed_tools(governor)` wraps the tools so every call is
authorized + audited.
"""

from __future__ import annotations

from typing import Any


def http_request(method, url, body=None) -> str:
    # TODO: wire the real generic HTTP/REST SDK here. Until then, an honest stub.
    return f"[http] {method} {url}"


# The tool registry + per-tool capability specs (capability = "tool:<name>").
TOOLS = {"http_request": http_request}
SPECS: dict[str, dict[str, Any]] = {"http_request": {"capability": "tool:http_request"}}


def governed_tools(governor: Any) -> dict[str, Any]:
    """Wrap this adapter's tools with a decision_os_min.Governor so every call is
    routed through the kernel. Returns the governed tool registry."""
    return governor.wrap(TOOLS, specs=SPECS)
