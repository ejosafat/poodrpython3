class Bicycle(object):
    def __init__(self, **kwargs):
        self.__size = kwargs['size']
        self.__chain = kwargs.get('size', self.default_chain)
        self.__tire_size = kwargs.get('tire_size', self.default_tire_size)
        self.post_initialize(**kwargs)

    @property
    def size(self):
        return self.__size

    @property
    def chain(self):
        return self.__chain

    @property
    def tire_size(self):
        return self.__tire_size

    @property
    def default_chain(self):
        return '10-speed'

    @property
    def default_tire_size(self):
        raise LookupError

    def post_initialize(self, **kwargs):
        pass

    @property
    def local_spares(self):
        return {}

    @property
    def spares(self):
        sp = self.local_spares
        sp.update({
            'tire_size': self.tire_size,
            'chain': self.chain,
        })
        return sp


class RoadBike(Bicycle):
    def post_initialize(self, **kwargs):
        self.__tape_color = kwargs['tape_color']

    @property
    def tape_color(self):
        return self.__tape_color

    @property
    def default_tire_size(self):
        return '23'

    @property
    def local_spares(self):
        return {
            'tape_color': self.tape_color,
        }


class MountainBike(Bicycle):
    def post_initialize(self, **kwargs):
        self.__front_shock = kwargs.get('front_shock', None)
        self.__rear_shock = kwargs.get('rear_shock', None)

    @property
    def front_shock(self):
        return self.__front_shock

    @property
    def rear_shock(self):
        return self.__rear_shock

    @property
    def default_tire_size(self):
        return '2.1'

    @property
    def local_spares(self):
        return {
            'rear_shock': self.rear_shock,
            'front_shock': self.front_shock,
        }

road_bike = RoadBike(size='M', tape_color='red')
print(road_bike.spares)

mountain_bike = MountainBike(size='S', front_shock='Manitou', rear_shock='Fox')
print(mountain_bike.spares)
