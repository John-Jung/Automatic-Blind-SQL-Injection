ascii = 82

min = 1
max = 127
cha = 0
while min < max:
    cha = cha + 1
    mid = int((min + max)/2)
    if ascii > mid:
        min = mid + 1
    else:
        max = mid
        print("{}차 ~ {} :평균 {}".format(cha, min, max ,mid))

    if ascii > mid:
        min = mid + 1
        print("-> 참 {} ~ {}".format(min, max))
    else:
        max = mid
        print("-> 거짓 {} ~ {}".format(min, max))




