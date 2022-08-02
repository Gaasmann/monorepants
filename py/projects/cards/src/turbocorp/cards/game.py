from turbocorp.cards.core.deck import Deck


def just_draw_cards():
    print("Hello, we'll just draw cards.")
    deck = Deck()
    while not deck.empty:
        input("Press enter for a new card.")
        card = deck.draw_card()
        print(f"The card: {card.rank} of {card.suit} ({card.color}).\n")
    print("End of deck. Goodbye!")
