class Gear(object):
    def __init__(self, chainring, cog, observer, wheel=None):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel
        self.__observer = observer

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
    def observer(self):
        return self.__observer

    @property
    def ratio(self):
        return self.chainring / self.cog

    @property
    def gear_inches(self):
        return self.ratio * self.wheel.diameter

    def set_cog(self, new_cog):
        self.__cog = new_cog
        self.changed()

    def set_chainring(self, chainring):
        self.__chainring = chainring
        self.changed()

    def changed(self):
        self.observer.changed(self.chainring, self.cog)
