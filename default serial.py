"""
Главное - помнить о магии с encode/decode и числом 48
encode переводит в биты по таблице, начинающейся с 1 : '1'
тогда как
"""
import serial
import time
ser = serial.Serial('COM7', 9600, timeout=0)
print("Hi, I'm COM7 port! Let's rock!")

def read():
    return chr(int(ser.readline().strip().decode('UTF-8')))
def write():
    ser.reset_input_buffer()
    ser.write(input().encode('UTF-8'))

while True:
    print('Вас приветствует тест последовательного порта')
    #time.sleep(0.5)
    write()
    time.sleep(0.1)
    data = read()
    if data != '' :
        print(data)
    if data == 'q' :
        break

ser.close()
