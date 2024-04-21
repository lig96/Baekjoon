import sys
input = sys.stdin.readline


class Player():
    def __init__(self, player_loc, boss_loc):
        self.now_HP, self.max_HP, self.attack, self.defence = (
            20, 20, 2, 2)
        self.level, self.exp = 1, 0
        #
        self.weapon = 0
        self.armor = 0
        self.ornaments = {'count': 0,
                          'HR': False, 'RE': False,
                          'CO': False, 'EX': False,
                          'DX': False, 'HU': False,
                          'CU': False}
       #
        self.r, self.c = player_loc
        self.first_r, self.first_c = player_loc
        self.boss_r, self.boss_c = boss_loc
        self.dr = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
        self.dc = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
        self.is_game_end = False
        self.outcome = None
        return

    def print_status(self):
        print(f'LV : {player.level}')
        print(f'HP : {max(player.now_HP, 0)}/{player.max_HP}')
        print(f'ATT : {player.attack}+{player.weapon}')
        print(f'DEF : {player.defence}+{player.armor}')
        print(f'EXP : {player.exp}/{player.level*5}')
        print(f'{player.outcome}')
        return

    def print_grid(self):
        if self.now_HP > 0:
            grid[self.r][self.c] = '@'
        for r in range(N):
            print(''.join(grid[r]))
        return

    def act(self, command):
        newr, newc = self.r+self.dr[command], self.c+self.dc[command]
        if not (0 <= newr < N and 0 <= newc < M):
            enemy = self.trap_check()  # 제자리에서 가시 체크
        elif (temp := grid[newr][newc]) == '#':
            enemy = self.trap_check()  # 제자리에서 가시 체크
        elif temp == '.':
            self.move(newr, newc)
        elif temp == 'B':
            self.open_box(newr, newc)
            self.move(newr, newc)
        elif temp == '^':
            self.move(newr, newc)
            enemy = self.trap_check()  # 이동 후 가시 체크
        elif temp == '&' or temp == 'M':
            win_or_lose, enemy = self.battle(newr, newc, temp == 'M')
            if win_or_lose == 'win' and self.ornaments['HR']:
                self.now_HP = min(self.now_HP+3, self.max_HP)
        else:
            raise Exception('다른 경우의 수가 존재함')

        # 다 끝난 뒤에 종료 여부 확인
        if self.now_HP <= 0:
            if self.ornaments['RE']:
                self.now_HP = self.max_HP
                self.move(self.first_r, self.first_c)
                self.ornaments['RE'] = False
                self.ornaments['count'] -= 1
            else:
                self.is_game_end = True
                self.outcome = f'YOU HAVE BEEN KILLED BY {enemy}..'
        elif grid[self.boss_r][self.boss_c] == '.':
            # 보스를 죽여서 '.'으로 대체됐으면
            self.is_game_end = True
            self.outcome = f'YOU WIN!'

    def move(self, newr, newc):
        self.r, self.c = newr, newc
        return

    def trap_check(self):
        r, c = self.r, self.c
        if grid[r][c] == '^':
            self.now_HP -= (1 if self.ornaments['DX'] else 5)
            enemy = 'SPIKE TRAP'
        else:
            enemy = None
        return enemy

    def open_box(self, r, c):
        a, b = boxes[r][c]
        if a == 'W':
            self.weapon = b
        elif a == 'A':
            self.armor = b
        else:
            if self.ornaments['count'] < 4 and not self.ornaments[b]:
                self.ornaments[b] = True
                self.ornaments['count'] += 1

        grid[r][c] = '.'
        boxes[r][c] = None
        return

    def battle(self, r, c, is_boss):
        name, attack, defence, now_HP, exp = monsters[r][c]
        # self가 안 붙은 건 몬스터의 성질

        if is_boss and self.ornaments['HU']:
            self.now_HP = self.max_HP

        turn = 0
        while True:
            if turn % 2 == 0:
                # 플레이어 공격. 선공.
                now_HP -= max(1, self.total_attack(turn) - defence)
            else:
                # 몬스터 공격
                if is_boss and self.ornaments['HU'] and turn == 1:
                    self.now_HP -= 0
                else:
                    self.now_HP -= max(1, attack - self.total_defence())

            if now_HP <= 0:
                flag = 'win'
                break
            elif self.now_HP <= 0:
                flag = 'lose'
                break
            else:
                turn += 1

        if flag == 'win':
            grid[r][c] = '.'
            monsters[r][c] = None
            self.move(r, c)
            self.exp_update(exp)

        return (flag, name)

    def total_attack(self, turn):
        temp = self.attack + self.weapon
        if not self.ornaments['CO'] or turn != 0:
            return temp
        else:
            if self.ornaments['DX']:
                return 3*temp
            else:
                return 2*temp

    def total_defence(self):
        return self.defence + self.armor

    def exp_update(self, exp):
        self.exp += exp + int(exp*0.2*self.ornaments['EX'])
        if self.level * 5 <= self.exp:
            self.max_HP += 5
            self.attack += 2
            self.defence += 2
            self.now_HP = self.max_HP
            self.level, self.exp = self.level+1, 0
        return


# 그리드 정보 입력 받기
N, M = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(N)]
S = list(input().rstrip())
# 몬스터 정보 입력 받기
K = 1 + sum(1 for r in range(N) for c in range(M)
            if grid[r][c] == '&')  # 1은 보스몬스터
monsters = [[None for _ in range(M)] for _ in range(N)]
for _ in range(K):
    temp = input().rstrip().split()
    for i in range(7):
        try:
            temp[i] = int(temp[i])
        except ValueError:
            pass
    monsters[temp[0]-1][temp[1]-1] = temp[2:]
    # monsters[R][C] = [이름, 공격력, 방어력, 최대체력, 경험치]
# 아이템 상자 정보 입력 받기
L = sum(1 for r in range(N) for c in range(M)
        if grid[r][c] == 'B')
boxes = [[None for _ in range(M)] for _ in range(N)]
for _ in range(L):
    temp = input().rstrip().split()
    for i in range(4):
        try:
            temp[i] = int(temp[i])
        except ValueError:
            pass
    boxes[temp[0]-1][temp[1]-1] = temp[2:]
    # boxes[R][C] = [종류, 내용]
# 기타 정보 추출하기
player_loc = [(r, c) for r in range(N) for c in range(M)
              if grid[r][c] == '@'][0]
boss_loc = [(r, c) for r in range(N) for c in range(M)
            if grid[r][c] == 'M'][0]
grid[player_loc[0]][player_loc[1]] = '.'  # 초기화


player = Player(player_loc, boss_loc)
for turn, command in enumerate(S, start=1):
    player.act(command)
    if player.is_game_end:
        player.print_grid()
        print(f'Passed Turns : {turn}')
        player.print_status()
        break
else:
    # 입력이 break 없이 끝났을 경우
    player.outcome = 'Press any key to continue.'

    player.print_grid()
    print(f'Passed Turns : {turn}')
    player.print_status()
