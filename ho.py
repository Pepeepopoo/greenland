Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import serial // Serial is not included with Python. It is a package that you'll need to install separately. 
... import time // импортируем модуль time
... import serial.tools.list_ports // получаем список доступных последовательных портов
... 
... speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200'] // сохраняем список доступных скоростей
... ports = [p.device for p in serial.tools.list_ports.comports()] // возвращаем список доступных COM-портов
... port_name = ports[0] // присваиваем имя первому порту равное 0 
... port_speed = int(speeds[-1]) // выбираем первую с конца скорость из списка доступных 
... port_timeout = 10 //  timeout порта = 10
... ard = serial.Serial(port_name, port_speed, timeout = port_timeout) // создаем объект `Serial`, указывая имя порта и скорость передачи данных
... time.sleep(1) // приостанавливаем программу на 1 секунду
... ard.flushInput() // очищаем входной буфер
... // раздел последовательного чтения 
... try:
...     msg_bin = ard.read(ard.inWaiting()) // в переменной msg_bin происходит чтение ard и возвращается количество байт в буфере приема.
...     msg_bin += ard.read(ard.inWaiting()) // прибавление по одному
...     msg_bin += ard.read(ard.inWaiting())
...     msg_bin += ard.read(ard.inWaiting())
...     msg_str_ = msg_bin.decode() // преобразование в представительный вид 
...     print(len(msg_bin)) / выводится длина, до которой дошли 
...     
... except Exception as e:    
...     print('Error!') // выводим ошибку
...     ard.close() // закрываем объект
...     time.sleep(1) // приостановление работы программы на 1 секунду
...     print(msg_str_) // выводим строковый вид msg_bin
