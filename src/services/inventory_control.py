from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Dict:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    def __is_available(self, ingredient: Ingredient, quantity: int) -> bool:
        return (
            ingredient in self.inventory
            and self.inventory[ingredient] >= quantity
        )

    def check_recipe_availability(self, recipe: Recipe) -> bool:
        for ingredient, quantity in recipe.items():
            if not self.__is_available(ingredient, quantity):
                return False
        return True

    def __consume_ingredient(
        self, ingredient: Ingredient, quantity: int
    ) -> None:
        if not self.__is_available(ingredient, quantity):
            raise ValueError
        self.inventory[ingredient] -= quantity

    def consume_recipe(self, recipe: Recipe) -> None:
        for ingredient, quantity in recipe.items():
            self.__consume_ingredient(ingredient, quantity)
