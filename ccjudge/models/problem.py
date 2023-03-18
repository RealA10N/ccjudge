import datetime

from datasize import DataSize
from pydantic import validator

from ccjudge.models.base import CCJudgeBaseModel


class Problem(CCJudgeBaseModel):
    timelimit: datetime.timedelta
    memlimit: DataSize

    @validator('memlimit', pre=True)
    def convert_string_to_datasize(cls, value: str) -> DataSize:
        # Because the logic of the DataSize constructor is mainly done in the
        # __new__ and not the __init__ method, pydantic gets confused and does
        # not automatically converts strings to datasize objects. This validator
        # does that (using the pre=True flag)
        return DataSize(value)
