from abc import ABC



class BaseCar(ABC):
    def __init__(self):
        self.self_weight = 0

    def calculate_cargo_volume(self):
        pass

    def calculate_total_weight(self):
        pass

    @staticmethod
    def to_tons(weight_in_kg: float):
        return round(weight_in_kg / 1000, 1)







