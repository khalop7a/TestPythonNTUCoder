n = int(input())
data = input()
a = data.split()
kq = 0
for i in a:
    if int(i) == 1:
        kq += 1
    else:
        kq -= 1
if kq < 0:
    kq *= -1
print(kq)



