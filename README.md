# Relay

Relay connects a synchronous chat client to a streaming provider. Use `respond` when the caller needs a complete reply and token counts, or iterate over `stream_text` to display text as it arrives. A separate `Tools` adapter handles catalog lookups.

## Install

Relay requires Python 3.10 or later and uses the standard library at runtime. From a checkout, install it in your virtual environment:

```sh
python -m pip install -e .
```

## Get a reply

A provider supplies two things: an `open(history)` method that returns an iterable of text chunks, and a `usage` mapping with token counts. The example below uses a local provider so you can run it without credentials.

```python
from relay import respond

class GreetingProvider:
    usage = {"input_tokens": 2, "output_tokens": 3}

    def open(self, history):
        yield "Hello, "
        yield history[-1]

provider = GreetingProvider()
reply = respond(provider, ["Ada"])
assert reply["text"] == "Hello, Ada"
assert reply["usage"]["total"] == 5
```

`respond` copies the message iterable into a list in its original order, passes it to the provider, and joins the nonempty chunks. After consuming the stream, it reads `input_tokens` and `output_tokens`. Each missing counter defaults to zero. The result includes `input`, `output`, and their `total`.

## Consume a stream

Pass a callable that opens the provider stream. Relay calls it when iteration starts. Each nonempty chunk is available to the caller as soon as the provider yields it.

```python
from relay.streaming import stream_text

for chunk in stream_text(lambda: iter(["Hello", "", "!"])):
    print(chunk, end="")
# Hello!
```

## Look up a catalog item

Construct `Tools` with a callable that accepts a catalog name and an item name. Its return value becomes the result of `lookup`.

```python
from relay import Tools

catalogs = {"docs": {"install": "Getting started"}}
tools = Tools(lambda catalog, item: catalogs[catalog][item])
assert tools.lookup("docs", "install") == "Getting started"
```

## Development

Start with `relay/gateway.py` to follow a chat request through history preparation, streaming, and usage reporting. Catalog lookups have their own entry point in `relay/tools.py`. Run the test suite from the repository root:

```sh
python -m unittest discover -v
```
