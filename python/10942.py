size_lst = int(input())
lst = []
temp = []
# 리스트 값 받기
# for i in range(0, size_lst):
#     s = int(input())
#     lst.append(s)
lst = list(map(int, input().split()))
# 질문 수
size_ques = int(input())

# 질문 입력
for j in range(0, size_ques):
    a, b = map(int, input().split())  # from to

    temp = lst[a - 1 : b]
    temp2 = temp.copy()
    temp2.reverse()

    if temp == temp2:
        print("Answer!!!", 1)
        temp = []
    else:
        print("Answer!!!", 0)
        temp = []
