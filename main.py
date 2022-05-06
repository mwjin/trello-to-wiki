from email.policy import default
import sys
from collections import defaultdict
from datetime import datetime

import yaml

from trello_to_wiki.trelloclient import TrelloClient


class TrelloToWiki:
    def __init__(self):
        with open("auth.yml") as infile:
            auth = yaml.safe_load(infile)
        self.client = TrelloClient(auth)
        self.board_id = "21H6HzC7"
        self._card_map = None

    @property
    def card_lists(self) -> list:
        print_log("Collect the card lists from the Trello board.")
        return self.client.get_card_lists(self.board_id)

    @property
    def card_map(self) -> dict:
        if self._card_map:
            return self._card_map

        result = {}
        for card_list in self.card_lists:
            print_log(f"Collect the cards from the list '{card_list.name}'.")
            cards = self.client.get_cards(card_list.id)
            for card in cards:
                for member_id in card.member_ids:
                    card.add_member_name(self.client.get_member_name(member_id))
                if card.category not in result:
                    result[card.category] = defaultdict(list)
                result[card.category][card_list.name].append(card)

        self._card_map = result
        return result

    def create_wiki(self, wiki_filename: str):
        print_log(f"Create the wiki file '{wiki_filename}'.")
        del self.card_map["None"]
        with open(wiki_filename, "w") as outfile:
            for category in self.card_map:
                print(f"=={category}==", file=outfile)
                for card_list in self.card_map[category]:
                    print(f"==={card_list}===", file=outfile)
                    for card in sorted(
                        self.card_map[category][card_list], key=lambda x: x.name
                    ):
                        print(card.wiki, file=outfile)


def print_log(msg: str):
    current_time = datetime.now().strftime("%H:%M:%S %m/%d/%y")
    print(f"[{current_time}] {msg}", file=sys.stderr)


def create_wiki_filename():
    current_date = datetime.now().strftime("%Y%m%d")
    return f"wiki/{current_date}.txt"


if __name__ == "__main__":
    TrelloToWiki().create_wiki(create_wiki_filename())
