import datetime
from typing import NewType

from ccjudge.models.base import CCJudgeBaseModel
from ccjudge.models.user import User

SessionKey = NewType('SessionKey', str)


class Session(CCJudgeBaseModel):
    user: User
    iat: datetime.datetime
    exp: datetime.datetime
