from turbocorp.cards.core.deck import Card


def test_draw_until_empty(deck):
    cards: set[Card] = set()
    while not deck.empty:
        card = deck.draw_card()
        assert card not in cards, "Card already drawn!"
        cards.add(card)
    assert len(cards) == 52, "The deck should have 52 cards!"
