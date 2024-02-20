from typing import List

class Vehicle:
    """
    Базовый класс, представляющий общий вид транспортного средства.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация нового экземпляра транспортного средства.

        Параметры:
        - brand (str): Марка транспортного средства.
        - model (str): Модель транспортного средства.
        - year (int): Год производства транспортного средства.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        """
        Запуск двигателя транспортного средства.
        """
        pass

    def stop_engine(self):
        """
        Остановка двигателя транспортного средства.
        """
        pass

    def __str__(self) -> str:
        return f"{self.year} {self.brand} {self.model}"

    def __repr__(self) -> str:
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year})"


class Car(Vehicle):
    """
    Подкласс, представляющий автомобиль и наследующий от базового класса Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, num_doors: int):
        """
        Инициализация нового экземпляра автомобиля.

        Параметры:
        - brand (str): Марка автомобиля.
        - model (str): Модель автомобиля.
        - year (int): Год производства автомобиля.
        - num_doors (int): Количество дверей у автомобиля.
        """
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def open_trunk(self):
        """
        Открытие багажника автомобиля.
        """
        pass

    def start_engine(self):
        """
        Запуск двигателя автомобиля, с дополнительными шагами, специфичными для автомобилей.
        """
        # Дополнительные шаги, специфичные для автомобилей
        super().start_engine()
        pass

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.num_doors}-дверный"

    def __repr__(self) -> str:
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, num_doors={self.num_doors})"


if __name__ == "__main__":
    # Пример использования
    vehicle1 = Vehicle("Toyota", "Camry", 2022)
    print(vehicle1)

    car1 = Car("Honda", "Civic", 2023, 4)
    print(car1)
