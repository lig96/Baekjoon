# [Gold III] LIST - 3291 

[문제 링크](https://www.acmicpc.net/problem/3291) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

그리디 알고리즘

### 제출 일자

2023년 12월 16일 22:55:54

### 문제 설명

<p>Little Michael lives in a small country and likes to watch a TV music show which is emitted every Sunday afternoon. It presents the same songs every week and, according to votes, displays popularity list of those songs.</p>

<p>Michael played too long with his friend one Sunday and failed to see new popularity list. He was sad, but he soon realized that he would be able to at least partially reconstruct the popularity list next week. Apart from the positions of songs, a list contains information about change of positions of all songs with regard to their last week’s positions. More precisely, each song is given a mark indicating whether that song stayed at same position, gained or lost popularity since last week.</p>

<p>Write a program that will using given popularity list help Michael to determine one possible last week’s popularity list.</p>

### 입력 

 <p>The first line of input file contains an integer N, 1 ≤ N ≤ 100, number of songs on popularity list.</p>

<p>Next N blocks describe a popularity list. A block consists of two lines. First line of ith block contains name of ith song. A name of a song consists of at most 100 uppercase letters of English alphabet. Second line of a block contains one of three words: UP (a song went up on a list), DOWN (a song went down on a list) or SAME (position stayed the same), describing a change on a list with respect to last week’s list.</p>

### 출력 

 <p>The output file contains one possible popularity list from last week in N lines.</p>

<p>Each line should contain name of a song so that ith line contains name of ith song on a list.</p>

<p>Note: A solution needs not to be unique, but there always will be at least one solution for each test data.</p>

