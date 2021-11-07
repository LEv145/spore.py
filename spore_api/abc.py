from typing import Any, Dict, Type, TypeVar
from abc import ABC, abstractmethod


class ABCBuilder():
    """Building data from raw to usable"""

    @abstractmethod
    def build(self, raw_data: Any) -> Any:
        """Build usable data"""
