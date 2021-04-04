from typing import Iterator

from crypto_ml.api.sample import ApiSample


class ApiHandler:
    """
    Abstract base class for API access and sample import
    """
    def iterate(self) -> Iterator[ApiSample]:
        raise NotImplementedError()
