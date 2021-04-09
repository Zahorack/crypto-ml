from typing import Iterator

from dataclasses import dataclass, asdict


@dataclass
class ApiSample:
    """
    Abstract base class for specific sample from API
    """
    def to_dict(self):
        return asdict(self)


class ApiIterator:
    """
    Abstract base class for API access and sample import
    """
    def iterate(self) -> Iterator[ApiSample]:
        raise NotImplementedError()

    @property
    def api_type(self) -> str:
        raise NotImplementedError()

    @property
    def api_platform(self) -> str:
        raise NotImplementedError()
