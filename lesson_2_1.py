# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list = ['Max', 32, 5.5, 'Moscow']
for i in list[:]:
    print(type(i))

# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list = [1, 2, 3, 4, 5]
if len(list) % 2 == 0:
    i = 0
    while i < len(list):
        el = list[i]
        list[i] = list[i+1]
        list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(list) - 1:
        el = list[i]
        list[i] = list[i + 1]
        list[i + 1] = el
        i += 2
print(list)

# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
number_mon = int(input("Введите номер месяца: "))
if number_mon == 1 or number_mon == 12 or number_mon == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif number_mon == 3 or number_mon == 4 or number_mon ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif number_mon == 6 or number_mon == 7 or number_mon == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif number_mon == 9 or number_mon == 10 or number_mon == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца нет")

# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

empty_str = str(input('Введи предложение:  '))
list_str =  empty_str.split(' ')
for i, el in enumerate(list_str, 1):
    if len(el) > 10:
        el = el[:10]
    print(f"{i}. - {el}")


# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
number = int(input('ввди число:  '))
k = my_list.count(number)
for element in my_list:
    if k > 0:
        i = my_list.index(number)
        my_list.insert(i+k, number)
        break
    else:
        if number > element:
            l = my_list.index(element)
            my_list.insert(l, number)
            break
        elif number < my_list[len(my_list)-1]:
            my_list.append(number)
print(my_list)