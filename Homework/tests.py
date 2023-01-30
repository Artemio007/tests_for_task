import sys
import unittest
from unittest import skipIf
from unittest.mock import Mock, patch
import pytest
from less13 import *


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
    @patch('lesson28.Homework.less13.FlyingBird', "The duck can fly")
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





