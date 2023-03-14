from typing import NewType
from uuid import UUID

from pydantic import BaseModel

CCJudgeUid = NewType('CCJudgeUid', UUID)


class CCJudgeBaseModel(BaseModel):
    """ A base model for all models that are created and used by CCJudge. """
    uid: CCJudgeUid


__all__ = ['CCJudgeBaseModel']
