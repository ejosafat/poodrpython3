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
    def __init__(self, **kwargs):
        self.__parts = kwargs['parts']

    @property
    def parts(self):
        return self.__parts

    @property
    def spares(self):
        return [part for part in self.parts if part.needs_spare]


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
road_tire = Part(name='tire_size', description='23')
tape = Part(name='tape_color', description='red')
mountain_tire = Part(name='tire_size', description='2.1')
rear_shock = Part(name='rear_shock', description='Fox')
front_shock = Part(
    name='front_shock', description='Manitou', needs_spare=False
)

road_bike_parts = Parts(parts=(chain, road_tire, tape))
road_bike = Bicycle(size='L', parts=road_bike_parts)
print(road_bike.size)
print(road_bike.spares)

mountain_bike = Bicycle(
    size='L',
    parts=Parts(parts=(chain, mountain_tire, front_shock, rear_shock))
)
print(mountain_bike.size)
print(mountain_bike.spares)
