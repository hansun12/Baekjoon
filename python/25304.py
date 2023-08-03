payment = int(input())
round = int(input())
money = 0

for _ in range(round):
    (a, b) = map(int, input().split())
    money += a * b

if money == payment:
    print("Yes")
else:
    print("No")
