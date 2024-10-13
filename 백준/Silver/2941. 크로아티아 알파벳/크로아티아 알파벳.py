import sys
input = sys.stdin.readline
sys_print = sys.stdout.write


def check(stack, stack_check):
    if ''.join(stack[-len(stack_check):]) == stack_check:
        return True
    else:
        return False


def do(stack, stack_check):
    for _ in range(len(stack_check)):
        stack.pop()
    stack.append(stack_check)
    return


chars = input().rstrip()


stack = []


for char in chars:
    stack.append(char)
    for stack_check in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
        if check(stack, stack_check):
            do(stack, stack_check)


print(len(stack))
