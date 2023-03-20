try:
    my_list = [7, 5, 3, 3, 2]
    n = int(input('Введите ваше число: '))
    if n <= min(my_list):
        my_list.append(n)
        print(my_list)
    elif n >= max(my_list):
        my_list.insert(0, n)
        print(my_list)
    else:
        i = 0
        while n < my_list[i]:
            i += 1
        my_list.insert(i, n)
        print(my_list)
except ValueError:
    print('Введите целое положительное число цифрой.')
finally:
    print("END")