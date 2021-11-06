from datetime import datetime


def datatime_from_string(string: str) -> datetime:
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S.%f")
