from trello_to_wiki.utils import replace_leading_spaces_with_asterisks


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
        if not self._desc:
            return ""

        return "\n".join(
            f"{replace_leading_spaces_with_asterisks(line)}"
            for line in filter(lambda x: x != "", self._desc.split("\n"))
        )

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

    @property
    def category(self):
        if "Issue" in self.labels:
            return "Issue"
        elif "Development" in self.labels:
            return "Development"
        elif "Other Tasks" in self.labels:
            return "Other Tasks"
        return "None"

    @property
    def wiki(self):
        if self.category == "Issue" or self.category == "Development":
            return (
                f"==={self.name}===\n"
                f"* 담당자: {', '.join(self.member_names)}\n"
                f"* 상태: {self.list_name}\n"
                f"{self.desc}"
            )
        elif self.category == "Other Tasks":
            return f"==={self.member_names[0]}===\n{self.desc}"
        return ""
