from datetime import date


class Ticket:
    def __init__(
        self,
        id: int,
        type: str,
        open_date: date,
        resolution_date: date,
        owner: str,
        status: str,
        comments: str,
    ):
        self.id = id
        self.type = type
        self.open_date = open_date
        self.resolution_date = resolution_date
        self.owner = owner
        self.status = status
        self.comments = comments
