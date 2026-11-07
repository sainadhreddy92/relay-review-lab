# Relay
Relay is a small Python library that adapts a streaming chat provider and a catalog lookup tool. All integrations are injected. The library and tests run offline on Python 3.10+.

## Quick start
From the checkout, run `python -m unittest discover -v`. To install the library in your virtual environment, run `python -m pip install -e .`.

```python
from relay import respond

class Provider:
    usage = {"input_tokens": 3, "output_tokens": 2}
    def open(self, history):
        return iter(["Hi", " there"])

reply = respond(Provider(), ["hello"])
assert reply["text"] == "Hi there"
```

## Request path
`relay/gateway.py` prepares message history, consumes the provider stream, and attaches usage counters. Consumers can also use `relay.streaming.stream_text` directly to display chunks as they arrive. `relay.tools.Tools` adapts a separate catalog backend.

## Maintainer practice
This is an original interview exercise. The four contributor branches start at the same release. In a 55-minute session, spend 8 minutes reading the library, 22 reviewing the four proposals, 18 patching one proposal and testing it, and 7 explaining your changes. An AI coding assistant and web references are welcome.

1. Review all four PRs. For each, explain the intent, cite a line or test, describe the impact and record your verdict. On your own GitHub PR, submit a **Comment** review and write your verdict in its body.
2. Pick one PR. Check out its branch, add a test, run it, make the smallest justified change, rerun the suite, and push to the same branch. Add a summary describing verification and remaining risks.
