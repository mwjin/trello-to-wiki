import pytest
import yaml

from card import Card
from card_list import CardList
from trelloclient import TrelloClient


@pytest.fixture(scope="module")
def auth_yml_path():
    return "auth.yml"


@pytest.fixture(scope="module")
def board_id():
    return "iREzMfkb"  # Board for testing


@pytest.fixture(scope="module")
def auth(auth_yml_path):
    with open(auth_yml_path) as auth_file:
        auth = yaml.safe_load(auth_file)
    return auth


@pytest.fixture(scope="module")
def trello_client(auth):
    return TrelloClient(auth)


@pytest.fixture(scope="module")
def card_lists(trello_client, board_id):
    return trello_client.get_card_lists(board_id)


@pytest.fixture(scope="module")
def cards(trello_client, card_lists):
    return trello_client.get_cards(card_lists[0].id)


def test_get_card_lists(card_lists):
    assert len(card_lists) == 2
    assert card_lists[0].name == "List"
    assert card_lists[1].name == "Empty List"


def test_get_cards(cards):
    assert len(cards) == 2
    assert cards[0].name == "Card"
    assert cards[1].name == "Empty Card"


def test_get_member_name(trello_client, cards):
    assert (
        trello_client.get_member_name(cards[0].member_ids[0]) == "Minwoo Jeong"
    )
