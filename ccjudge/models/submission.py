from datetime import datetime
from enum import Enum

from ccjudge.models import Problem, User
from ccjudge.models.base import CCJudgeBaseModel


class SubmissionVerdict(str, Enum):
    Queued = "Queued"
    Judging = "Judging"
    Right = "Right"
    Wrong = "Wrong"
    runtime_error = "RuntimeError"
    CompilationError = "CompilationError"
    MemoryExceeded = "MemoryExceeded"
    TimeExceeded = "TimeExceeded"


class Submission(CCJudgeBaseModel):
    iat: datetime
    user: User
    problem: Problem
    verdict: SubmissionVerdict
