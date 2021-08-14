import math
n = int(input())
result = True
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        result = False
        break
if n == 1:
    print("NO")
    exit()
if result:
    print("YES")
else:
    print("NO")