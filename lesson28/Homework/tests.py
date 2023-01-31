import sys
import unittest
from unittest import skipIf
from unittest.mock import patch
import pytest
from less16 import *
from less17 import History, history
from less18 import *


class Test16Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("tests for task 3 from lesson 16")

    def setUp(self) -> None:
        self.bird = Bird("kivi")
        self.flying_bird_0 = FlyingBird("duck")
        self.flying_bird_1 = FlyingBird("duck", 1)
        self.non_flying_bird = NonFlyingBird("chicken")
        self.super_bird = SuperBird("woodpecker", 1)

    @skipIf(sys.version_info < (3, 10), reason="you need python 3.10 or higher")
    def test_bird(self):
        self.assertIsInstance(self.flying_bird_0, Bird)
        self.assertIsInstance(self.non_flying_bird, Bird)
        self.assertIsInstance(self.super_bird, Bird)
        self.assertEqual(self.bird.name, "kivi")
        self.assertEqual(self.bird.fly(), f"The {self.bird.name} can fly")
        self.assertEqual(self.bird.walk(), f"the {self.bird.name} can walk")

    @skipIf(sys.version_info < (3, 10), reason="you need python 3.10 or higher")
    @patch('lesson28.Homework.less16.FlyingBird', "The duck can fly")
    def test_flying_bird_fly(self):
        self.assertEqual(self.flying_bird_0.fly(), "The duck can fly")

    @skipIf(sys.platform == "linux", reason="im wanna work on windows")
    def test_flying_bird_other(self):
        self.assertEqual(self.flying_bird_0.walk(), "the duck can walk")
        self.assertNotIsInstance(self.flying_bird_0.eats(), Bird)
        self.assertIsInstance(self.flying_bird_0.ration, dict)
        self.assertIsInstance(self.flying_bird_0.ration.get(1), str)
        with self.assertRaises(TypeError):
            self.flying_bird_0.walk("gx")
            self.flying_bird_0.walk(1)

    @pytest.mark.xfail
    def test_non_flying_bird(self):
        self.assertEqual(self.non_flying_bird.fly(), f"the {self.non_flying_bird.name} can't fly")
        self.assertEqual(self.non_flying_bird.walk(), f"the {self.non_flying_bird.name} c2n walk")

    def test_super_bird(self):
        self.assertEqual(self.super_bird.fly(), f"the {self.super_bird.name} can fly")
        self.assertEqual(self.super_bird.walk(), f"the {self.super_bird.name} can walk")
        self.assertEqual(self.super_bird.swim(), f"the {self.super_bird.name} can swim")
        self.assertEqual(self.super_bird.eats(), f"the {self.super_bird.name} like {self.super_bird.eat}")
        with self.assertRaises(TypeError):
            self.super_bird.fly(51)


class Test17Less(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("tests for task 3 from lesson 17")

    def setUp(self) -> None:
        self.atr_0 = History({"hi0": 0})
        self.atr_0.set_value("hi1", 1)
        self.atr_0.set_value("hi2", 2)
        self.atr_0.set_value("hi3", 3)
        self.atr_0.set_value("hi4", 4)
        self.atr_0.set_value("hi5", 5)
        self.atr_0.set_value("hi6", 6)
        self.atr_0.set_value("hi7", 7)
        self.atr_0.set_value("hi8", 8)
        self.atr_0.set_value("hi9", 9)
        self.atr_0.set_value("hi10", 10)
        self.atr_0.set_value("hi11", 12)
        self.atr_0.set_value("hi12", 13)
        self.atr_0.set_value("hi13", 14)

    @skipIf(sys.platform == "linux", reason="you need windows")
    def test_history(self):
        self.assertEqual(len(history), 10)
        self.assertIsInstance(self.atr_0.element, dict)
        self.assertIsInstance(history, list)
        with self.assertRaises(TypeError):
            self.atr_0.set_value("dfj")
        with self.assertRaises(NameError):
            self.atr_0.set_value(hi)

    @skipIf(sys.version_info < (3, 10), reason="you need python 3.10 or higher")
    def test_get_value(self):
        self.assertIsInstance(self.atr_0.get_value(), list)
        with self.assertRaises(TypeError):
            self.atr_0.get_value("hello")


class Test18Less(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("tests for task 4 for less 18")

    def setUp(self) -> None:
        self.material_ex = Material("steel", 7850.3)
        self.subject_ex = Subject("wire", "steel", 7800.3)

    def test_get_material(self):
        self.assertIsInstance(self.material_ex.get_material(), str)
        self.assertEqual(self.material_ex.get_material(), "steel;7850.3")
        with self.assertRaises(TypeError):
            self.material_ex.get_material(4556)

    @skipIf(sys.version_info < (3, 10), reason="you need python 3.10 or higher")
    def test_get_subject(self):
        self.assertEqual(self.subject_ex.get_subject(), "wire;steel;7850.0;7800.3;61232355.0")
        self.assertIsInstance(self.subject_ex.get_subject(), str)

    @pytest.mark.xfail
    @patch("lesson28.Homework.less18.Subject", 61232355.0)
    def test_get_mass(self):
        self.assertEqual(self.subject_ex.for_mass, 61232355.0)

    @patch("lesson28.Homework.less18.Runner", "steel wire mass is 61232355.0 kg")
    def test_runner(self):
        assert Runner(self.subject_ex).get_subject() == "steel wire mass is 61232355.0 kg"





