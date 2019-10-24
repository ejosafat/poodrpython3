from Parts01 import RoadBikeParts, MountainBikeParts


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


road_bike = Bicycle(size='L', parts=RoadBikeParts(tape_color='red'))
print(road_bike.size)
print(road_bike.spares)

mountain_bike = Bicycle(
    size='L', parts=MountainBikeParts(rear_shock='Fox', front_shock='Manitou')
)

print(mountain_bike.size)
print(mountain_bike.spares)
