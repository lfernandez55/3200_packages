class Car():
    def __init__(self, car_model, car_speed):
        self.car_model = car_model
        self.car_speed = car_speed

    def run_car(self):
        print("This " + self.car_model + " is going " + str(self.car_speed) + " miles per hour. Watch out!" )


class ElectricCar(Car):
    def __init__(self, car_make, car_speed, electric_type ):
        super().__init__(car_make, car_speed)
        self.electric_type = electric_type

    def display_electric_type(self):
        print("This electric vehicle is a " + self.electric_type)

if __name__ == '__main__':
    ford = Car("Ford 150", "95")
    ford.run_car()

    prius = ElectricCar("Prius", "80", "hybrid")
    prius.run_car()
    prius.display_electric_type()

