def to_num(chars: str) -> int:
    if len(chars) == 1:
        # 0인 경우는 없음
        return dic[chars[0]]

    ans = 0
    i = 0
    while i <= len(chars)-2:  # len(chars) >= 2
        now, after = dic[chars[i]], dic[chars[i+1]]
        if now >= after:
            ans += now
            i += 1
        else:
            ans += -now+after
            i += 2
    else:
        # 마지막을 확인해야 함.
        now, after = dic[chars[-2]], dic[chars[-1]]
        if now >= after:
            ans += after
    return ans


def to_char(nums: int) -> str:
    ans = ''
    for char in keys:
        while nums >= dic[char]:
            nums -= dic[char]
            ans += char
    return ans


T = int(input())
strings = [input() for _ in range(T)]


dic = dict()
keys = ['M', 'CM', 'D', 'CD',
        'C', 'XC', 'L', 'XL',
        'X', 'IX', 'V', 'IV',
        'I']
values = [1000, 900, 500, 400,
          100, 90, 50, 40,
          10, 9, 5, 4,
          1]
for i in range(len(keys)):
    dic[keys[i]] = values[i]


for string in strings:
    if string.isdecimal():
        print(to_char(int(string)))
    else:
        print(to_num(string))
