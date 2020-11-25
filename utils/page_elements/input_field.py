from .abstract import Element


class InputField(Element):

    @property
    def value(self):
        return self._element.get_attribute("value")

    @value.setter
    def value(self, value):
        self._element.clear()
        self._element.send_keys(value)
