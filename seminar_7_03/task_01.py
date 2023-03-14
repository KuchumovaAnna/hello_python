"""1.Треугольник существует только тогда, когда сумма любых двух его сторон больше
   третьей. Дано a, b, c - стороны предполагаемого треугольника.
   Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
   Если хотя бы в одном случае отрезок окажется больше суммы двух других,
   то треугольника с такими сторонами не существует. 
   Отдельно сообщить является ли треугольник разносторонним,
   равнобедренным или равносторонним.
"""

a = int(input('Enter side а: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

if a + b > c and b + c > a and a + c > b:
    print("The triangle exists.")
    if a == b == c:
        print("The triangle is equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is isosceles.")
else:
    print("Sorry, there is no such triangle!")

