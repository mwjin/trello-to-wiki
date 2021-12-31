class CardList:
    def __init__(self, data) -> None:
        self._id = data.get("id")
        self._name = data.get("name")
        assert self._id is not None
        assert self._name is not None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
