"""
Cars module
===============================================================================

Cars module demonstrates how to load data from the package directory.

"""
import os


def get_cars():
    """Get cars function.

    Usage:

    >>> from hello import get_cars
    >>> cars = get_cars()
    ['renault', 'mazda', 'toyota', 'subaru', 'mitsubishi', 'dodge', 'jeep', 'chevrolet', 'volkswagen', 'honda', 'mclaren', 'porsche', 'ferrari', 'lamborghini', 'mercedes-benz', 'audi', 'volvo', 'bmw', 'jaguar']


    """

    module_path = os.path.dirname(__file__)
    cars_path = os.path.join(module_path, "files", "cars.txt")
    with open(cars_path, "r") as cars_file:
        cars = cars_file.readlines()
        cars = [car.replace("") for car in cars]
    return cars
