from collections import namedtuple


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


def Struct(**kwargs):
    return namedtuple('Struct', ' '.join(kwargs.keys()))(**kwargs)


class PartsFactory:
    @staticmethod
    def build(config, parts_class=Parts):
        return parts_class(
            [PartsFactory.create_part(part_config) for part_config in config]
        )

    @staticmethod
    def create_part(part_config):
        return Struct(
            name=part_config[0],
            description=part_config[1],
            needs_spare=part_config[2] if (len(part_config) == 3) else True
        )


road_config = (
    ('chain', '10-speed'),
    ('tire_size', '23'),
    ('tape_color', 'red'),
)

mountain_config = (
    ('chain', '10-speed'),
    ('tire_size', '2.1'),
    ('front_shock', 'Manitou', False),
    ('rear_shock', 'Fox'),
)

road_bike = Bicycle(
    size='L',
    parts=PartsFactory.build(road_config)
)
print(road_bike.spares)

mountain_bike = Bicycle(
    size='L',
    parts=PartsFactory.build(mountain_config)
)
print(mountain_bike.spares)

recumbent_config = (
    ('chain', '9-speed'),
    ('tire_size', '28'),
    ('flag', 'tall and orange'),
)

recumbent_bike = Bicycle(
    size='L',
    parts=PartsFactory.build(recumbent_config)
)

print(recumbent_bike.spares)
