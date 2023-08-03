word = input()
word = word.lower()
count = 0
lst = [0] * 26

for i in range(len(word)):
    lst[(ord(word[i]) - ord("a"))] += 1

m = max(lst)
for i in range(len(lst)):
    if lst[i] == m:
        count += 1

if count == 1:
    print((chr(lst.index(max(lst)) + ord("a"))).upper())
else:
    print("?")
