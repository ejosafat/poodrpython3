class Gear(object):
    def __init__(self, chainring, cog, rim, tire):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = Wheel(rim, tire)

    @property
    def chainring(self):
        return self.__chainring

    @property
    def cog(self):
        return self.__cog

    @property
    def wheel(self):
        return self.__wheel

    @property
    def ratio(self):
        return self.chainring / self.cog

    @property
    def gear_inches(self):
        return self.ratio * self.wheel.diameter


class Wheel(object):
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    @property
    def diameter(self):
        return self.rim + (self.tire * 2)


print(Gear(52, 11, 26, 1.5).gear_inches)
print(Gear(52, 11, 24, 1.25).gear_inches)
