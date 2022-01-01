import yaml

from trelloclient import TrelloClient
from collections import defaultdict


def main():
    with open("auth.yml") as infile:
        auth = yaml.safe_load(infile)
    client = TrelloClient(auth)
    board_id = "21H6HzC7"
    card_lists = client.get_card_lists(board_id)
    
    card_map = defaultdict(list)
    for card_list in card_lists:
        cards = client.get_cards(card_list.id)
        for card in cards:
            card.list_name = card_list.name
            for member_id in card.member_ids:
                card.add_member_name(client.get_member_name(member_id))
            card_map[card.category].append(card)

    for category in card_map:
        print(f"=={category}==")
        for card in sorted(card_map[category], key=lambda x: x.name):
            print(card.wiki)


if __name__ == "__main__":
    main()
