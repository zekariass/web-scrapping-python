class SiteLocator:
    def __init__(self, tag, topic):
        self.root_url = f"https://medium.com/tag/{topic}"

    @property
    def target_url(self):
        return self.root_url
