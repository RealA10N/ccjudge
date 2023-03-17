from enum import Enum
from typing import Type, TypeVar

T = TypeVar('T')


class CCJudgeBaseStrEnum(str, Enum):
    """ A base Enum that uses strings as values (continent for configuration
    purposes). All CCJudge defined enums should inherit from this type."""

    def _generate_next_value_(name, start, count, last_values):
        """ Return the lower-cased version of the member name. Used by auto() """
        return name.lower()
