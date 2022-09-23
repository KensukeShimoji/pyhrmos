
from dataclasses import dataclass
import datetime
from typing import Generic, TypeVar


@dataclass
class PagenationQuery:
    """ Pagenation(問い合わせ). """

    limit: int = 25
    page: int = 1
    date_from: datetime = None
    date_to: datetime = None


T = TypeVar('T')


@dataclass
class PagenatedResponse(Generic[T]):
    """ Pagenation(レスポンス). """

    total_count: int
    total_page: int
    data: T

    @classmethod
    def of(cls, headers: dict, data: T) -> 'PagenatedResponse':  # pylint: disable=invalid-name
        """ Pagenation Response Factory. """
        return PagenatedResponse(
            total_count=int(headers['X-Total-Count']),
            total_page=int(headers['X-Total-Page']), data=data)
