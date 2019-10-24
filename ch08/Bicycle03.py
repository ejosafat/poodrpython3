class Bicycle:
    def __init__(self, **kwargs):
        self.__size = kwargs['size']
        self.__parts = kwargs['parts']

    @property
    def size(self):
        return self.__size

    @property
    def parts(self):
        return self.__parts

    @property
    def spares(self):
        return self.parts.spares


class Parts:
    def __init__(self, parts):
        self.__parts = parts

    @property
    def parts(self):
        return self.__parts

    @property
    def spares(self):
        return [part for part in self.parts if part.needs_spare]

    def __len__(self):
        return len(self.parts)

    def __iter__(self):
        return (part for part in self.parts)


class Part:
    def __init__(self, **kwargs):
        self.__name = kwargs['name']
        self.__description = kwargs['description']
        self.__needs_spare = kwargs.get('needs_spare', True)

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def needs_spare(self):
        return self.__needs_spare


chain = Part(name='chain', description='10-speed')
mountain_tire = Part(name='tire_size', description='2.1')
rear_shock = Part(name='rear_shock', description='Fox')
front_shock = Part(
    name='front_shock', description='Manitou', needs_spare=False
)

mountain_bike = Bicycle(
    size='L',
    parts=Parts(parts=(chain, mountain_tire, front_shock, rear_shock))
)
print(len(mountain_bike.spares))
print(len(mountain_bike.parts))
print([part for part in mountain_bike.parts])
