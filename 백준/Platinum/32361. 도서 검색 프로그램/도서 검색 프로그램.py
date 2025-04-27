# 전위표기식의 계산은 뒤집어서 후위표기식처럼 스택을 쓰면 된다.


import sys
input = sys.stdin.readline
sys_print = sys.stdout.write
# sys.setrecursionlimit(1500*2)


def make_long_input(N_size=200, M_size=200, search_size=1450):
    '''
    재귀적으로 methods를 처리하는 코드를 저격하는 케이스를 만듭니다.
    A(A(A(A(A(A(A(A(a:Z), t:Z), t:Z), t:Z), t:Z), t:Z),
    형태입니다.
    '''
    def rec(t, text, search_size):
        if len(text) > search_size:
            return text
        text = 'A(' + text + ')' + f', {t}'
        return rec(t, text, search_size)

    print(N_size)
    for i in range(N_size):
        long_input_n = f'n{i} a{i}'
        j = 0
        while len(long_input_n) < 190:
            long_input_n = long_input_n + str(j)
            j += 1
        if len(long_input_n) > 200:
            raise Exception
        print(long_input_n)

    print(M_size)
    long_input_m = rec('a:Z', '', search_size)
    if len(long_input_m) > 1500:
        raise Exception
    for _ in range(M_size):
        print(long_input_m)
    return


def do_search(search: str, books: list[list[str, set]]) -> int:
    return sum(all(do_methods(search, book)) for book in books)


def do_methods(methods: str, book: list[str, set]) -> list[bool]:
    stack = []
    str_stack = []
    prev_char = None
    for char in reversed(methods):
        if prev_char == "(":
            # assert char in "AON"
            # (의 왼쪽이라면 A, O, N임.
            temp = []
            stack.pop()  # 범위의 시작인 여는 괄호 없앰.
            while stack[-1] != ")":
                temp.append(stack.pop())
            stack.pop()  # 범위의 끝인 닫는 괄호 없앰.
            # 이 시점에서 temp는 A, O, N 뒤에 오는 <methods>, <method>임.
            if char == "A":
                temp2 = all(temp)
            elif char == "O":
                temp2 = any(temp)
            elif char == "N":
                # assert len(temp) == 1
                temp2 = not temp[0]
            else:
                raise Exception
            stack.append(temp2)
        elif prev_char == ":":
            # assert char in "niat"
            # <nameInclude>를 "i:" <str>로 바꾼 것에 유의.
            str_ = stack.pop()
            if char == "n":
                temp = (str_ == book[0])
            elif char == "i":
                temp = (str_ in book[0])
            elif char == "a":
                temp = (str_ == book[1])
            elif char == "t":
                temp = (str_ in book[2])
            else:
                raise Exception
            stack.append(temp)
        else:
            if char == ")":
                stack.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ":":
                # iff, :의 오른쪽에 str가 있음.
                stack.append("".join(reversed(str_stack)))
                str_stack = []
            elif char == " ":
                pass
            elif char.isalnum() or char == "-" or char == "_":
                str_stack.append(char)
            elif char == ",":
                pass
            else:
                raise Exception
        prev_char = char
    return stack


N = int(input())
books = []
for _ in range(N):
    book = input().split()
    books.append([book[0], book[1], set(book[2:])])
M = int(input())
searches = [input().rstrip().replace("ni:", "i:") for _ in range(M)]
# 파싱 편의를 위해 ni:를 i:로 바꿔서 글자수를 통일시킴.


for search in searches:
    ans = do_search(search, books)
    sys_print(str(ans)+'\n')
