class Bicycle(object):
    def __init__(self, **kwargs):
        self.__size = kwargs['size']
        self.__tape_color = kwargs.get('tape_color', None)
        self.__style = kwargs['style']
        self.__front_shock = kwargs.get('front_shock', None)
        self.__rear_shock = kwargs.get('rear_shock', None)

    @property
    def size(self):
        return self.__size

    @property
    def tape_color(self):
        return self.__tape_color

    @property
    def style(self):
        return self.__style

    @property
    def front_shock(self):
        return self.__front_shock

    @property
    def rear_shock(self):
        return self.__rear_shock

    @property
    def spares(self):
        if self.style == 'road':
            return {
                'chain': '10-speed',
                'tire_size': '23',
                'tape_color': self.tape_color,
            }
        else:
            return {
                'chain': '10-speed',
                'tire_size': '2.1',
                'rear_shock': self.rear_shock,
                'front_shock': self.front_shock,
            }


bike = Bicycle(
    size='S', style='mountain', front_shock='Manitou', rear_shock='Fox'
)
print(bike.spares)
