class Product:
    """
    Класс продуктов интернет магазина
    """
    name: str
    description: str
    __price: float
    quantity: int
    products_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Конструктор объектов
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_list.append(self)

    @classmethod
    def new_product(cls, product: dict):
        """
        Формирует новый продукт из словаря, если продукт уже существует, то возвращает старый продукт с
        наибольшей ценой и суммированным количеством
        """
        for prod in cls.products_list:
            if prod.name == product["name"] and prod.description == product["description"]:
                prod.price = max(prod.price, product["price"])
                prod.quantity += product["quantity"]
                return prod
            else:
                new_prod = cls(product["name"], product["description"], product["price"], product["quantity"])
                return new_prod

    @property
    def price(self) -> float:
        """
        Геттер атрибута __price - возврщает цену продукта
        """
        return self.__price

    @price.setter
    def price(self, new_price) -> None:
        """
        Сеттер атрибута __price - обновляет цену продукта, если новая цена ниже старой запрашивается подтверждение
        """
        if new_price > 0:
            if new_price < self.__price:
                if input("Вы уверенны, что хотите снизить цене? Введите 'y' - если да, 'n' - если нет: ") == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")
