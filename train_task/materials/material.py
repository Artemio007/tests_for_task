class Material:
    def __init__(self, name: str) -> None:
        self.__materials_density_map = {
            "steel": 7800.0,
            "copper": 8933.0,
            "water": 997,
            "diesel": 820
        }
        self._name = name
        self._volume = 1

    def __get_density(self):
        return self.__materials_density_map.get(self._name, 0)

    def get_mass(self):
        return self._volume * self.__get_density()

    def __str__(self):
        return f"{self.get_mass()} kg"





