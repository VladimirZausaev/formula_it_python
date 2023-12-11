import doctest

class Transport:
    def init(self, name: str, max_speed: float):
        """
        Создает новый экземпляр транспортного средства.

        :param name: название транспортного средства
        :param max_speed: максимальная скорость транспортного средства
        """
        self.name = name
        self.max_speed = max_speed

    def move(self, distance: float) -> float:
        """
        Двигает транспортное средство на заданное расстояние.

        :param distance: расстояние, которое необходимо пройти
        :return: время, за которое транспортное средство пройдет заданное расстояние
        """
        ...

    def stop(self):
        """
        Останавливает транспортное средство.
        """
        ...


class Fruit:
    def init(self, name: str, color: str):
        """
        Создает новый экземпляр фрукта.

        :param name: название фрукта
        :param color: цвет фрукта
        """
        self.name = name
        self.color = color

    def eat(self):
        """
        Ест фрукт.
        """
        ...

    def peel(self):
        """
        Чистит фрукт.
        """
        ...

class OnlineStore:
    def init(self, name: str, website: str):
        """
        Создает новый экземпляр интернет-магазина.

        :param name: название интернет-магазина
        :param website: адрес сайта интернет-магазина
        """
        self.name = name
        self.website = website

    def search(self, query: str) -> list:
        """
        Ищет товары в интернет-магазине по заданному запросу.

        :param query: запрос для поиска товаров
        :return: список найденных товаров
        """
        ...

    def buy(self, product_id: int, quantity: int):
        """
        Покупает товар в интернет-магазине.

        :param product_id: идентификатор товара
        :param quantity: количество товара для покупки
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации