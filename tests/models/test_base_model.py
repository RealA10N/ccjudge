import uuid

import pytest
from pydantic import ValidationError

from ccjudge.models.base import CCJudgeBaseModel


@pytest.mark.parametrize('uid', (
    '00000000-0000-0000-0000-000000000000',
    uuid.uuid1(),
    uuid.uuid3(namespace=uuid.uuid1(), name="abc"),
    uuid.uuid3(namespace=uuid.uuid4(), name="123"),
    uuid.uuid5(namespace=uuid.uuid1(), name="ABC"),
    uuid.uuid5(namespace=uuid.uuid4(), name="456"),

))
def test_invalid_uids(uid):
    with pytest.raises(ValidationError):
        CCJudgeBaseModel(uid=uid)


def test_valid_uids():
    uid = uuid.uuid4()
    model = CCJudgeBaseModel(uid=uid)
    assert model.uid == uid


def test_valid_creation():
    model = CCJudgeBaseModel.create()
    assert model.uid.version == 4


def test_creation_with_existing_uid():
    with pytest.raises(ValueError):
        CCJudgeBaseModel.create(uid=uuid.uuid4())
