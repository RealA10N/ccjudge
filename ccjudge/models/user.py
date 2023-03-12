from typing import NewType

from ccjudge.models.base import CCJudgeBaseModel

Username = NewType('Username', str)


class User(CCJudgeBaseModel):
    name: Username
