from relay.history import prepare
from relay.streaming import stream_text
from relay.usage import usage_summary

def respond(provider, messages, limit=None):
    history = prepare(messages, limit)
    text = "".join(stream_text(lambda: provider.open(history)))
    return {"text": text, "usage": usage_summary(provider.usage)}
