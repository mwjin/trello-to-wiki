class TrelloClient:
    def __init__(self, auth: dict) -> None:
        self._key = auth.get("key")
        self._token = auth.get("token")
        self._trello_api_url = "https://api.trello.com/1"
