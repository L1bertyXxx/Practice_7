from random import randint

list = [randint(0,10) for i in range(10)]
print(list)

dup = []

for i in list:
    if list.count(i) > 1 and i not in dup:
        dup.append(i)
for i in dup:
    count = list.count(i)
    print(f"Число {i} встречается {count}")

