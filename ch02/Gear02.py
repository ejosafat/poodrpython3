class Gear(object):
    def __init__(self, chainring, cog, rim, tire):
        self.__chainring = chainring
        self.__cog = cog
        self.__rim = rim
        self.__tire = tire

    @property
    def chainring(self):
        return self.__chainring

    @property
    def cog(self):
        return self.__cog

    @property
    def rim(self):
        return self.__rim

    @property
    def tire(self):
        return self.__tire

    @property
    def ratio(self):
        return self.chainring / self.cog

    @property
    def gear_inches(self):
        return self.ratio * (self.rim + (self.tire * 2))

print(Gear(52, 11, 26, 1.5).gear_inches)
print(Gear(52, 11, 24, 1.25).gear_inches)
