from datetime import timedelta
from uuid import uuid4

from datasize import DataSize

from ccjudge.models import Problem


def test_configuration_creation():
    problem = Problem.create(timelimit=1, memlimit='2G')
    assert problem.timelimit.total_seconds() == 1
    assert problem.memlimit == 2 * (1000)**3


def test_model_creation():
    problem = Problem(uid=uuid4(), timelimit=timedelta(
        seconds=1), memlimit=DataSize('2G'))
    assert problem.timelimit.total_seconds() == 1
    assert problem.memlimit == 2 * (1000)**3
