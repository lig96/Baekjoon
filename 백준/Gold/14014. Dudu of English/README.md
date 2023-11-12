# [Gold V] Dudu of English - 14014 

[문제 링크](https://www.acmicpc.net/problem/14014) 

### 성능 요약

메모리: 34848 KB, 시간: 112 ms

### 분류

구현, 파싱, 정규 표현식, 문자열

### 제출 일자

2023년 11월 12일 16:13:33

### 문제 설명

<p><strong>"your uf of library have bugs"</strong> -- Dudu, 2015</p>

<p>Dudu realized that English is a very inefficient language. To address this issue he created his own dialect: <strong>dudu of english</strong>. Here are a couple of examples:</p>

<ul>
	<li>From "The <a href="https://www.hackerrank.com/external_redirect?to=https://en.wikipedia.org/wiki/Disjoint-set_data_structure" target="_blank">Union-Find</a> in your library has bugs!" to "yur uf of lbrary hve bugs"</li>
	<li>From "My professor is funny sometimes." to "prfessor of funny smtimes"</li>
</ul>

<p>Your job is to write the first translator from English to dudu of english, using the following rules:</p>

<ul>
	<li>All capital letters should be "decapitalized." dudu of english speakers are humble.</li>
	<li>Prepositions are overrated, and Dudu has realized that certain words are pretty much equivalent. They are called <strong>of-words</strong>, and should be translated simply to "of." A list of of-words will be given below.</li>
	<li>For Dudu, vowels don't improve readability. If a word has K vowels, you should remove the first K/2 of them, rounded down. Dudu considers <strong>a</strong>, <strong>e</strong>, <strong>i</strong>, <strong>o</strong>, and <strong>u</strong> to be vowels.</li>
	<li>All punctuation should be removed. Who likes commas anyway?</li>
	<li>All line breaks should be removed from the initial input, and replaced with spaces.</li>
	<li>Any sequence of spaces in the input should be condensed to a single space. Dudu is not wasteful.</li>
	<li>Dudu prefers to read only short lines, but he doesn't like breaking words either. As you print the output, if a word causes the current line to exceed 20 characters in length (not including spaces), put a line break after it.</li>
</ul>

<p>The rules should be applied in the order specified above. Don't print any leading spaces (spaces at the beginning of a line).</p>

<p><strong>of-words</strong> are: of, to, into, onto, above, below, from, by, is, at.</p>

<p>Dudu considers any character that isn't a lowercase or uppercase letter, a space, or a line break to be punctuation.</p>

### 입력 

 <p>The input will start with an integer N indicating the number of lines to be translated.</p>

<p>The next N lines will contain the text to be translated.</p>

<ul>
	<li>1 ≤ N ≤ 50</li>
</ul>

<p>The total length of the text to be translated won't exceed 5000 characters.</p>

### 출력 

 <p>utput the text of the nput<br>
trnslated of ddu of nglish</p>

