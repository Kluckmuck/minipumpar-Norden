class Pdf:
    def __init__(self, x, y, size, lineHeight, lineWidth, font, fontBold):
        self.x = x
        self.y = y
        self.size = size
        self.lineHeight = lineHeight
        self.lineWidth = lineWidth
        self.font = font
        self.fontBold = fontBold

    def x():
        doc = "The x property."
        def fget(self):
            return self._x
        def fset(self, value):
            self._x = value
        def fdel(self):
            del self._x
        return locals()
    x = property(**x())
