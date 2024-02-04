# 단순하게 행렬 연산으로 계산할 경우
# 입력 Q*(N+1)
# 은닉층 가중치 (N+1)*(M+1)
# 출력층 가중치 (M+1)*1
# -> Q*1
# 최대 (2000*2001)*(2001*2001)*(2001*1)이니
# 행렬 연산에서 시간 초과가 난다.
# O(QNM + QM1)

# 출력 = summation(a_i*x_i+b_i) from i=1 to i=N
# 출력 = summation(a_i*x_i)+b from i=1 to i=N
# 꼴의 식으로 구성되니
# xi가 모두 0일 때(라인 b)와 하나만 1일 때의 차이를 계산하여 ai를 구한다.
# xi에 ai가 곱해지면 출력이 나오니
# 이 ai를 진짜 가중치라고 봐도 좋을 것이다. 라인 a.
# 입력 Q*(N+1)
# 진짜 가중치 (N+1)*1
# -> Q*1
# 최대 (2000*2001)*(2001*1)이니
# 시간 초과가 나지 않는다.
# O(QN1)
# 진짜 가중치 행렬을 만들기 위하여 사전 작업이 필요하긴 하나
# N번의 루프에서 (1*M)*(M*1)으로
# 이것도 O(N*1M1)이니
# 합하더라도 훨씬 빠르다.


import sys
input = sys.stdin.readline
print = sys.stdout.write


def mm(left, right):
    R = len(left)
    J = len(left[0])
    C = len(right[0])
    temp = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            temp[r][c] = sum(
                left[r][j]*right[j][c] for j in range(J)
            )
    return temp


def make_true_w():
    true_w = [[None] for _ in range(N+1)]

    for i in range(N, N+1):
        temp_input = [hidden_w[-1]]
        b = mm(temp_input, output_w)[0][0]
        true_w[i] = [b]  # 라인 b.
    for i in range(N):
        temp_input = [[hidden_w[i][c]+hidden_w[-1][c] for c in range(M+1)]]
        # 기본적으로 temp_input = mm(00~~1~~00, hidden_w)인데
        # mm연산에 비해 0*something을 안 해도 돼서 훨씬 빠름.
        a = mm(temp_input, output_w)[0][0] - b
        true_w[i] = [a]  # 라인 a.
    return true_w


N, M, Q = map(int, input().split())
#
hidden_w = [[0 for _ in range(M+1)] for _ in range(N+1)]
for col in range(M):
    temp = list(map(int, input().split()))
    Ci = temp[0]
    for i in range(1, 1+Ci):
        hidden_w[temp[i]-1][col] = temp[i+Ci]
        # hidden_w[row][col] = weight
    hidden_w[-1][col] = temp[-1]  # 바이어스의 가중치
hidden_w[-1][-1] = 1  # 출력층의 바이어스를 위한 1
# AD0
# BE0
# CF0
# bb1 형태이고 (입력~~1)*(000~~1)이 곱해져서 (1)만 남고 이게 바이어스에 곱해짐
#
output_w = [[i] for i in map(int, input().split())]
#
input_mat = [list(map(int, input().split()))+[1] for _ in range(Q)]
# +[1]을 해줘서 은닉층의 바이어스를 위한 1


true_w = make_true_w()


ans_mat = mm(input_mat, true_w)  # Q*1


print('\n'.join(str(ans[0]) for ans in ans_mat))
