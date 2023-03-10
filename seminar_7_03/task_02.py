"""2. Напишите код, который запрашивает число и сообщает является ли оно 
 простым или составным. Используйте правило для проверки:
 “Число является простым, если делится нацело только на единицу и на себя”.
 Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

num = int(input("Введите число для проверки от 0 до 100000: "))
while num < 0 or num > 100_000:
    num = int(input("Введите коректное число от 0 до 100000: "))
count = 0
for i in range(2, num // 2 + 1):
    if (num % i == 0):
        count = count + 1
if (count <= 0):
    print("Число простое.")
else:
    print("Число является составным.")