from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from ccjudge.models.base import CCJudgeBaseModel

ModelT = TypeVar('ModelT', bound=CCJudgeBaseModel)


class GenericQueue(ABC, Generic[ModelT]):
    """ Queue for data that is modeled by CCJudge.
    This is an abstract definition. Subtypes of this type should implement their
    own `enqueue` and `dequeue` methods.

    Note: because this is a generic queue of CCJudge models, and the
    CCJudgeBaseModel is actually a subclass of pydantic.BaseModel, there may be
    some useful methods that you can use to manipulate the representation of
    elements in the queue. For example, it is possible to turn and model to it's
    JSON representation using the `.json()` method. It is also possible to get
    the schema using `.schema()`. For more information, check the pydantic
    documentation. """

    @abstractmethod
    async def enqueue(self, entry: ModelT) -> None:
        """ Push an element to the queue. If the method does not raise an
        exception, it should be assumed that the entry was pushed successfully,
        and now appears exactly once in the queue. """

    @abstractmethod
    async def dequeue(self) -> ModelT:
        """ Remove the next element of the queue, and return it.
        If the method does not raise an exception, it should be assumed that
        exactly one entry was removed from the queue and returned as the return
        value. """
