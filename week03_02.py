import os
import csv


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        try:
            self.photo_file_name = photo_file_name
            self.brand = brand
            self.carrying = float(carrying)
        except Exception as e:
            print(e)

    def get_photo_file_ext(self):
        path = os.path.splitext(self.photo_file_name)
        return path[1]

    def __str__(self):
        return f"{self.brand}"


class Car(CarBase):

    def __init__(self, brand, photo_file_name,  carrying, passenger_seats_count):
        try:
            CarBase.__init__(self, brand, photo_file_name, carrying)
            self.car_type = 'car'
            self.passenger_seats_count = int(passenger_seats_count)
        except Exception as e:
            print(e)


class Truck(CarBase):

    def __init__(self, photo_file_name, brand, carrying, body_whl):
        CarBase.__init__(self, photo_file_name, brand, carrying)
        self.car_type = 'truck'
        try:
            whl = body_whl.split("x")
            if len(whl) == 3:
                self.body_length = float(whl[0])
                self.body_width = float(whl[1])
                self.body_height = float(whl[2])
            else:
                raise Exception
        except Exception as e:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0
            print(e)

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(CarBase):

    def __init__(self, photo_file_name, brand, carrying, extra):
        CarBase.__init__(self, photo_file_name, brand, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def is_not_empty_file(file):
    return os.stat(file).st_size > 0


def get_car_list(csv_filename):
    car_list = []
    if is_not_empty_file(csv_filename):
        with open(csv_filename) as csv_fd:
            reader = csv.DictReader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                try:
                    if row['car_type'] == 'car':
                        car_list.append(Car(photo_file_name=row['photo_file_name'], brand=row['brand'],
                                            carrying=row['carrying'], passenger_seats_count=row['passenger_seats_count']))
                    elif row['car_type'] == 'truck':
                        car_list.append(Truck(photo_file_name=row['photo_file_name'], brand=row['brand'],
                                              carrying=row['carrying'], body_whl=row['body_whl']))
                    elif row['car_type'] == 'spec_machine':
                        car_list.append(SpecMachine(photo_file_name=row['photo_file_name'], brand=row['brand'],
                                                    carrying=row['carrying'], extra=row['extra']))
                except IndexError as e:
                    print(e)
    return car_list


# if __name__ == '__main__':
#     pass
