from cars_main import get_car_list
import sys

input_csv_filename = sys.argv[1]

car_list = get_car_list(input_csv_filename)
for car in car_list:
    print('---')
    print(car.car_type)
    print(car.brand)
    print(car.photo_file_name)
    print(car.carrying)
    print('---')
    print(car.get_photo_file_ext())
        
    if (car.car_type == 'truck'):
        print('---')
        print(car.get_body_volume())
            
    if (car.car_type == 'car'):
        print('---')
        print(car.passenger_seats_count)
            
    if (car.car_type == 'spec_machine'):
        print('---')
        print(car.extra)
            
    print('---')
    print(' ')