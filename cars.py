import os
import csv


class CarBase:

    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        path = os.path.splitext(self.photo_file_name)
        return path[1]


class Car(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, passenger_seats_count):
        CarBase.__init__(self, car_type, photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, body_whl):
        CarBase.__init__(self, car_type, photo_file_name, brand, carrying)
        try:
            whl = self.body_whl.split("x")
            self.body_length = float(whl[0])
            self.body_width = float(whl[1])
            self.body_height = float(whl[2])
        except Exception as e:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width



class SpecMachine(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, extra):
        CarBase.__init__(self, car_type, photo_file_name, brand, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)
    return car_list
