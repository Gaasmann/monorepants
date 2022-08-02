import pytest

from turbocorp.cards.core.deck import Deck


@pytest.fixture
def deck() -> Deck:
    return Deck()
