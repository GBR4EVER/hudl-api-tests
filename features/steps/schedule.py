import random
import string
import uuid


class Schedule:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Categories:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def post_valid_schedule():
    uniqueId = str(uuid.uuid4())
    uniqueSqlId = random.randint(1, 100000)
    print(uniqueId)
    categoryDetails = [
        Categories()
    ]
    return Schedule(
        gameId=uniqueId,
        sqlId=uniqueSqlId,
        schedule="2020-01-26T19:00:00",
        opponent="Test Opponent",
        opponentId="445",
        isHome=True,
        gameType="0",
        categoryDetailsList=categoryDetails
    )


def get_valid_schedule():
    return Schedule(
        gameId="1234567"
    )
