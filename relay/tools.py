class Tools:
    def __init__(self, fetch):
        self.fetch = fetch

    def lookup(self, catalog, item):
        return self.fetch(catalog, item)
