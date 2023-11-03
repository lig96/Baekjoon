# [Silver I] LaTeX Expert - 19818 

[문제 링크](https://www.acmicpc.net/problem/19818) 

### 성능 요약

메모리: 34788 KB, 시간: 120 ms

### 분류

구현, 파싱, 정규 표현식, 문자열

### 제출 일자

2023년 11월 4일 04:48:30

### 문제 설명

<p>Regina is finishing her graduation work. She asks Grigory who is LaTeX expert to help her with layout.</p>

<p>Making layout is easy for Grigory, but he has some problems with bibliography rendering. Due to graduation work design requirements, references in bibliography must be placed in the same order as they are placed in the text of the work. Each reference has exactly one occurrence in Regina's work.</p>

<p>For placing reference on some source Grigory uses <code>\cite{<reference>}</code> construction, where <code><reference></code> is the name of the reference. An example of a text that contains three references is shown below.</p>

<pre>The most famous characters of Pushkin's works are Onegin \cite{onegin},
Dubrovsky \cite{dubrovsky} and Tsar Saltan \cite{saltan}.</pre>

<p>To make the bibliography, Grigory needs to place the following construction after the text of the work:</p>

<pre>\begin{thebibliography}{99}
\bibitem{onegin} A.S.Pushkin. Eugene Onegin. 1831.
\bibitem{dubrovsky} A.S.Pushkin. Dubrovsky. 1841.
\bibitem{saltan} A.S.Pushkin. The Tale of Tsar Saltan. 1832.
\end{thebibliography}
</pre>

<p>Here <code>99</code> is the maximal number of references and reference description is written after <code>\bibitem{<reference>}</code> construction.</p>

<p>Text is quite large and Grigory is quite lazy, so he doesn't want to check the order of references. Therefore he asks you to write a program that can analyze the text and the bibliography. If the bibliography is incorrect, your program must print the correct new one.</p>

### 입력 

 <p>Input contains the text of the work that consists of lowercase and uppercase English letters, ends of lines, spaces, <<<code>.</code>>>, <<<code>,</code>>>, <<<code>'</code>>> (ASCII code 39) characters and <code>\cite{<reference>}</code> constructions. Here <code><reference></code> is a nonempty string of lowercase English letters that has the length at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>. ASCII code of <<<code>\textbackslash</code>>> character is 92.</p>

<p>Each <code>\cite{<reference>}</code> construction starts at a new line or after a space character. The text of the work can contain empty lines.</p>

<p>The following line after the text is equal to <code>\begin{thebibliography}{99}</code>. Each of the following lines contains a description of a source in the described format. Description consists of the same characters as the text of work. Length of each description isn't greater than <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container> characters. The following line after the bibliography is <code>\end{thebibliography}{99}</code>.</p>

<p>It's guaranteed that:</p>

<ul>
	<li>The total number of references is not greater than 99.</li>
	<li>There is at least one reference in the text.</li>
	<li>If the text contains some reference, the bibliography contains that reference too.</li>
	<li>The number of <code>\cite{<reference>}</code> constructions in the text is the same as the number of <code>\bibitem{<reference>}</code> constructions in the bibliography.</li>
	<li>The references in the text are different.</li>
	<li>The total number of lines in the input isn't greater than <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>5</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^5$</span></mjx-container>.</li>
	<li>The sum of lengths of the lines in the text isn't greater than <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>5</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^5$</span></mjx-container>.</li>
	<li>Input doesn't contain two consecutive space characters. The first and the last characters of each line aren't spaces.</li>
</ul>

### 출력 

 <p>Print <code>Correct</code> if the bibliography from the input is correct and <code>Incorrect</code> otherwise.</p>

<p>In the second case print the correct bibliography in the required format then. The source descriptions must be the same as defined in input.</p>

