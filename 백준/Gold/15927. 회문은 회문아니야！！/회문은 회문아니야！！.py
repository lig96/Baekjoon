s = input()

if s == s[0]*len(s):
    print(-1)
elif s != s[::-1]:
    print(len(s))
else:
    print(len(s)-1)
