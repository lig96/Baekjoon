# [Silver I] Meow Factor 2 - 17896 

[문제 링크](https://www.acmicpc.net/problem/17896) 

### 성능 요약

메모리: 116492 KB, 시간: 224 ms

### 분류

많은 조건 분기, 정규 표현식, 문자열

### 제출 일자

2023년 11월 5일 06:28:13

### 문제 설명

<p>Strings of yarn have been popular in Catland for ages. Which cat has not spent many a lazy afternoon bouncing around a ball of yarn? Lately however, strings of yarn have gotten competition: strings of characters. It turns out that these are almost as much fun as yarn, and generally much safer as well (so far, no cat has had to call 911 on account of any character string-related entanglement accidents).</p>

<p>Naturally, some strings are more stylish than others, and for cool cats it is important to engage in their string-playing pastime with style. The meow factor of a string S is the minimum number of operations needed to transform S into a string S 0 which contains the word “meow” as a substring, where an operation is one of the following four:</p>

<ol>
	<li>Insert an arbitrary character anywhere into the string.</li>
	<li>Delete an arbitrary character anywhere from the string.</li>
	<li>Replace any character in the string by an arbitrary character.</li>
	<li>Swap any two adjacent characters in the string.</li>
</ol>

<p>Write a program to compute the meow factor of a string of characters.</p>

### 입력 

 <p>The input consists of a single line containing a string S, consisting only of lower-case letters ‘a’-‘z’. The length of S is at least 1 and at most 10<sup>6</sup>.</p>

### 출력 

 <p>Output the meow factor of S.</p>

