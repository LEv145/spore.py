from typing import Any, Dict
from abc import ABC, abstractmethod


class ABCBuilder(ABC):
    """Building data from raw to usable"""
    @staticmethod
    @abstractmethod
    def build(raw_data: Dict[str, Any]) -> Any:
        """Build usable data"""
