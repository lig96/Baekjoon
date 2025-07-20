import sys
input = sys.stdin.readline


N = int(input())
A_arr = list(map(int, input().split()))
B, C = map(int, input().split())


ans = 0
for Ai in A_arr:
    ans += 1
    Ai -= B
    if Ai <= 0:
        continue
    ans += int(((Ai-0.001)//C)+1)  # ceil(Ai/C)
    # Ai = 0


print(ans)
