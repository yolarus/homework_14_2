class Product:
    """
    Класс продуктов интер-нет магазина
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """
        Конструктор объектов
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
