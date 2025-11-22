#1-misol
import random

son = random.randint(1, 100)
print("Son:", son)

if son > 50:
    print("katta")
else:
    print("kichik yoki teng 50")


#2-misol
import random

print(random.choice(["heads", "tails"]))


#3-misol
import random

son = random.randint(1, 20)
print("Son:", son)

if son % 3 == 0:
    print("3 ga bo‘linadi")
else:
    print("3 ga bo‘linmaydi")


#4-misol
import random

lst = [5, 10, 15, 20, 25]
tanlangan = random.choice(lst)
lst.remove(tanlangan)

print("Tanlangan element:", tanlangan)
print("Yangi ro‘yxat:", lst)


#5-misol
import random

son = random.randint(1, 1000)
print("Son:", son)
print("Kvadrati:", son ** 2)


#6-misol
import random

parol = ''.join(str(random.randint(0, 9)) for _ in range(6))
print(parol)


#7-misol
import random
import math

son = random.randint(1, 10)
print("Son:", son)
print("Faktorial:", math.factorial(son))


#8misol
import random

satr = "salomdunyo"
print(random.choice(satr))


#9-misol
import random

son = random.randint(0, 50)
print("Son:", son)

if son % 7 == 0:
    print("7 ga bo‘linadi")
else:
    print("7 ga bo‘linmaydi")


#10-misol
import random

son = random.randint(1, 4)
print("Son:", son)

if son == 1:
    print("Siz 1 ni oldingiz!")
elif son == 2:
    print("Bu 2 – omadli son!")
elif son == 3:
    print("3 chiqdi – davom eting!")
else:
    print("4 – eng yuqori natija!")
