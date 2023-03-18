from abc import ABC, abstractmethod

from ccjudge.models import Blob
from ccjudge.models.base import CCJudgeUid


class GenericBlobStore(ABC):
    """ Blobs are essentially just files. Each blob is uniquely identifiable by
    a unique id, and usually the implementation of the blob manager stores the
    blobs in a "flat" structure. """

    @abstractmethod
    async def get(self, uid: CCJudgeUid) -> Blob | None:
        """ Retrieve that blob that corresponds to the given uid. None should
        be returned only if there is not, without a doubt, a blob with the
        given uid. """

    @abstractmethod
    async def store(self, blob: Blob) -> None:
        """ Store the given blob in the database. Raise an error if something
        went wrong. """

    @abstractmethod
    async def delete(self, uid: CCJudgeUid) -> None:
        """ Delete a blob with the given uid from the database. If the method
        returns, it should be guaranteed that there is no blob with the given
        uid in the database. If there is no blob with the given uid already,
        return None quietly. """
