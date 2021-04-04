from typing import Iterator

from dataclasses import dataclass


@dataclass
class ApiSample:
    """
    Abstract base class for specific sample from API
    """


class ApiHandler:
    """
    Abstract base class for API access and sample import
    """
    def iterate(self) -> Iterator[ApiSample]:
        raise NotImplementedError()
