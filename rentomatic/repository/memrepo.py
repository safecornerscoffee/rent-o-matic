from rentomatic.domain.room import Room


class MemRepo:
    def __init__(self, data):
        self.data = [Room.from_dict(i) for i in data]

    def list(self, filters=None):

        result = self.data

        if filters is None:
            return result

        if "code__eq" in filters:
            result = [r for r in result if r.code == filters["code__eq"]]

        if "price__eq" in filters:
            result = [r for r in result if r.price == int(filters["price__eq"])]

        if "price__lt" in filters:
            result = [r for r in result if r.price < int(filters["price__lt"])]

        if "price__gt" in filters:
            result = [r for r in result if r.price > int(filters["price__gt"])]

        return result
