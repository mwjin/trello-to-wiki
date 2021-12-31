import requests


class TrelloClient:
    def __init__(self, auth: dict) -> None:
        self._key = auth.get("key")
        self._token = auth.get("token")
        self._trello_api_url = "https://api.trello.com/1"

    @property
    def auth_query_string(self):
        return f"?key={self._key}&token={self._token}"

    def get_cardlists(self, board_id: str) -> list:
        api_url = f"{self._trello_api_url}/boards/{board_id}/lists"
        response = requests.get(f"{api_url}{self.auth_query_string}")
        return response.json()
