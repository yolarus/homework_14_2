from src.product import Product


def test_product_init(first_product: Product) -> None:
    assert first_product.name == "Iphone 15"
    assert first_product.description == "Apple Iphone 15"
    assert first_product.price == 1500
    assert first_product.quantity == 10


def test_product_new_product_duplication(first_product, new_prod_dupl) -> None:
    second_prod = Product.new_product(new_prod_dupl)
    assert second_prod.price == 1500
    assert second_prod.quantity == 35


def test_product_new_product(first_product, new_prod) -> None:
    second_prod = Product.new_product(new_prod)
    assert second_prod.price == 800
    assert second_prod.quantity == 10
