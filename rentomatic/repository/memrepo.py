
from rentomatic.domain.room import Room


class MemRepo:
    def __init__(self, data):
        self.data = [Room.from_dict(i) for i in data]

    def list(self):
        return self.data
