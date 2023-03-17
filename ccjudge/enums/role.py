from enum import auto

from ccjudge.enums.base import CCJudgeBaseStrEnum


class Role(CCJudgeBaseStrEnum):
    """ An enum representing different roles of permission in the CCJudge API. """
    Submit = auto()
    Judge = auto()
    Manage = auto()
