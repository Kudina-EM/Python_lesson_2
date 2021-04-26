# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = input('введи имя:')
surname = input('введи фамилию:')
year = (input('введи год рождения:'))
city = input('введи город проживания:')
email = input('введи email:')
phone = input('введи номер телефона:')


def my_func(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)
print(my_func(name = 'Катя', surname = 'Кудина', year = '1980', city = 'Москва', email = 'email@mail.ru', phone = '8-916-280'))
