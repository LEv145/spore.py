from typing import Any, Callable
from abc import ABC, abstractmethod


class ABCBuilder(ABC):
    """Building data from raw to usable"""
    def __init__(self, decoder: Callable[[str], dict[str, Any]]) -> None:
        self._decoder = decoder

    @abstractmethod
    def build(self, raw_data: Any) -> Any:
        """Build usable data"""
