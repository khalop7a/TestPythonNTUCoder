n = int(input())
kq = 0
while n != 0:
    kq += n % 10
    n = n // 10

if kq % 10 == 9:
    print("YES")
else:
    print("NO")