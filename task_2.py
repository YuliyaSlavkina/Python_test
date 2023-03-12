import time

cur_time = int(input("Введите время в секундах: "))
time_format = time.strftime("%H:%M:%S", time.gmtime(cur_time))
print(f"Время в формате ч:м:с  -  {time_format}")