n = int(input())
kq = n % 7
if ((n - 1) // 7) % 2 == 0:
    print(str(7 - kq) + " " + str(kq))
else:
    print(str(kq) + " " + str(7-kq))