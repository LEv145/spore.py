class SporeApiStatusError(Exception):
    """Exception from spore API"""
    def __init__(self, status: int) -> None:
        self.status = status

    def __str__(self) -> str:
        return f"Status {self.status}"
