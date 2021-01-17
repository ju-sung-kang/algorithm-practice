# [["  ","북","  "],   다음과 같이 배열에 주사위에 적힌 숫자를 저장해 둘 것이다
#  ["서","상","동"],
#  ["  ","남","  "],
#  ["  ","하","  "]]


def east():
    global arr
    tmp = arr[1][1]
    arr[1][1] = arr[1][0]
    arr[1][0] = arr[3][1]
    arr[3][1] = arr[1][2]
    arr[1][2] = tmp


def west():
    global arr
    tmp = arr[1][1]
    arr[1][1] = arr[1][2]
    arr[1][2] = arr[3][1]
    arr[3][1] = arr[1][0]
    arr[1][0] = tmp


def north():
    global arr
    tmp = arr[1][1]
    arr[1][1] = arr[2][1]
    arr[2][1] = arr[3][1]
    arr[3][1] = arr[0][1]
    arr[0][1] = tmp


def south():
    global arr
    tmp = arr[1][1]
    arr[1][1] = arr[0][1]
    arr[0][1] = arr[3][1]
    arr[3][1] = arr[2][1]
    arr[2][1] = tmp


def overlap():  # 주사위 밑면과 map이 만났을때 수정
    global dice_map
    global arr

    if dice_map[r][c] == 0:
        dice_map[r][c] = arr[3][1]
    else:
        arr[3][1] = dice_map[r][c]
        dice_map[r][c] = 0


arr = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]
n, m, r, c, k = map(int, input().split())

dice_map = []
command = []

for i in range(n):
    dice_map.append(list(map(int, input().split())))

command = list(map(int, input().split()))

for i in range(k):
    if command[i] == 1:
        if c != m-1:
            c += 1
            east()
            print(arr[1][1])
            overlap()

    elif command[i] == 2:
        if c != 0:
            c -= 1
            west()
            print(arr[1][1])
            overlap()

    elif command[i] == 3:
        if r != 0:
            r -= 1
            north()
            print(arr[1][1])
            overlap()

    else:  # command[i] == 4
        if r != n-1:
            r += 1
            south()
            print(arr[1][1])
            overlap()
