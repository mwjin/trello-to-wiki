import sys
from collections import defaultdict
from datetime import datetime

import yaml

from trelloclient import TrelloClient


def main():
    with open("auth.yml") as infile:
        auth = yaml.safe_load(infile)
    client = TrelloClient(auth)

    print_log("Collect the card lists from the Trello board.")
    board_id = "21H6HzC7"
    card_lists = client.get_card_lists(board_id)

    card_map = defaultdict(list)
    for card_list in card_lists:
        print_log(f"Collect the cards from the list '{card_list.name}'.")
        cards = client.get_cards(card_list.id)
        for card in cards:
            card.list_name = card_list.name
            for member_id in card.member_ids:
                card.add_member_name(client.get_member_name(member_id))
            card_map[card.category].append(card)

    print_log(f"Print the wiki.")
    print_wiki(card_map)


def print_log(msg: str):
    current_time = datetime.now().strftime("%H:%M:%S %m/%d/%y")
    print(f"[{current_time}] {msg}", file=sys.stderr)


def print_wiki(card_map: dict):
    del card_map["None"]
    for category in card_map:
        print(f"=={category}==")
        for card in sorted(card_map[category], key=lambda x: x.name):
            print(card.wiki)


if __name__ == "__main__":
    main()
