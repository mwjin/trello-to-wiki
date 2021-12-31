class TrelloClient:
    def __init__(self, auth_key, auth_token) -> None:
        self._key = auth_key
        self._token = auth_token
        self._trello_api_url = "https://api.trello.com/1"
