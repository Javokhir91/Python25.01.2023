# Задача 2: - HARD необязательная, идет за 3 обязательных
# Найдите сумму цифр любого вещественного или целого числа.
# Можно использовать decimal. Через строку решать нельзя.

nums = float(input("Введите трехзначное число: "))
num1 = str(nums)
num = int(num1)

num1 = num % 10
num2 = num % 100 // 10
num3 = num // 100

print(f'сумму цифр трехзначного числа -> {num1 + num2 + num3}')