word = list(input())
temp = word.copy()
word.reverse()

if word == temp:
    print(1)
else:
    print(0)
