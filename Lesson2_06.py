new_list = []
counter = 1

while True:
    question = input("Хотите ввести элемент? ")
    if question  == "Да":
        new_list.append((counter, {"название": input("Введите название товара "), "цена": input("Введите цену товара "),
                         "количество": input("Введите количество товара "),
                         "ед": input("Введите единицу измерения количества товара")}))
        counter += 1
    elif question == "Нет":
        break
    else: print("Ответьте Да или Нет")

counter = 1
new_dict = new_list[0][1].copy()

while counter < len(new_list):
    for key in new_list[counter][1].keys():
        if counter == 1:
            temp_list = []
            temp_list.append(new_dict.get(key))
        else:
            temp_list = new_dict.get(key)[:]
        temp_list.append(new_list[counter][1].get(key))
        temp_list = list(set((temp_list)))
        new_dict.update({key: temp_list[:]})
    counter += 1


print(new_dict)