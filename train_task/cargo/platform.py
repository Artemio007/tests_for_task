from cargo.base_car import BaseCar


class Platform(BaseCar):
    def __init__(self, cargo_weight: float) -> None:
        super().__init__()
        self.__cargo_weight = cargo_weight
        self.__total_weight = self.calculate_total_weight()

    @property
    def total_weight(self):
        return self.__total_weight

    def calculate_total_weight(self):
        return self.__cargo_weight + self.self_weight

