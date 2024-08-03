import json

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[Category]:
    """
    Считывание данных из json-файла по переданному пути и конвертация их в экземпляры классов
    """
    with open(path, "r") as file:
        data = json.load(file)

    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
