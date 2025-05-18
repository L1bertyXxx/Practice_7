a = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
b = int(input("введите кол-во дней"))

if 0 <= b <=7:
    print(f"Ваши выходные дни: {a[7-b:7]}")
    print(f"Ваши рабочие дни: {a[:7 - b]}")
else:
    print("error")