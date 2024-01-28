import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

def power(a, b):
    return a ** b

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Ошибка: невозможно извлечь квадратный корень из отрицательного числа"

def factorial(a):
    if a >= 0:
        return math.factorial(a)
    else:
        return "Ошибка: невозможно вычислить факториал отрицательного числа"

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

def input_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Ошибка: введите число")

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("0. Выход")

    choice = input_number("Введите номер операции: ")

    if choice == 0:
        break

    if choice in [1, 2, 3, 4, 5]:
        num1 = input_number("Введите первое число: ")
        num2 = input_number("Введите второе число: ")

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 5:
            result = power(num1, num2)

        print("Результат: ", result)

    elif choice in [6, 7, 8, 9, 10]:
        num = input_number("Введите число: ")

        if choice == 6:
            result = square_root(num)
        elif choice == 7:
            result = factorial(num)
        elif choice == 8:
            result = sin(num)
        elif choice == 9:
            result = cos(num)
        elif choice == 10:
            result = tan(num)

        print("Результат: ", result)

    else:
        print("Ошибка: неверный номер операции")