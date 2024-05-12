// # 공식 사이트 솔루션 그대로 씀.
// #
// # dfs + range maximum query 세그먼트 트리 + 오프라인 쿼리
// #
// # 포레스트를 미리 구성 후 각 트리의 시작점을 roots에 저장하여
// # 각 root에서 dfs(=트리라서 백트래킹)로 순회한다.
// # 정점 x를 진실로 갖는 학생이 있으면 표기하고
// # 정점 x를 거짓으로 갖는 학생이 있으면
// # 가장 최근 진실인 정점 y ~ 정점 x의 경로 내의 가중치 중 최댓값을 찾는다.
// # 트리 구조이기 때문에 경로의 유일함과 y의 depth(=dlen)가 얕은 게 보장된다.
// # 진실 y의 깊이 = 2, 거짓 x의 깊이 = 4이라면
// # 가상의 리스트 [edge_num[?], e[?], e[y], e[?], e[x], e[초과]]에 대하여
// # 구간 [2, 4] 혹은 [2, 5)에 대하여 최댓값을 찾는 쿼리를 날린다고 볼 수 있다.
// # e[초과]는 해당 쿼리에 대하여 쓰이지 않기 때문에 초기화를 안 해도 된다.
// #
// # 엄밀히 말하면 사이클이 있기 때문에 트리는 아니다.
// # 따라서 사이클을 찾은 뒤 위의 과정을 먼저 사이클 내에서 시행해야 한다.
// # 이 과정을 통해 root = 1인 [1, 2, 3, 1, ..] 사이클 + [1, 2, 3, ...] 트리에서
// # 2->3->1(사이클)->2->3->...(트리)로
// # 3진실->1거짓을 올바르게 도출할 수 있다.
// # dfs만 돌린다면 1은 방문 처리가 되었기 때문에 3->1 경로가 없었을 것이다.
// # (참고로 사이클의 시작은 root인 1이 아니라 그 다음 2부터)
// #
// # 세그먼트 트리 재귀 구현은 시간 초과라서 비재귀 구현으로 바꿈.
// # 쿼리의 구간은 [2, 5) 꼴.
// #
// # 그럼에도 53%에서 시간 초과나서 c++17로 제출해서 정답 판정 받음.


// import sys
// sys.setrecursionlimit(int(5e5)+10)
// input = sys.stdin.readline
// print = sys.stdout.write


// def get_max(N, left, right):
//     result = 0
//     left += N
//     right += N
//     while left < right:
//         if left & 1:
//             # 홀수라면
//             result = max(result, rmq[left])
//             left += 1
//         if right & 1:
//             # 홀수라면
//             result = max(result, rmq[right-1])
//             right -= 1
//         left >>= 1
//         right >>= 1
//     return result


// def update(N, i, val):
//     i += N
//     rmq[i] = val
//     while i > 1:
//         if rmq[i >> 1] == max(rmq[i], rmq[i ^ 1]):
//             return
//         rmq[i >> 1] = max(rmq[i], rmq[i ^ 1])
//         i >>= 1
//     return


// def relax(a, ind, b):
//     # a는 call-by-reference
//     # a[ind] = min(a[ind], b)
//     if a[ind] > b:
//         a[ind] = b
//     return


// def process(v):
//     global cur_len
//     for stu_i in trues[v]:
//         latest[stu_i].append(cur_len)
//     for stu_i in falses[v]:
//         if latest[stu_i]:
//             relax(ans, stu_i, get_max(N_tree, latest[stu_i][-1], cur_len))
//     return


// def unprocess(v):
//     for stu_i in trues[v]:
//         latest[stu_i].pop()
//     return


// def dfs(v):
//     global cur_len
//     if used[v]:
//         return
//     used[v] = True
//     process(v)
//     for consequence, argument_i in adj[v]:
//         update(N_tree, cur_len, argument_i)
//         cur_len += 1
//         dfs(consequence)
//         cur_len -= 1
//     unprocess(v)
//     return


// def solve(v):
//     global cur_len
//     for consequence, argument_i in cycles[v]:
//         update(N_tree, cur_len, argument_i)
//         cur_len += 1
//         process(consequence)
//     dfs(v)
//     for consequence, argument_i in cycles[v]:
//         unprocess(consequence)
//     cur_len -= len(cycles[v])
//     return


// def build():
//     def _build(v, cycles, roots, used, data_):
//         # 리스트 data에서 append, pop으로도 가능하지만
//         # append의 시간복잡도가 최대 O(길이)라서 비효율적일 듯.
//         # 리스트를 길이에 따라 선언 후 값 수정하는 방식으로 구현함.
//         dlen = 0
//         while not used[v]:
//             data_[dlen] = v
//             dlen += 1
//             used[v] = flood_fill_i
//             v = parent[v]

//         if used[v] == flood_fill_i:
//             if not adj[v]:  # 라인 A
//                 return
//             roots.append(v)
//             while data_[dlen-1] != v:
//                 element = data_[dlen-1]
//                 cycles[v].append((element, edge_num[element]))
//                 dlen -= 1
//             if edge_num[v] != -1:
//                 cycles[v].append((v, edge_num[v]))
//         return
//     cycles = [[] for _ in range(N)]
//     roots = []
//     used = [0 for _ in range(N)]
//     data_ = [None for _ in range(N)]  # 정점 v의 cycle
//     flood_fill_i = 0
//     for i in range(N):
//         if not used[i]:
//             flood_fill_i += 1
//             _build(i, cycles, roots, used, data_)
//     return cycles, roots


