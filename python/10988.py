word = list(input())

for i in range(0, len(word)):
    # 짝수일떄
    if len(word) % 2 == 0:
        if word[i] == word[:-1]:
            print(1)
        else:
            print(0)
    # 홀수일때
    if len(word) % 2 != 0:
        del word[len(word) // 2]
        if word[i] == word[:-1]:
            print(1)
        else:
            print(0)
