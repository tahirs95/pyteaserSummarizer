import bs4
import readability


class ContentExtractor:

    def __init__(self, raw_html):
        if hasattr(raw_html, "decode"):
            raw_html = raw_html.decode()

        self.document = readability.Document(raw_html)
        self.parser = bs4.BeautifulSoup(self.document.summary(True), "lxml")

    def _extract_images(self):
        image_tags = self.parser.find_all("img")
        if image_tags:
            return [img.attrs.get('src') for img in image_tags]
        else:
            return []

    def images(self):
        return self._extract_images()

    def content(self):
        return self.parser.text

    def title(self):
        return self.document.title()
