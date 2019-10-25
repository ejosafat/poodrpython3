class Gear(object):
    def __init__(self, chainring, cog, wheel=None):
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
