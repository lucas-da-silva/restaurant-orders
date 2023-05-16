import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


def test_dish():
    egg = Ingredient("ovo")
    egg_quantity = 10
    pizza = "Pizza"
    pizza_price = 39.20
    hamburger = "Hamburger"
    hamburger_price = 20.20

    pizza_dish = Dish(pizza, pizza_price)
    assert pizza_dish.name == pizza
    assert repr(pizza_dish) == f"Dish('{pizza}', R${pizza_price:.2f})"

    pizza_dish.add_ingredient_dependency(egg, egg_quantity)
    assert pizza_dish.recipe.get(egg) == egg_quantity
    assert pizza_dish.get_ingredients() == {egg}

    assert pizza_dish.get_restrictions() == egg.restrictions

    pizza_second_dish = Dish(pizza, pizza_price)
    assert pizza_dish.__hash__() == pizza_second_dish.__hash__()
    assert pizza_dish == pizza_second_dish

    hamburger_dish = Dish(hamburger, hamburger_price)
    assert pizza_dish.__hash__() != hamburger_dish.__hash__()
    assert pizza_dish != hamburger_dish

    with pytest.raises(TypeError):
        assert Dish(pizza, "")
    with pytest.raises(ValueError):
        assert Dish(pizza, 0)
