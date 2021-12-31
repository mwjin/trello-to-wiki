class Card:
    def __init__(self, data) -> None:
        self._id = data.get("id")
        self._name = data.get("name")
        self._labels = {
            label_data.get("name") for label_data in data.get("labels")
        }
        self._member_ids = data.get("idMembers")
        self._list_id = data.get("id_list")
        self._desc = data.get("desc")
        self._list_name = ""
        self._member_names = []

    @property
    def name(self):
        return self._name

    @property
    def labels(self):
        return set(self._labels)

    @property
    def member_ids(self):
        return list(self._member_ids)

    @property
    def list_id(self):
        return self._list_id

    @property
    def desc(self):
        return self._desc

    @property
    def list_name(self):
        return self._list_name

    @list_name.setter
    def list_name(self, value):
        self._list_name = value

    @property
    def member_names(self):
        return list(self._member_names)

    def add_member_name(self, name):
        self._member_names.append(name)

