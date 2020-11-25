from .abstract import Element


class Button(Element):

    def click(self):
        self._element.click()
