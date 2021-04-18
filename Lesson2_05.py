my_list = [7, 5, 3, 3, 2]

while True:
    rate = input("Введите натуральное число рейтинга ")
    try:
        rate = int(rate)
        my_list.append(rate)
        my_list.sort()
        my_list.reverse()
        print(my_list)
        break

    except ValueError:
        continue