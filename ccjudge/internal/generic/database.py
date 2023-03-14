from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Generic, NewType, TypeVar

from ccjudge.models.base import CCJudgeBaseModel, CCJudgeUid

ModelT = TypeVar('ModelT', bound=CCJudgeBaseModel)
FieldPathT = NewType('FieldPathT', str)


class GenericDatabase(ABC, Generic[ModelT]):
    """ A generic database, responsible for storing models used by CCJudge.
    Flexible and can be implemented as a document database, relational database,
    or any other database type. """

    @abstractmethod
    async def get(self, uid: CCJudgeUid) -> ModelT | None:
        """ Get model by unique id. If the model does not exist in the database,
        returns None. """

    @abstractmethod
    async def find(
        self,
        select: list[tuple[FieldPathT, Any]] | None = None,
        order_by: FieldPathT | None = None,
        limit: int | None = None,
    ) -> AsyncGenerator[ModelT, None]:
        """ Find models that match the given criteria in the database. 'select'
        is a list of field paths that should match the given values in all models.
        'order_by' is the field that the returned models should be sorted by.
        'limit' is the maximum number of models returned.
        """

    @abstractmethod
    async def store(self, model: ModelT) -> None:
        """ Store the given model in the database. """

    @abstractmethod
    async def remove(self, uid: CCJudgeUid) -> None:
        """ Delete the uniquely identified model from the database. Exit quietly
        if model doesn't exist already. """
