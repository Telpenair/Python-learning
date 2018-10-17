# inheritance and little exceptions practice
# work with csv file
# interesting: 
#              add encode UTF-8 to open file (without it displays some odd symbols) 
# to do:
#          more practice with class methods

import os
import csv


class BaseCar:
    def __init__(self, car_type='', photo_file_name='', brand='', carrying=0):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(BaseCar):
    def __init__(self, car_type='car', passenger_seats_count=0, photo_file_name='', brand='', carrying=0):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(BaseCar):
    def __init__(self, car_type='truck', body_whl="0x0x0", photo_file_name='', brand='', carrying=0):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.body_whl = body_whl
        body_list = body_whl.split("x")
        self.body_height = float(body_list[0])
        self.body_length = float(body_list[1])
        self.body_width = float(body_list[2])

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(BaseCar):
    def __init__(self, car_type='spec_machine', extra='', photo_file_name='', brand='', carrying=0):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.extra = extra


def open_csv(csv_filename):
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=";")
        csv_row_list = []
        i=0
        heading_csv = []
        for row in reader:
            if (i == 0):
                heading_csv = row
                i += 1
            else:
                csv_row_list.append(row)
    return csv_row_list

def get_car_list(csv_filename):

    csv_row_list = open_csv(csv_filename)
    
    car_list = []
    
    for row in csv_row_list:
        try:
            if (row[0] == ''):
                continue
        except IndexError:
            continue
        if (row[0] == 'car'):
            car_list.append(Car(passenger_seats_count=row[2], photo_file_name=row[3], brand=row[1], carrying=row[5]))
                
        if (row[0] == 'truck'):
            try:
                car_list.append(Truck(body_whl=row[4], photo_file_name=row[3], brand=row[1], carrying=row[5]))
            except ValueError:
                car_list.append(Truck(body_whl='0x0x0', photo_file_name=row[3], brand=row[1], carrying=row[5]))
                    
        if (row[0] == 'spec_machine'):
            car_list.append(SpecMachine(extra=row[6], photo_file_name=row[3], brand=row[1], carrying=row[5]))
    

    return car_list