# [Platinum III] Dijkstra's Nightmare (Hard) - 27675 

[문제 링크](https://www.acmicpc.net/problem/27675) 

### 성능 요약

메모리: 33392 KB, 시간: 60 ms

### 분류

벨만–포드, 비트마스킹, 해 구성하기, 데이크스트라, 그래프 이론, 구현, 수학, 최단 경로

### 제출 일자

2024년 3월 9일 11:49:13

### 문제 설명

<p>Every computer scientist should be familiar with <a href="https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm">Dijkstra’s algorithm</a>: the basic algorithm to compute single-source shortest paths in a given graph. When executing the algorithm, we maintain a set of <em>active</em> vertices. In each iteration, we select and process the active vertex with the smallest current distance. When processing a vertex, we examine the outgoing edges. Whenever one of them can be used to improve the distance to an adjacent vertex, we do so and mark that adjacent vertex as active.</p>

<p>It is well-known that the algorithm is efficient whenever all edge lengths are non-negative. The reference implementation we provided in this problem runs in <em>O</em>(<em>m</em>log<em>n</em>) time for such graphs (where <em>m</em> is the number of edges and <em>n</em> is the number of vertices).</p>

<p>Things start getting hairy once we allow edges with negative lengths. Finding the shortest <em>simple</em> path (i.e., a path with no repeated vertices) in such a graph is actually an NP-hard problem. Some versions of Dijkstra’s algorithm will terminate quickly for such graphs but sometimes they will give incorrect results. This is not the case for our reference implementation. Our reference implementation is actually solving a slightly different problem: for each vertex <em>v</em>, we are looking for the length of the shortest <em>walk</em> from the starting vertex to <em>v</em>. (A walk is a path that may contain repeated vertices and edges. Note that if all edge lengths are positive, the shortest walk has to be a simple path.)</p>

<p>Sometimes there is no shortest walk from the starting vertex to some vertex <em>v</em>, because for every walk we can find an even shorter one. For such inputs our reference implementation never terminates.</p>

<p>In this problem, the word “graph” always denotes a directed weighted graph with no duplicate edges and no self-loops. The letters <em>n</em> and <em>m</em> denote its numbers of vertices and edges. Vertices are numbered 0 through <em>n</em> − 1. The starting vertex is 0.</p>

<p>We want you to show that there are graphs for which Dijkstra’s algorithm terminates, but its time complexity is exponential in the number of vertices.</p>

<p>The reference implementation contains a variable named <code>PROCESSED_VERTICES</code>. You are given several values <em>p</em>. For each <em>p</em>, construct any valid graph for which our implementation will terminate after finitely many steps, and the value of <code>PROCESSED_VERTICES</code> at the end will be exactly <em>p</em>.</p>

### 입력 

 <p>You are given the file <code><a href="https://upload.acmicpc.net/11b8d3b1-4647-4121-a1fb-c7322a3edd51/">d2.in</a></code>. The first line of this file contains an integer <em>t</em> specifying the number of test cases. Each test case is preceded by a blank line. Each test case consists of a single line containing the number <em>p</em>. You may assume that 1 ≤ <em>p</em> ≤ 10 000 000.</p>

### 출력 

 <p>In a valid graph, 1 ≤ <em>n</em> ≤ 60 and the length of each edge fits into a signed 32-bit integer variable.</p>

<p>Each graph should be output as a sequence of <em>m</em> + 2 lines. The first of these lines should contain <em>n</em>, the second line should contain <em>m</em>, and each of the following <em>m</em> lines should contain three integers describing an edge – the vertex numbers of its two endpoints (between 0 and <em>n</em> − 1) followed by its length.</p>

<p>The output should contain a sequence of <em>t</em> such graphs. Do not output any empty lines between them.</p>

