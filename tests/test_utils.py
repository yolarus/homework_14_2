from unittest.mock import mock_open, patch

from src.utils import read_json


def test_read_json() -> None:
    data = """[{"name": "Категория 1",
             "description": "Это категория 1",
             "products": [{"name": "Продукт 1", "description": "Первый", "price": 10, "quantity": 5},
                          {"name": "Продукт 2", "description": "Второй", "price": 20, "quantity": 10},
                          {"name": "Продукт 3", "description": "Третий", "price": 30, "quantity": 15}]}]"""

    with patch("builtins.open", mock_open(read_data=data)) as mock_file:
        result = read_json("test.json")
        names = ["Продукт 1", "Продукт 2", "Продукт 3",]
        for cat in result:
            for i, prod in enumerate(cat.products_list):
                assert prod.name == names[i]

        mock_file.assert_called_once_with("test.json", "r")
