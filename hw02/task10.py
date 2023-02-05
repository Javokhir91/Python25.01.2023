# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
#  решкой, а некоторые – гербом. Определите минимальное число
#  монеток, которые нужно перевернуть, чтобы все монетки были
#  повернуты вверх одной и той же стороной. Выведите минимальное
#  количество монет, которые нужно перевернуть.
#  5 -> 1 0 1 1 0 2

from random import randint

coin = int(input("enter quantity coins: "))
coins = [randint(0, 1) for i in range(coin)]
print(coins)
c = 0
r = 0
for item in coins:
    if item == 0:
        c += 1
    else:
        r += item
if c < r:
    print(c)
else:
    print(r)
# И тут нашел хорошую штуку как коинт ))
# if coins.count(0) < coins.count(1):
#     print(coins.count(0))
# else:
#     print(coins.count(1))
