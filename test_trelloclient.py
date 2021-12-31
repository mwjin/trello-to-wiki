import pytest
import yaml

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
def card_list(card_lists):
    return card_lists[0]


@pytest.fixture(scope="module")
def empty_card_list(card_lists):
    return card_lists[1]


@pytest.fixture(scope="module")
def cards(trello_client, card_list):
    return trello_client.get_cards(card_list.id)


@pytest.fixture(scope="module")
def card(cards):
    return cards[0]


@pytest.fixture(scope="module")
def empty_card(cards):
    return cards[1]


def test_get_card_lists(card_lists):
    assert len(card_lists) == 2


def test_get_cards(cards):
    assert len(cards) == 2


def test_get_cards_from_empty_card_list(trello_client, empty_card_list):
    assert trello_client.get_cards(empty_card_list.id) == []


def test_card_content(card):
    assert card.name == "Card"
    assert len(card.member_ids) == 1
    assert card.desc == "This is a card for testing"
    assert "Test" in card.labels


def test_empty_card(empty_card):
    assert empty_card.name == "Empty Card"
    assert empty_card.member_ids == []
    assert empty_card.desc == ""
    assert empty_card.labels == set()


def test_get_member_name(trello_client, card):
    assert trello_client.get_member_name(card.member_ids[0]) == "Minwoo Jeong"
