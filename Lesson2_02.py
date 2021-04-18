new_list = []

while True:
    question = input("Хотите ввести элемент? ")
    if question  == "Да":
        new_list.append(input("Введите элемент "))
    elif question == "Нет":
        break
    else: print("Ответьте Да или Нет")

counter = 0

while counter < len(new_list) // 2:
    new_list[counter * 2], new_list[counter * 2 + 1] = new_list[counter * 2 + 1], new_list[counter * 2]
    counter += 1

print(new_list)