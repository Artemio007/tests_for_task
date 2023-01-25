from typing import List


class Train:
    def __init__(self, capacity: float, cars: List[object]) -> None:
        self.capacity = capacity
        self.cars = cars

    def is_transportable(self):
        return self.capacity > self.__get_cars_total_weight()

    def __get_cars_total_weight(self):
        total_weight = 0
        for car in self.cars:
            total_weight += car.total_weight
        return total_weight

    def sort_cars(self):
        return self.cars.sort(key=lambda x: x.total_weight, reverse=True)
