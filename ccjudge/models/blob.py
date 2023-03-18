from io import IOBase

from ccjudge.models.base import CCJudgeBaseModel


class Blob(CCJudgeBaseModel):
    file: IOBase

    class Config:
        arbitrary_types_allowed = True
