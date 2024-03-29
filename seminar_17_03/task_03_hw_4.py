"""Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""
def check(x):
    if x % 50 == 0:
        return True
    else:
        return False


def add(amount, n, count=0):
    if (check(n)):
        if count == 3:
            count = 0
            total = (amount + n) * 1.03
            print(total)
            return total, count
        else:
            count += 1
            total = amount + n
            print(total)
            return total, count
    else:
        print("error, вводимая сумма не кратна 50")
        return amount, count


def calc_commission(n):
    if n * 0.015 < 30:
        return 30
    elif n * 0.015 > 600:
        return 600
    else:
        return n * 0.015


def take_off(amount, n, count=0):
    if (check(n) and amount > n):
        if count == 3:
            count = 0
            total = ((amount - n) - calc_commission(n)) * 1.03
            if total < 0:
                print("error, total < 0")
                return amount, count
            print(total)
            return total, count
        else:
            count += 1
            total = (amount - n) - calc_commission(n)
            if total < 0:
                print("error, total < 0")
                return amount, count
            print(total)
            return total, count
    else:
        print("error, снимаемая сумма не кратна 50 или снимаемая сумма больше суммы на счете")
        return amount, count


amount = 0
count = 0
main_flag = True
while main_flag:
    s = int(input("Введите действие: 1 - добавить; 2 - снять; 3 - выйти: "))
    if s == 1:
        n = int(input("Введите сумму добавления, кратную 50: "))
        amount, count = add(amount, n, count)
    elif s == 2:
        n = int(input("Введите сумму снятия, кратную 50: "))
        amount, count = take_off(amount, n, count)
    else:
        break