import pytest
import yaml

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
    assert len(trello_client.get_cardlists(board_id)) > 0
