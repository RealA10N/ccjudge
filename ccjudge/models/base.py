import uuid
from typing import NewType, Type, TypeVar

from pydantic import BaseModel, validator

CCJudgeUid = NewType('CCJudgeUid', uuid.UUID)
T = TypeVar('T')


class CCJudgeBaseModel(BaseModel):
    """ A base model for all models that are created and used by CCJudge. """
    uid: CCJudgeUid

    @validator('uid')
    def validate_random_uuid(cls, value: CCJudgeUid) -> CCJudgeUid:
        if value.version != 4:
            # This also covers the nil uuid which has no specified version
            raise ValueError("Only random UUID (version 4) is supported")
        return value

    @classmethod
    def create(cls: Type[T], **kwargs) -> T:
        """ Generate a random UUID and create a new model with the given args
        and kwargs."""
        if 'uid' in kwargs:
            raise ValueError(
                "Can't construct a new model when uid is provided")
        return cls(**{'uid': uuid.uuid4()} | kwargs)


__all__ = ['CCJudgeBaseModel']
