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
            return

    def get_photo_file_ext(self):
        path = os.path.splitext(self.photo_file_name)
        return path[1]

    def __str__(self):
        return f"{self.brand}"


class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        try:
            CarBase.__init__(self, brand, photo_file_name, carrying)
            self.car_type = 'car'
            self.passenger_seats_count = int(passenger_seats_count)
        except Exception as e:
            print(e)


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        CarBase.__init__(self, brand, photo_file_name, carrying)
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

    def __init__(self, brand, photo_file_name, carrying, extra):
        CarBase.__init__(self, brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def is_not_empty_file(file):
    return os.stat(file).st_size > 0


def is_empty_string(value):
    if not len(value.strip()):
        raise Exception
    else:
        return value


def check_photo_path(photo):
    allow = ['.jpeg', '.png', '.jpg', '.gif']
    path = os.path.splitext(photo)
    if path[1] in allow:
        return photo
    else:
        raise Exception


def validate_rows(file):
    result = []
    if is_not_empty_file(file):
        with open(file) as csv_fd:
            reader = csv.DictReader(csv_fd, delimiter=';')
            try:
                pass
            except StopIteration as e:
                # TODO
                return []
            for row in reader:
                try:
                    check_photo_path(row['photo_file_name'])
                    obj = {'car_type': is_empty_string(row['car_type']),
                           'photo_file_name': is_empty_string(row['photo_file_name']),
                           'brand': is_empty_string(row['brand']), 'carrying': float(row['carrying']),
                           'passenger_seats_count': row['passenger_seats_count'],
                           'body_whl': row['body_whl'],
                           'extra': row['extra']}
                    result.append(obj)
                    print(result)
                except Exception as e:
                    print(e)
    return result


def get_car_list(csv_filename):
    car_list = []
    result = validate_rows(csv_filename)
    for row in result:
        try:
            if row['car_type'] == 'car':
                is_empty_string(row['passenger_seats_count'])
                car_list.append(Car(brand=row['brand'], photo_file_name=row['photo_file_name'],
                                    carrying=row['carrying'], passenger_seats_count=row['passenger_seats_count']))
                print(os.path.splitext(row['photo_file_name']))
                print(type(check_photo_path(row['photo_file_name'])))
            elif row['car_type'] == 'truck':
                car_list.append(Truck(brand=row['brand'], photo_file_name=row['photo_file_name'],
                                      carrying=row['carrying'], body_whl=row['body_whl']))
            elif row['car_type'] == 'spec_machine':
                is_empty_string(row['extra'])
                car_list.append(SpecMachine(brand=row['brand'], photo_file_name=row['photo_file_name'],
                                            carrying=row['carrying'], extra=row['extra']))
        except (Exception, IndexError) as e:
            print(e)
    return car_list


# if __name__ == '__main__':
#     pass
