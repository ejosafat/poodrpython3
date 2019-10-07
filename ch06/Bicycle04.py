class Bicycle(object):
    def __init__(self, **kwargs):
        self.__size = kwargs['size']

    @property
    def size(self):
        return self.__size


class RoadBike(Bicycle):
    def __init__(self, **kwargs):
        self.__tape_color = kwargs.get('tape_color', None)
        super().__init__(**kwargs)

    @property
    def tape_color(self):
        return self.__tape_color

    @property
    def spares(self):
        return {
            'chain': '10-speed',
            'tire_size': '23',
            'tape_color': self.tape_color,
        }


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
    def spares(self):
        mb_spares = super().spares
        mb_spares.update({
            'rear_shock': self.rear_shock,
            'front_shock': self.front_shock,
        })
        return mb_spares

road_bike = RoadBike(size='M', tape_color='red')
print(road_bike.size)

mountain_bike = MountainBike(size='S', front_shock='Manitou', rear_shock='Fox')
print(mountain_bike.size)
