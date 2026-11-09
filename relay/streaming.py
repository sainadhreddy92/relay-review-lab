def stream_text(open_stream):
    for attempt in range(2):
        try:
            for text in open_stream():
                if text:
                    yield text
            return
        except TimeoutError:
            if attempt == 1:
                raise
