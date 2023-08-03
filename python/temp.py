import sys

cnt = 0

for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline()
    alp = [line[0]]
    group = True
    for i in range(1, len(line)):
        if line[i - 1] == line[i]:
            continue
        if line[i] in alp:
            group = False
            break
        alp.append(line[i])

    if group:
        cnt += 1

print(cnt)
