import random
import string
import uuid


class Schedule:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def id_generator(size=9, char=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