// N = int(5e5)
// N_tree = int(1e6)  # 원문 N=int(1e6)
// # 사이클에서 1번 순회하고 사이클을 포함한 dfs에서 1번 순회해서
// # 세그먼트트리의 바탕이 되는 배열의 길이는 5e5의 2배여야 함.
// INF = float('inf')  # 원문 inf=int(1e9)
// #
// parent = [i for i in range(N)]
// edge_num = [-1 for _ in range(N)]
// adj = [[] for _ in range(N)]
// for argument_i in range(M := int(input())):
//     premise, consequence = map(lambda x: int(x)-1, input().split())
//     parent[consequence] = premise
//     edge_num[consequence] = argument_i
//     adj[premise].append((consequence, argument_i))
// #
// trues = [[] for _ in range(N)]
// falses = [[] for _ in range(N)]
// for stu_i in range(Q := int(input())):
//     temp = list(map(int, input().split()))
//     t = temp[0]
//     for i in range(1, 1+t):
//         trues[temp[i]-1].append(stu_i)
//     f = temp[1+t]
//     for i in range(1+t+1, 1+t+1+f):
//         falses[temp[i]-1].append(stu_i)
// #
// #
// cycles, roots = build()
// #
// #
// ans = [INF for _ in range(Q)]
// used = [False for _ in range(N)]
// rmq = [0 for _ in range(2*N_tree)]
// cur_len = 0
// latest = [[] for _ in range(N)]
// for root in roots:
//     solve(root)
// #
// #
// for v in ans:
//     print(str(-1 if v == INF else v+1)+'\n')


#include <cstdio>
#include <cassert>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <complex>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
using namespace std;
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define sz(a) ((int) (a).size())
#define int64 long long
#define ldb long double
const double pi = acos(-1.0);
const int N = (int) 1e6;
const int inf = (int) 1e9;
int rmq[4 * N], cur_len, ans[N], used[N], cnt, edge_num[N], p[N], data_[N], dlen, u, v, t, q, m;
vector<int> latest[N], trues[N], falses[N], roots;
vector< pair<int, int> > adj[N], cycle[N];

int get_max(int t, int l, int r, int x, int y) {
	if ((r <= x) || (y <= l))
		return -inf;
	if ((x <= l) && (r <= y))
		return rmq[t];
	int m = (l + r) / 2;
	return max(get_max(t * 2 + 1, l, m, x, y), get_max(t * 2 + 2, m, r, x, y));
}

void update(int t, int l, int r, int x, int y) {
	if ((l > x) || (x >= r))
		return;
	if (l + 1 == r)
		rmq[t] = y;
	else {
		int m = (l + r) / 2;
		update(t * 2 + 1, l, m, x, y);
		update(t * 2 + 2, m, r, x, y);
		rmq[t] = max(rmq[t * 2 + 1], rmq[t * 2 + 2]);
	}
}

void relax(int& a, int b) {
	a = min(a, b);
}

void process(int v) {
	for (int i = 0; i < sz(trues[v]); ++i)
		latest[trues[v][i]].pb(cur_len);
	for (int i = 0; i < sz(falses[v]); ++i) {
		int qnum = falses[v][i];
		if (!latest[qnum].empty())
			relax(ans[qnum], get_max(0, 0, N, latest[qnum].back(), cur_len));
	}
}

void unprocess(int v) {
	for (int i = 0; i < sz(trues[v]); ++i)
		latest[trues[v][i]].pop_back();
}

void dfs(int v) {
	if (used[v]) return;
	used[v] = true;
	process(v);
	for (int i = 0; i < sz(adj[v]); ++i) {
		update(0, 0, N, cur_len++, adj[v][i].sc);
		dfs(adj[v][i].fs);
		cur_len--;
	}
	unprocess(v);
}

void solve(int v) {
	for (int i = 0; i < sz(cycle[v]); ++i) {
		update(0, 0, N, cur_len++, cycle[v][i].sc);
		process(cycle[v][i].fs);
	}
	dfs(v);
	for (int i = 0; i < sz(cycle[v]); ++i)
		unprocess(cycle[v][i].fs);
	cur_len -= sz(cycle[v]);
}

void build(int v) {
	++cnt, dlen = 0;
	while (!used[v])
		data_[dlen++] = v, used[v] = cnt, v = p[v];
	if (used[v] == cnt) {
		roots.pb(v);
		while (data_[dlen - 1] != v) {
			cycle[v].pb(mp(data_[dlen - 1], edge_num[data_[dlen - 1]]));
			dlen--;
		}
		if (edge_num[v] != -1)
			cycle[v].pb(mp(v, edge_num[v]));
	}
}

int main() {
	//assert(freopen("input.txt", "r", stdin));
	//assert(freopen("output.txt", "w", stdout));
	scanf("%d", &m);
	memset(p, -1, sizeof(p));
	memset(edge_num, -1, sizeof(edge_num));
	for (int i = 0; i < m; ++i) {
		scanf("%d%d", &u, &v), --u, --v;
		assert(p[v] == -1);
		p[v] = u, edge_num[v] = i;
		adj[u].pb(mp(v, i));
	}
	scanf("%d", &q);
	for (int i = 0; i < q; ++i) {
		ans[i] = inf;
		scanf("%d", &t);
		for (int j = 0; j < t; ++j) {
			scanf("%d", &u), --u;
			trues[u].pb(i);
		}
		scanf("%d", &t);
		for (int j = 0; j < t; ++j) {
			scanf("%d", &u), --u;
			falses[u].pb(i);
		}
	}
	for (int i = 0; i < N; ++i)
		if (p[i] == -1)
			p[i] = i;
	for (int i = 0; i < N; ++i)
		if (!used[i])
			build(i);
	memset(used, 0, sizeof(used));
	for (int i = 0; i < sz(roots); ++i)
		solve(roots[i]);
	for (int i = 0; i < q; ++i)
		printf("%d\n", (ans[i] == inf) ? -1 : ans[i] + 1);
	return 0;
}
