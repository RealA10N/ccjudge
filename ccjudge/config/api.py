from datetime import timedelta
from typing import Mapping, TypeAlias

from pydantic import PositiveInt, validator

from ccjudge.config.base import CCJudgeBaseConfigModel
from ccjudge.enums import Role

TimeframeLimitT: TypeAlias = tuple[PositiveInt, timedelta]


class APIConfig(CCJudgeBaseConfigModel):

    # credentials
    jwt_key: str
    pwd_key: str

    # sessions
    max_session: Mapping[Role, timedelta] = {
        Role.Submit: timedelta(weeks=2),
        Role.Judge: timedelta(days=3),
        Role.Manage: timedelta(days=1),
    }

    @validator('max_session')
    def max_sessions_for_all_roles(cls, value: Mapping[Role, timedelta]) -> Mapping[Role, timedelta]:
        if set(Role) != set(value.keys()):
            raise ValueError('Max session length not defined to all roles')
        return value
