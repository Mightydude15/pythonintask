# Задача 6. Вариант 16.
# Создайте игру, в которой компьютер загадывает имя одной из шести официальных
# жен Ивана IV Грозного, а игрок должен его угадать.

# Komissarov N.D.
# 15.04.2017

import random

wifes = "Анастасия Романовна", "Мария Темрюковна", "Марфа Собакина", "Анна Колтовская", "Анна Васильчикова", "Мария Нагая"

secret = random.choice(["Анастасия Романовна", "Мария Темрюковна", "Марфа Собакина", "Анна Колтовская", "Анна Васильчикова", "Мария Нагая"])

print("Загадано случайное имя одной из шести жён Ивана IV Грозного")
print("Список возможных вариантов ответа: ", wifes)
answer = input("Введите Ваш ответ: \n")
if answer == secret:
    print("Верно! ", secret)
else:
    print("\n\nВы ошиблись.")
    print("\nЗагаданное компьютером имя: " + secret)
