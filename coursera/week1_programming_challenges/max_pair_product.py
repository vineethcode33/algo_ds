# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
product = 0
a.sort()

if len(a)>1:
    product = a[-1]*a[-2]
elif len(a)==1:
    product = a[0]

print(product)