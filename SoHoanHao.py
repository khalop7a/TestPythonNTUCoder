import math
a = int(input())
kq = 1
for i in range(2, int(math.sqrt(a))+1):
    if a % i == 0:
        kq += i + a // i

if kq == a:
    print("YES")
else:
    print("NO")
