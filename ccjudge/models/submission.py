import uuid
from datetime import datetime
from enum import Enum
from typing import NewType

import ccjudge.models
from ccjudge.models.base import CCJudgeBaseModel

SubmissionUid = NewType('SubmissionUid', uuid.UUID)


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
    uid: SubmissionUid
    iat: datetime
    user: ccjudge.models.User
    problem: ccjudge.models.Problem
    verdict: SubmissionVerdict
