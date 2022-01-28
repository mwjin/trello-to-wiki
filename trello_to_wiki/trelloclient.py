import requests

from trello_to_wiki.card import Card
from trello_to_wiki.card_list import CardList


class TrelloClient:
    def __init__(self, auth: dict) -> None:
        self._key = auth.get("key")
        self._token = auth.get("token")
        self._trello_api_url = "https://api.trello.com/1"
        self._member_name_cache = {}

    @property
    def auth_query_string(self) -> str:
        return f"?key={self._key}&token={self._token}"

    def get_response_data(self, api_url) -> dict:
        response = requests.get(f"{api_url}{self.auth_query_string}")
        return response.json()

    def get_card_lists(self, board_id: str) -> list[CardList]:
        api_url = f"{self._trello_api_url}/boards/{board_id}/lists"
        return [
            CardList(list_data) for list_data in self.get_response_data(api_url)
        ]

    def get_cards(self, card_list_id: str) -> list[Card]:
        api_url = f"{self._trello_api_url}/lists/{card_list_id}/cards"
        return [
            Card(card_data) for card_data in self.get_response_data(api_url)
        ]

    def get_member_name(self, member_id: str) -> str:
        if member_id not in self._member_name_cache:
            self._member_name_cache[member_id] = self.get_response_data(
                f"{self._trello_api_url}/members/{member_id}"
            ).get("fullName")

        return self._member_name_cache[member_id]
