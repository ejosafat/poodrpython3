class Bicycle(object):
    def __init__(self, **kwargs):
        self.__size = kwargs['size']
        self.__chain = kwargs.get('size', self.default_chain)
        self.__tire_size = kwargs.get('tire_size', self.default_tire_size)

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

    @property
    def spares(self):
        return {
            'tire_size': self.tire_size,
            'chain': self.chain,
        }


class RoadBike(Bicycle):
    def __init__(self, **kwargs):
        self.__tape_color = kwargs.get('tape_color', None)
        super().__init__(**kwargs)

    @property
    def tape_color(self):
        return self.__tape_color

    @property
    def default_tire_size(self):
        return '23'

    @property
    def spares(self):
        rb_spares = super().spares
        rb_spares.update({
            'tape_color': self.tape_color,
        })
        return rb_spares


class MountainBike(Bicycle):
    def __init__(self, **kwargs):
        self.__front_shock = kwargs.get('front_shock', None)
        self.__rear_shock = kwargs.get('rear_shock', None)
        super().__init__(**kwargs)

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
    def spares(self):
        mb_spares = super().spares
        mb_spares.update({
            'rear_shock': self.rear_shock,
            'front_shock': self.front_shock,
        })
        return mb_spares

road_bike = RoadBike(size='M', tape_color='red')
print(road_bike.spares)

mountain_bike = MountainBike(size='S', front_shock='Manitou', rear_shock='Fox')
print(mountain_bike.spares)
