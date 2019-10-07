class Gear(object):
    def __init__(self, chainring, cog, wheel):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel

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
        self.__rim = rim
        self.__tire = tire

    @property
    def rim(self):
        return self.__rim

    @property
    def tire(self):
        return self.__tire

    @property
    def diameter(self):
        return self.rim + (self.tire * 2)

print(Gear(52, 11, Wheel(26, 1.5)).gear_inches)
