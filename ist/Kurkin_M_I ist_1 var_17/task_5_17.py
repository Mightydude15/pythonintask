#Задача 5. Вариант 17.
#Напишите программу, которая бы при	запуске	случайным образом отображала название одной	из трех	стран, входящих	в военно-политический блок "Тройственный союз".

#Kurkin M. I.
#19.04.2017
print ("Данная программа случайным образом отображает название одной	из трех	стран, входящих	в военно-политический блок <Тройственный союз>")

import random

import string

# создаем список стран и вносим их в массив

country = ["Германия","Австро-Венгрия","Италия"]

print("Одна из стран входящая в тройственный союз ", random.choice(country))

input ("Для выхода из программы нажмите клавишу <Enter>.")