import unittest
from io import StringIO
from unittest.mock import patch

class Car:
    def __init__(self, number, brand, type, capacity):
        self.set_number(number)
        self.set_brand(brand)
        self.set_type(type)
        self.set_capacity(capacity)


    def set_number(self, number):
        if number is None or number == '':
            raise ValueError("Number should not be empty") 

        if isinstance(number, str) == False:
            raise ValueError("Number should be string") 

        if len(number) < 6 or len(number) > 20:
            raise ValueError("Number length should be between 6 and 20")

        self.number = number

    def get_number(self):
        return self.number

    def set_brand(self, brand):
        if brand is None or brand == '':
            raise ValueError("Brand should not be empty") 

        if isinstance(brand, str) == False:
            raise ValueError("Brand should be string") 

        if len(brand) < 3 or len(brand) > 20:
            raise ValueError("Brand length should be between 3 and 20")

        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_type(self, type):
        if type is None or type == '':
            raise ValueError("Type should not be empty") 

        if isinstance(type, str) == False:
            raise ValueError("Type should be string") 

        if len(type) < 3 or len(type) > 20:
            raise ValueError("Type length should be between 3 and 20")

        self.type = type

    def get_type(self):
        return self.type

    def set_capacity(self, capacity):
        if capacity is None:
            raise ValueError("Capacity should not be empty") 

        if isinstance(capacity, int) == False:
            raise ValueError("Capacity should be integer") 

        if capacity < 1 or capacity > 20:
            raise ValueError("Capacity should be between 1 and 20")

        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def __str__(self):
        return f"Number: {self.number}, Brand: {self.brand}, Type: {self.type}, Capacity: {self.capacity}"

    
        
class CarRental:
    def __init__(self):
        self.cars = []

    def get_cars(self):
        return self.cars

    def add_car(self, car):
        self.cars.append(car)

    def get_cars_by_capacity(self, capacity):
        if self.cars == None or isinstance(self.cars, list) == False:
            raise ValueError("Member variable cars should be initialized and it's type should be list") 
        if capacity is None:
            raise ValueError("Capacity should not be empty") 

        if isinstance(capacity, int) == False:
            raise ValueError("Capacity should be integer") 

        if capacity < 0:
            raise ValueError("Capacity argument should be more than or equal to 0")

        return [c for c in self.cars if c.get_capacity() == capacity]

    def display_all(self):        
        if self.cars == None or isinstance(self.cars, list) == False:
            raise ValueError("Member variable cars should be initialized and it's type should be list") 
        
        if len(self.cars) < 1:
            print("There is no cars in inventory")
            return

        headers = ["Number", "Brand", "Type", "Capacity"]
        row_format = "{:>15}" * (len(headers) + 1)
        print(row_format.format("No", *headers))

        index = 0
        for c in self.cars:
            print(row_format.format(str(index + 1), *[c.get_number(), c.get_brand(), c.get_type(), c.get_capacity()]))
            index += 1 
            

# Write the driver to test your class.    
def main():
    car_rental = CarRental()

    car1 = Car('111111', 'Benz', 'Sedan', 4)
    car2 = Car('222222', 'Audi', 'SUV', 6)
    car3 = Car('333333', 'BMW', 'Truck', 7)
    # car4 = Car(444, 'BMW', 'Truck', 7)
    
    car_rental.add_car(car1)
    car_rental.add_car(car2)
    car_rental.add_car(car3)

    cars_by_capacity_6 = car_rental.get_cars_by_capacity(6)
    for c in cars_by_capacity_6:
        print(c)

    car_rental.display_all()


class TestCarClass(unittest.TestCase):
    def test_argument_valid(self):        
        with self.assertRaises(ValueError) as context:
            car = Car("", "BMW", "Truck", 10)

        with self.assertRaises(ValueError) as context:
            car = Car("AC123", "", "Truck", 10)

        with self.assertRaises(ValueError) as context:
            car = Car("AC123", "Benz", "", 10)

        with self.assertRaises(ValueError) as context:
            car = Car("AC123", "Benz", "Trunk", 0)

        with self.assertRaises(ValueError) as context:
            car = Car("AC123", "Benz", "Trunk", 100)

    def test_add_car(self):
        car_rental = CarRental()

        car1 = Car('111111', 'Benz', 'Sedan', 4)
        car2 = Car('222222', 'Audi', 'SUV', 6)
        car3 = Car('333333', 'BMW', 'Truck', 7)

        car_rental.add_car(car1)
        car_rental.add_car(car2)
        car_rental.add_car(car3)

        self.assertEqual(len(car_rental.cars), 3)

    def test_get_cars_by_capacity(self):
        car_rental = CarRental()

        car1 = Car('111111', 'Benz', 'Sedan', 4)
        car2 = Car('222222', 'Audi', 'SUV', 6)
        car3 = Car('333333', 'BMW', 'Truck', 7)
        car4 = Car('444444', 'Lexas', 'SUV', 6)


        car_rental.add_car(car1)
        car_rental.add_car(car2)
        car_rental.add_car(car3)
        car_rental.add_car(car4)

        cars_by_capacity_6 = car_rental.get_cars_by_capacity(6)
        self.assertEqual(len(cars_by_capacity_6), 2)

        cars_by_capacity_7 = car_rental.get_cars_by_capacity(7)
        self.assertEqual(len(cars_by_capacity_7), 1)

        with self.assertRaises(ValueError) as context:
            car_by_capacity_error = car_rental.get_cars_by_capacity(-1)

        
        cars_by_capacity_10 = car_rental.get_cars_by_capacity(10)
        self.assertEqual(len(cars_by_capacity_10), 0)

        with self.assertRaises(ValueError) as context:
            car_by_capacity_error = car_rental.get_cars_by_capacity(-2)
        
    def test_display_all(self):
        car_rental = CarRental()

        car1 = Car('111111', 'Benz', 'Sedan', 4)
        car2 = Car('222222', 'Audi', 'SUV', 6)
        car3 = Car('333333', 'BMW', 'Truck', 7)

        car_rental.add_car(car1)
        car_rental.add_car(car2)
        car_rental.add_car(car3)

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            car_rental.display_all()            
            self.assertEqual(fakeOutput.getvalue(), 
                '''             No         Number          Brand           Type       Capacity
              1         111111           Benz          Sedan              4
              2         222222           Audi            SUV              6
              3         333333            BMW          Truck              7
''')
        car_rental_empty = CarRental()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            car_rental_empty.display_all()            
            self.assertEqual(fakeOutput.getvalue(), 'There is no cars in inventory\n')


if __name__ == "__main__":
    main()
    unittest.main()