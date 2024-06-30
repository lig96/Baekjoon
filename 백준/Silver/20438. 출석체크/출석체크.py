import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K, Q, M = map(int, input().split())
sleepers = list(map(int, input().split()))
receivers = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(M)]


students = [0 for _ in range(N+3)]
# 0 출석 안 함
# 1 출석함
# 2 졸고 있음
for sleeper in sleepers:
    students[sleeper] = 2
for receiver in receivers:
    if students[receiver] == 0:
        for temp in range(receiver, N+3, receiver):
            if students[temp] == 0:
                students[temp] = 1


psum = [0]
# psum[E+1] - psum[S]
# = students[0:E+1] - students[0:S]
# = students[S:E+1]
temp = 0
for student in students:
    temp += int(student != 1)
    psum.append(temp)
for S, E in queries:
    print(str(psum[E+1] - psum[S])+'\n')
