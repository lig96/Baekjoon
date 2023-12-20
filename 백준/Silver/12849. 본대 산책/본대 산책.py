D = int(input())
mod = 1_000_000_007


zeros = [0 for _ in range(8)]
prev = [1, 0, 0, 0, 0, 0, 0, 0]
now = zeros[::]


for _ in range(D):
    now[0] = prev[1]+prev[3]
    now[1] = prev[0]+prev[2]+prev[3]
    now[2] = prev[1]+prev[3]+prev[4]+prev[5]
    now[3] = prev[0]+prev[1]+prev[2]+prev[5]
    now[4] = prev[2]+prev[5]+prev[6]
    now[5] = prev[2]+prev[3]+prev[4]+prev[7]
    now[6] = prev[4]+prev[7]
    now[7] = prev[5]+prev[6]
    for i in range(8):
        now[i] %= mod

    prev, now = now, zeros[::]


print(prev[0])