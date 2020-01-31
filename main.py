from my_package import fooFunc
from my_package import Car, ElectricCar

fooFunc()

ford = Car("Hummer", "85")
ford.run_car()

prius = ElectricCar("EHummer", "110", "monster-hybrid")
prius.run_car()
prius.display_electric_type()


