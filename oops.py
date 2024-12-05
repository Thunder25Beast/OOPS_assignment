class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.__price = price  # Private attribute for encapsulation

    def apply_discount(self, discount):
        """Apply a discount percentage to the car price."""
        self.__price -= self.__price * (discount / 100)

    def get_price(self):
        """Getter for price."""
        return self.__price

    def set_price(self, new_price):
        """Setter for price with validation."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

    def get_info(self):
        """Display car's information."""
        return f"Make: {self.make}, Model: {self.model}, Price: ${self.__price:.2f}"


class ElectricCar(Car):
    def __init__(self, make, model, price, battery_range):
        super().__init__(make, model, price)
        self.battery_range = battery_range

    def get_info(self):
        """Override to include battery range."""
        return super().get_info() + f", Battery Range: {self.battery_range} miles"


class SportsCar(Car):
    def __init__(self, make, model, price, top_speed):
        super().__init__(make, model, price)
        self.top_speed = top_speed

    def get_info(self):
        """Override to include top speed."""
        return super().get_info() + f", Top Speed: {self.top_speed} mph"


# Main program to demonstrate all tasks
if __name__ == "__main__":
    # Task 1: Basic Class Creation
    car = Car("Toyota", "Corolla", 20000)
    print(car.get_info())
    car.apply_discount(10)
    print(car.get_info())

    # Task 2: Encapsulation
    car.set_price(18000)
    print(car.get_info())
    print("Current Price:", car.get_price())

    # Task 3: Inheritance
    electric_car = ElectricCar("Tesla", "Model S", 80000, 400)
    sports_car = SportsCar("Porsche", "911", 150000, 200)

    print(electric_car.get_info())
    print(sports_car.get_info())

    # Task 4: Polymorphism
    cars = [
        car,
        electric_car,
        sports_car,
        Car("Honda", "Civic", 22000),
        ElectricCar("Nissan", "Leaf", 30000, 150),
    ]

    for c in cars:
        print(c.get_info())

