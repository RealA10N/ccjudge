from typing import IO

from ccjudge.models.base import CCJudgeBaseModel


class Blob(CCJudgeBaseModel):
    data: IO
