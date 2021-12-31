import requests

from card import Card
from card_list import CardList


class TrelloClient:
    def __init__(self, auth: dict) -> None:
        self._key = auth.get("key")
        self._token = auth.get("token")
        self._trello_api_url = "https://api.trello.com/1"

    @property
    def auth_query_string(self):
        return f"?key={self._key}&token={self._token}"

    def get_response_data(self, api_url) -> dict:
        response = requests.get(f"{api_url}{self.auth_query_string}")
        return response.json()

    def get_card_lists(self, board_id: str) -> list[CardList]:
        api_url = f"{self._trello_api_url}/boards/{board_id}/lists"
        return [CardList(data) for data in self.get_response_data(api_url)]

    def get_cards(self, card_list_id: str) -> list:
        api_url = f"{self._trello_api_url}/lists/{card_list_id}/cards"
        return [
            Card(card_data) for card_data in self.get_response_data(api_url)
        ]

    def get_member_name(self, member_id: str) -> str:
        api_url = f"{self._trello_api_url}/members/{member_id}"
        return self.get_response_data(api_url).get("fullName")
