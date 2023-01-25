from math import pi
from materials.material import Material
from cargo.base_car import BaseCar


class Cistern(BaseCar):
    def __init__(self, length: float, diameter: float, material: Material) -> None:
        """
        Only liquids allowed e.g. water
        :param length:
        :param diameter:
        :param material:
        """
        super().__init__()
        self.__self_weight = 21000
        self.__length = length
        self.__diameter = diameter
        self.__material = material
        self.__total_weight = self.calculate_total_weight()

    @property
    def total_weight(self):
        return self.__total_weight

    def __calculate_cargo_volume(self):
        """
        Calculate volume of cistern
        :return: volume of cistern in m3
        """
        return pi * self.__diameter * self.__length

    def calculate_total_weight(self) -> float:
        return self.to_tons(self.__calculate_cargo_volume() * self.__material.get_mass() + self.__self_weight)

#
# water = Material("water")
# cist = Cistern(12.0, 2.5, material=water)
#
# print(cist.calculate_total_weight())
