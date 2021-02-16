import os
import csv


class CarBase:

    def __init__(self, car_type, photo_file_name, brand, carrying):
        try:
            self.car_type = car_type
            self.photo_file_name = photo_file_name
            self.brand = brand
            self.carrying = carrying
        except Exception as e:
            print(e)


    def get_photo_file_ext(self):
        path = os.path.splitext(self.photo_file_name)
        return path[1]


class Car(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, passenger_seats_count):
        try:
            CarBase.__init__(self, car_type, photo_file_name, brand, carrying)
            self.passenger_seats_count = passenger_seats_count
        except Exception as e:

            print(e)


class Truck(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, body_whl):
        CarBase.__init__(self, car_type, photo_file_name, brand, carrying)
        try:
            whl = body_whl.split("x")
            self.body_length = float(whl[0])
            self.body_width = float(whl[1])
            self.body_height = float(whl[2])
        except Exception as e:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0
            print(e)

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, extra):
        CarBase.__init__(self, car_type, photo_file_name, brand, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row['car_type'] == 'car':
                    car_list.append(Car(row['car_type'], row['photo_file_name'], row['brand'],
                                        row['carrying'], row['passenger_seats_count']))
                elif row['car_type'] == 'truck':
                    car_list.append(Truck(row['car_type'], row['photo_file_name'], row['brand'],
                                        row['carrying'], row['body_whl']))
                elif row['car_type'] == 'spec_machine':
                    car_list.append(SpecMachine(row['car_type'], row['photo_file_name'], row['brand'],
                                          row['carrying'], row['extra']))
            except IndexError as e:
                print(e)
    return car_list


#if __name__ == '__main__':

