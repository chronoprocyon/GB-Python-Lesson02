new_list = input("Введите слова через пробел ")

new_list = new_list.split()

counter = 0

while counter < len(new_list):
    if len(new_list[counter]) > 10:
        print(counter + 1, new_list[counter][:10])
    else: print(counter + 1, new_list[counter])
    counter += 1
