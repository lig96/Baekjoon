import sys
input = sys.stdin.readline


N = int(input())
desks = [list(map(int, input().split())) for _ in range(N)]


consecutive_grade = [0 for _ in range(6)]
temp_conse_gr = [0 for _ in range(6)]
for desk in desks:
    for grade in range(1, 6):
        if grade in desk:
            temp_conse_gr[grade] += 1
            consecutive_grade[grade] = max(
                consecutive_grade[grade],
                temp_conse_gr[grade]
            )
        else:
            temp_conse_gr[grade] = 0


ans_i, ans_v = None, -float('inf')
for i, v in enumerate(consecutive_grade):
    if v > ans_v:  # 동순위일 시 작은 i
        ans_i, ans_v = i, v
print(ans_v, ans_i)
