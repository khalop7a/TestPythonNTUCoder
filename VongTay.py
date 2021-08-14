n = int(input())
kq = (n-1) % 7 + 1
if ((n - 1) // 7) % 2 == 0:
    print(str(7 - kq) + " " + str(kq))
else:
    print("{} {}".format(kq, 7 - kq))