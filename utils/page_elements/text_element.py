from .abstract import Element


class TextElement(Element):

    @property
    def text(self):
        return self._element.text
