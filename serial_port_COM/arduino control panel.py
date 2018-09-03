# control panel for arduino
# todo - use argparse, make digital input
# and analog input/output

import serial
import time
ser = serial.Serial('COM7', 9600, timeout=0)
time.sleep(2)
ser.write(b'5')
print("Hi, I'm COM7 port! Let's rock!")

def read():
    return chr(int(ser.readline().strip().decode('UTF-8')))
def write():
    ser.reset_input_buffer()
    ser.write(input().encode('UTF-8'))

def greetings():
    print("Вас приветствует система управления ардуино!")
    print("Для того чтобы задать цифровой вход нажмите 'I'")
    print("Для того чтобы задать цифровой выход нажмите 'O'")
    print("Для того чтобы задать аналоговый вход нажмите 'C'")   
    print("Для того чтобы задать аналоговый выход нажмите 'Z'")
    print("Для выхода нажмите 'q'")

def readwrite():
    write()
    time.sleep(0.1)
    data = read()
    return data

def dig_out():
    print("Режим цифрового вывода. Введите номер порта, ")
    print("затем введите символ 'e'. Для сброса значения введите 's'.")
    print("Для выхода введите 'q'")
    while True:
        data = readwrite()
        if data == '':
            print("повторите ввод")
        if data == 'e':
        print("Введите сигнал - '1' или '0'")
            data = readwrite()
            print("будет подано на порт:");
            print(port)
            print("значение:")
            if  (data1 == '0'): print("LOW")
            elif (data1 == '1'): print("HIGH")
            print("Возвращение в главное меню")
            print("...")
            break
        port = data
        print("вы ввели номер порта:")
        print(port)

while True:
    greetings()
    data = readwrite()
    if data != '' :
        print(data)
    if data == 'q' :
        break
    #if data == 'I':
        
    if data == 'O':
        dig_out()
        
    #if data == 'C':
    #if data == 'Z':

ser.close()
    

