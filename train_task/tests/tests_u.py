import unittest
from unittest import skipIf
from unittest.mock import Mock, patch
from cargo.base_car import *
from cargo.cistern import Cistern
from cargo.container import Container
from cargo.platform import Platform
from materials.material import Material


class TrainTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Tests for task 'Train'")

    def setUp(self) -> None:
        self.base_car_test = BaseCar.to_tons(7856)
        self.test_materials = Material("water")
        self.cistern_class_test = Cistern(100.9, 133.5, self.test_materials)
        self.container_class_test = Container(100.9, 133.5, 564, self.test_materials)

    def test_base_car_methods(self):
        self.assertIsInstance(self.base_car_test, float)
        self.assertEqual(self.base_car_test, 7.9)
        self.num = 1

    def test_cistern_methods(self):
        self.assertIsInstance(self.cistern_class_test.calculate_total_weight(), float)
        self.assertEqual(self.cistern_class_test.calculate_total_weight(), 42211.8)
        self.num = 2

    def test_container_methods(self):
        self.assertEqual(self.container_class_test.calculate_total_weight(), 7574382.1)
        self.assertIsInstance(self.container_class_test.calculate_total_weight(), float)
        with self.assertRaises(TypeError):
            Container("100", 133.5, 564, self.test_materials)
        self.num = 3

    @patch('cargo.container.Container', return_value=1348800)
    def test_container_methods_privat(self, calculate_cargo_volume):
        self.assertEqual(calculate_cargo_volume(120, 562, 20, "water"), 1348800)
        self.num = 4

    @skipIf(Platform, "no reason")
    def test_skip_platform(self):
        platform_obj = Platform(120)
        platform_obj.calculate_total_weight = Mock(return_value=56)
        platform_obj.calculate_total_weight(562, 230)
        platform_obj.calculate_total_weight.assert_called_with(562, 230)
        cl = Platform(120)
        self.assertEqual(cl.calculate_total_weight(), 120)
        self.num = 5

    def tearDown(self) -> None:
        print(f"test {self.num} is over")
