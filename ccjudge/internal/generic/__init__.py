""" This sub-package contains different generic interfaces that are used and
required by CCJudge. The user (admin) has full freedom on how to implement
those interfaces. """

from .database import GenericDatabase
from .queue import GenericQueue

__all__ = ['GenericDatabase', 'GenericQueue']
