import dataclasses
from itertools import product
from typing import Literal
from typing import get_args

Suits = Literal["clubs", "diamonds", "hearts", "spades"]
Ranks = Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
Colors = Literal["red", "black"]


@dataclasses.dataclass(frozen=True)
class Card:
    suit: Suits
    rank: Ranks

    @property
    def color(self) -> Colors:
        return "red" if self.suit in ["diamonds", "hearts"] else "black"


class Deck:
    """This is a deck of cards"""

    def __init__(self):
        self.remaining_cards: set[Card] = {Card(suit, rank) for suit, rank in product(get_args(Suits), get_args(Ranks))}

    def draw_card(self) -> Card:
        return self.remaining_cards.pop()  # not sure arbitrary == random

    @property
    def size(self) -> int:
        return len(self.remaining_cards)

    @property
    def empty(self) -> bool:
        return not bool(self.remaining_cards)
