import pytest
import yaml

from cardlist import CardList
from trelloclient import TrelloClient


@pytest.fixture(scope="module")
def auth_yml_path():
    return "auth.yml"


@pytest.fixture(scope="module")
def board_id():
    return "21H6HzC7"


@pytest.fixture(scope="module")
def auth(auth_yml_path):
    with open(auth_yml_path) as auth_file:
        auth = yaml.safe_load(auth_file)
    return auth


@pytest.fixture(scope="module")
def trello_client(auth):
    return TrelloClient(auth)


def test_get_cardlists(trello_client, board_id):
    card_lists = trello_client.get_cardlists(board_id)
    assert len(card_lists) > 0
    assert isinstance(card_lists[0], CardList)
