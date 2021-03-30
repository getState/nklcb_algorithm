"""
문제 설명
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

U: 위쪽으로 한 칸 가기

D: 아래쪽으로 한 칸 가기

R: 오른쪽으로 한 칸 가기

L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.

이때, 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다. 예를 들어 위의 예시에서 게임 캐릭터가 움직인 길이는 9이지만, 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다.
(8, 9번 명령어에서 움직인 길은 2, 3번 명령어에서 이미 거쳐 간 길입니다)

단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.

"""



dnX = [-1, 1, 0, 0]
dnY = [0, 0, 1, -1]

def get_direction(direction):
    if direction == 'U':
        return 0
    elif direction == 'D':
        return 1
    elif direction == 'R':
        return 2
    elif direction == 'L':
        return 3
    else:
        print("error")

def solution(dirs):
    #11*11*11*11 배열
    arr = [[[[False] *11 for _ in range(11) ] for _ in range(11)] for _ in range(11)]
    answer = 0
    now = [5, 5]
    for direction in dirs:
        direct = get_direction(direction)
        print(now)
        nowX = now[0]
        nowY = now[1]
        nextX = nowX+dnX[direct]
        nextY = nowY+dnY[direct]
        if nextX<0 or nextX>10 or nextY<0 or nextY>10 :
            continue
        if arr[nowX][nowY][nextX][nextY] == False and arr[nextX][nextY][nowX][nowY] == False:
            answer += 1
        arr[nowX][nowY][nextX][nextY] = True
        arr[nextX][nextY][nowX][nowY] = True
        now = [nextX, nextY]
        
    
    return answer