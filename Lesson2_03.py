#list

new_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]


while True:
    month = input("Введите месяц в виде целого числа ")
    try:
        month = int(month)
        if 1 <= month <= 12:
            break
        else:
            print("Введите целое число от 1 до 12")
    except ValueError:
        print("Введите целое число от 1 до 12")


print(new_list[month - 1])

#dict

new_dict = {"1": "Зима", "2": "Зима", "3": "Весна", "4": "Весна", "5": "Весна", "6": "Лето", "7": "Лето", "8": "Лето", "9": "Осень", "10": "Осень", "11": "Осень", "12": "Зима"}

while True:
    month = input("Введите месяц в виде целого числа ")
    if new_dict.get(month) != None:
        print(new_dict.get(month))
        break
    else:
        print("Введите целое число от 1 до 12")

