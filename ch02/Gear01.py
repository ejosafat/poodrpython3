class Gear(object):
    def __init__(self, chainring, cog):
        self.__chainring = chainring
        self.__cog = cog

    @property
    def chainring(self):
        return self.__chainring

    @property
    def cog(self):
        return self.__cog

    @property
    def ratio(self):
        return self.chainring / self.cog

print(Gear(52, 11).ratio)
print(Gear(30, 27).ratio)
