def prepare(messages, limit=None):
    history = list(messages)
    if limit is None:
        return history
    if limit < 0:
        raise ValueError("negative limit")
    return history[-limit:]
