def prepare(messages, limit=None):
    '''Return a chronological snapshot, oldest first.

    With a limit, keep at most that many of the most recent messages.
    '''
    if limit is not None:
        if isinstance(limit, bool) or not isinstance(limit, int):
            raise TypeError("limit must be an integer")
        if limit < 0:
            raise ValueError("negative limit")
    history = list(messages)
    if limit is None:
        return history
    return history[-limit:] if limit else []
