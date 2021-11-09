from typing import Any, Callable
from abc import ABC, abstractmethod

from dataclass_wizard import JSONSerializable


class ABCBuilder(JSONSerializable, ABC):
    """Building data from raw to usable"""
    def __init__(self, decoder: Callable[[str], dict[str, Any]]) -> None:
        self._decoder = decoder

    @abstractmethod
    def build(self, raw_data: Any) -> Any:
        """Build usable data"""
