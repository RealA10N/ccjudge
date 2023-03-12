import datetime
import string
from typing import NewType

from pydantic import validator

from ccjudge.models.base import CCJudgeBaseModel

ProblemName = NewType('ProblemName', str)
ByteCount = NewType('ByteCount', int)


class Problem(CCJudgeBaseModel):
    name: ProblemName
    timelimit: datetime.timedelta
    memlimit: ByteCount

    @validator('name')
    def name_validator(cls, value: ProblemName) -> ProblemName:
        VALID_CHARS = string.ascii_lowercase + '-'
        if set(value) - set(VALID_CHARS):
            raise ValueError(
                "Problem name should contain lowercase letters and '-' only"
            )
        return value
