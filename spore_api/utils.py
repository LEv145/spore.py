from typing import Any, Dict, List, Optional
from datetime import datetime


def datatime_from_string(string: str) -> datetime:
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S.%f")


def find_dict_by_value(
    lst: List[Dict[Any, Any]],
    seek_key: Any,
    seek_value: Any,
) -> Optional[Dict[Any, Any]]:
    for dct in lst:
        if dct.get(seek_key) == seek_value:
            return dct

    return None
