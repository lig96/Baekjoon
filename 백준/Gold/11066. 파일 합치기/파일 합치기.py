# 시간 확인용 펌
# https://www.acmicpc.net/source/66175852

import sys
input=sys.stdin.readline

t= int(input())
for i in range(t):
    K = int(input())  # 소설을 구성하는 장의 수
    arr = [0]+list(map(int, input().split()))

    dp = [[0 for i in range(K+1)] for j in range(K + 1)]
    #dp[i][j] : i부터 j까지 합쳤을 때 최솟값..

    for i in range(1,K+1):
        for j in range(1,K+1): #초기값.. 연속한 숫자들에 대해서만 처리
            if j==i+1:
                dp[i][j]=arr[i]+arr[j]

    for i in range(K-1,0,-1):
        for j in range(1,K+1):
            if dp[i][j]==0 and i<j:
                dp[i][j]=min([dp[i][k]+dp[k+1][j] for k in range(i,j)])+sum(arr[i:j+1])

    print(dp[1][K])



