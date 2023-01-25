from materials.material import Material
from cargo.base_car import BaseCar


class Container(BaseCar):
    def __init__(self, length: float, height: float, width: float, material: Material) -> None:
        super().__init__()
        self.__self_weight = 9000
        self.__length = length
        self.__height = height
        self.__width = width
        self.__material = material
        self.__total_weight = self.calculate_total_weight()

    @property
    def total_weight(self):
        return self.__total_weight

    def __calculate_cargo_volume(self) -> float:
        return self.__height * self.__width * self.__length

    def calculate_total_weight(self):
        """
        Function calculate total weight of the train car including container. It is assumed that material mass
        was calculated for 1 m3
        :return: total_weight in tons
        """
        return self.to_tons(self.__calculate_cargo_volume() * self.__material.get_mass() + self.__self_weight)

    def __str__(self):
        return f"{self.__calculate_cargo_volume()} m3"

#