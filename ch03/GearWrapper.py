from Gear02 import Gear


def gear(**kwargs):
    return Gear(kwargs['chainring'], kwargs['cog'], kwargs['wheel'])
