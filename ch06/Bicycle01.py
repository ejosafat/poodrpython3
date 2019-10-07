class Bicycle(object):
    def __init__(self, **kwargs):
        self.__size = kwargs['size']
        self.__tape_color = kwargs['tape_color']

    @property
    def size(self):
        return self.__size

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

bike = Bicycle(size='M', tape_color='red')
print(bike.size)
print(bike.spares)
