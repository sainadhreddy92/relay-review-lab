def stream_text(open_stream):
    for text in open_stream():
        if text:
            yield text
