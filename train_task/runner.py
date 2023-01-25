from materials.material import Material
from train.train import Train
from materials import material
from cargo.container import Container
from cargo.platform import Platform
from cargo.cistern import Cistern


def main():
    steel = Material("steel")
    diesel = Material("diesel")

    platform = Platform(50)
    container = Container(12, 2.5, 2.5, steel)
    cistern = Cistern(12.5, 2.5, diesel)

    train = Train(150, [platform, container, cistern])
    train.sort_cars()
    print(train.is_transportable())


if __name__ == "__main__":
    main()
