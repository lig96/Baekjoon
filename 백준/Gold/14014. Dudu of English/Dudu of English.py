import re


def sol(s):
    #
    s = s.lower()
    #
    s = s.split()  # 여기서 \n 사라짐
    of_words = ['of', 'to', 'into',
                'onto', 'above', 'below',
                'from', 'by', 'is', 'at']
    s = [word if word not in of_words else 'of' for word in s]
    #
    new_s = []
    for word in s:
        K = len(re.findall('a|e|i|o|u', word))
        if K >= 2:
            word = re.sub('a|e|i|o|u', '', word, count=K//2)
        new_s.append(word)
    s = new_s
    #
    s = ' '.join(s)
    s = re.sub('[^a-z \n]', '', s)
    #
    s = re.sub('\n', ' ', s)  # 불필요함
    #
    s = re.sub(' +', ' ', s)
    #
    s = s.split()
    chars, len_chars = '', 0
    for word in s:
        chars += word+' '
        len_chars += len(word)
        if len_chars > 20:
            print(chars)
            chars, len_chars = '', 0
    else:
        print(chars)
        chars, len_chars = '', 0


N = int(input())
s = [input() for _ in range(N)]
s = '\n'.join(s)
sol(s)
