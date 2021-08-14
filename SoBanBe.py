import math
a, b = map(int, input().split())
kq1, kq2 = 0, 0


def tong_cac_uoc(n):
    kq = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i ==0:
            kq += i + n // i
    return kq


kq1 = tong_cac_uoc(a)
kq2 = tong_cac_uoc(b)
if int(kq1) == int(kq2):
    print("YES")
else:
    print("NO")


