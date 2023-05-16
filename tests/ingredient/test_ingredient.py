from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


def test_ingredient():
    egg = Ingredient("ovo")
    assert egg.name == "ovo"
    assert egg.restrictions == {Restriction.ANIMAL_DERIVED}
    assert repr(egg) == "Ingredient('ovo')"

    second_egg = Ingredient("ovo")
    assert egg.__hash__() == second_egg.__hash__()
    assert egg == second_egg

    chicken = Ingredient("frango")
    assert egg.__hash__() != chicken.__hash__()
    assert egg != chicken
