# 1. Поработайте с переменными, создайте несколько, выведите на экран.
a = 1
b = 2
print(a + b)

# Запросите у пользователя некоторые числа и строки и сохраните в переменные
# затем выведите на экран.

value_1 = int(input("Введите первое слагаемое"))
value_2 = int(input("Введите второе слагаемое"))
print(f"Сумма Ваших слагаемых равна {value_1 + value_2}")

name = input("Введите Ваше имя")
city = input("Введите Ваш город")
print(f"Привет, {name}, из города {city}!")

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


time_in_sec = int(input("Введите время в секундах"))
time_in_min, seсond = divmod(time_in_sec, 60)
time_in_hour, minute = divmod(time_in_min, 60)
print(f"Указанное время соответствует: {time_in_hour}:{minute}:{seсond}")

# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input("Введите число n ")
nn = n + n
nnn = nn + n
rezult = int(n) + int(nn) + int(nnn)
print(f"Сумма n, nn и nnn равна {rezult}")

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

x = int(input("Введите число х"))
x_dev = 0
maximum = 0
while x > 9:
    x_q, x_dev = divmod(x, 10)
    x = x_q
    if x_dev >= maximum:
        maximum = x_dev
if x > maximum:
    maximum = x
print(f"самая большая цифра в числе х - {maximum}")

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.


revenue = float(input("Введите значение выручки"))
costs = float(input("Введите значения издержек"))
if revenue > costs:
    print("Ваша фирма приносит прибыль")
else:
    print("Ваша фирма работает в убыток или не приносит прибыль")

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = float(input("Введите значение выручки"))
costs = float(input("Введите значения издержек"))
if revenue > costs:
    profitability = revenue / costs
    staff = int(input("Ваша фирма приносит прибыль. Укажите количество сотрудников в фирме"))
    if staff == 0:
        print("Ваша фирма ликвидирована, за вами уже выехали")
    else:
        profitability_for_person = profitability / staff
    print(f"Прибыль фирмы в расчёте на одного сотрудника составляет {profitability_for_person}")
else:
    print("Ваша фирма работает в убыток или не приносит прибыль")

# 7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.


a = float(input("Введите число а, составляющее расстояние за 1 день"))
b = float(input("Введите число b, составляющее желаемый результат"))
i = 1
if a < b:
    while a < b:
        a = a + a / 100 * 10
        i = i + 1
    print(f"Количество дней, за которое будет достугнут результат - {i}")
else:
    print("Результат достигнут")

# коммент для пул реквеста