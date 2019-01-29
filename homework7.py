class Metaclass(type):
    """Metaclass"""

    def __init__(cls, name, bases, classdict):
        type.__init__(cls, name, bases, classdict)
        prefixes = ["get_", "set_", "del_"]
        accessors = {}

        for item in classdict.keys():
            for i in range(len(prefixes)):
                if item[:4] == prefixes[i]:
                    if item[4:] not in accessors.keys():
                        accessors[item[4:]] = [None, None, None]
                    accessors[item[4:]][i] = getattr(cls, item)

            for name, (getter, setter, deleter) in accessors.items():
                setattr(cls, name, property(getter, setter, deleter))


if __name__ == '__main__':
    class Example(metaclass=Metaclass):
        """Example class"""

        def __init__(self):
            self._x = None

        def get_x(self):
            return self._x

        def set_x(self, value):
            self._x = value

        def get_y(self):
            return 'y'

    ex = Example()
    ex.x = 255
    print(ex.x)
    print(ex.y)
