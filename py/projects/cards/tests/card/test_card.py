import pytest

from turbocorp.cards.core.deck import Card

scenarios = [
    ("spades", "4", "black"),
    ("clubs", "8", "black"),
    ("diamonds", "king", "red"),
    ("hearts", "2", "red"),
]


@pytest.mark.parametrize(("suit", "rank", "expected_color"), scenarios)
def test_color(suit, rank, expected_color):
    card = Card(suit, rank)
    assert card.color == expected_color
