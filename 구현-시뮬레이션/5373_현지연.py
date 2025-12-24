# 큐빙
# https://www.acmicpc.net/problem/5373

import sys
from copy import deepcopy
input = sys.stdin.readline

def rotate_clockwise(a):
    a[0][0], a[0][1], a[0][2], a[1][2], a[2][2], a[2][1], a[2][0], a[1][0] = \
    a[2][0], a[1][0], a[0][0], a[0][1], a[0][2], a[1][2], a[2][2], a[2][1]

def rotate_counterclockwise(a):
    a[0][0], a[0][1], a[0][2], a[1][2], a[2][2], a[2][1], a[2][0], a[1][0] = \
    a[0][2], a[1][2], a[2][2], a[2][1], a[2][0], a[1][0], a[0][0], a[0][1]

def init_cube():
    return [
        [['w'] * 3 for _ in range(3)],  # 0: U
        [['r'] * 3 for _ in range(3)],  # 1: F
        [['b'] * 3 for _ in range(3)],  # 2: R
        [['o'] * 3 for _ in range(3)],  # 3: B
        [['g'] * 3 for _ in range(3)],  # 4: L
        [['y'] * 3 for _ in range(3)],  # 5: D
    ]

n = int(input())
for _ in range(n):
    m = int(input())
    methods = input().split()

    cube = init_cube()

    for method in methods:
        if method == "U+":
            rotate_clockwise(cube[0])
            temp = cube[1][0][:]
            cube[1][0] = cube[2][0][:]
            cube[2][0] = cube[3][0][:]
            cube[3][0] = cube[4][0][:]
            cube[4][0] = temp

        elif method == "U-":
            rotate_counterclockwise(cube[0])
            temp = cube[1][0][:]
            cube[1][0] = cube[4][0][:]
            cube[4][0] = cube[3][0][:]
            cube[3][0] = cube[2][0][:]
            cube[2][0] = temp
        
        elif method == "D+":
            rotate_clockwise(cube[5])
            temp = cube[1][2][:]          # F bottom
            cube[1][2] = cube[4][2][:]    # F ← L
            cube[4][2] = cube[3][2][:]    # L ← B
            cube[3][2] = cube[2][2][:]    # B ← R
            cube[2][2] = temp             # R ← F

        elif method == "D-":
            rotate_counterclockwise(cube[5])
            temp = cube[1][2][:]          # F bottom
            cube[1][2] = cube[2][2][:]    # F ← R
            cube[2][2] = cube[3][2][:]    # R ← B
            cube[3][2] = cube[4][2][:]    # B ← L
            cube[4][2] = temp             # L ← F
        
        elif method == "F+":
            rotate_clockwise(cube[1])
            temp = cube[0][2][:]
            cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[4][2][2], cube[4][1][2], cube[4][0][2]
            cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[5][0][0], cube[5][0][1], cube[5][0][2]
            cube[5][0][0], cube[5][0][1], cube[5][0][2] = cube[2][2][0], cube[2][1][0], cube[2][0][0]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = temp

        elif method == "F-":
            rotate_counterclockwise(cube[1])
            temp = [cube[0][2][2], cube[0][2][1], cube[0][2][0]]
            cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[5][0][2], cube[5][0][1], cube[5][0][0]
            cube[5][0][0], cube[5][0][1], cube[5][0][2] = cube[4][0][2], cube[4][1][2], cube[4][2][2]
            cube[4][0][2], cube[4][1][2], cube[4][2][2] = temp

        elif method == "R+":
            rotate_clockwise(cube[2])
            temp = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
            cube[3][0][0], cube[3][1][0], cube[3][2][0] = cube[0][2][2], cube[0][1][2], cube[0][0][2]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = temp
            
        elif method == "R-":
            rotate_counterclockwise(cube[2])
            temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
            cube[3][0][0], cube[3][1][0], cube[3][2][0] = cube[5][2][2], cube[5][1][2],cube[5][0][2]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = temp
                
        elif method == "B+":
            rotate_clockwise(cube[3])
            temp = [cube[2][0][2], cube[2][1][2], cube[2][2][2]]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[5][2][2], cube[5][2][1], cube[5][2][0]
            cube[5][2][0], cube[5][2][1], cube[5][2][2] = cube[4][0][0], cube[4][1][0], cube[4][2][0]
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[0][0][2], cube[0][0][1], cube[0][0][0]
            cube[0][0][0], cube[0][0][1], cube[0][0][2] = temp

        elif method == "B-":
            rotate_counterclockwise(cube[3])
            temp = cube[0][0][:]
            cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[5][2][0], cube[5][2][1], cube[5][2][2]
            cube[5][2][0], cube[5][2][1], cube[5][2][2] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp
            
        elif method == "L+":
            rotate_clockwise(cube[4])
            temp = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[0][0][0], cube[0][1][0], cube[0][2][0]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
            cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = temp
            
        elif method == "L-":
            rotate_counterclockwise(cube[4])
            temp = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0]
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
            cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[0][2][0], cube[0][1][0], cube[0][0][0]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = temp

        print(method)
        print(*cube[0][0], sep='')
        print(*cube[0][1], sep='')
        print(*cube[0][2], sep='')

    print(*cube[0][0], sep='')
    print(*cube[0][1], sep='')
    print(*cube[0][2], sep='')




### 도전 1. 시간초과된 코드
#     import sys
# from copy import deepcopy
# input = sys.stdin.readline

# def rotate_clockwise(graph):
#     rotated = [[0] * 3 for _ in range(3)]
#     for i in range(3):
#         for j in range(3):
#             rotated[j][2-i] = graph[i][j]
#     return rotated

# def rotate_counterclockwise(graph):
#     rotated = [[0] * 3 for _ in range(3)]
#     for i in range(3):
#         for j in range(3):
#             rotated[2-j][i] = graph[i][j]
#     return rotated

# origin_cube = [[['w', 'w', 'w'],
#          ['w', 'w', 'w'],
#          ['w', 'w', 'w'],],
#          [['r', 'r', 'r'],
#          ['r', 'r', 'r'],
#          ['r', 'r', 'r'],],
#          [['b', 'b', 'b'],
#          ['b', 'b', 'b'],
#          ['b', 'b', 'b'],],
#          [['o', 'o', 'o'],
#          ['o', 'o', 'o'],
#          ['o', 'o', 'o'],],
#          [['g', 'g', 'g'],
#          ['g', 'g', 'g'],
#          ['g', 'g', 'g'],],
#          [['y', 'y', 'y'],
#          ['y', 'y', 'y'],
#          ['y', 'y', 'y'],]]

# n = int(input())
# for _ in range(n):
#     m = int(input())
#     methods = input().split()
#     cube = deepcopy(origin_cube)

#     for method in methods:
#         if method == "U+":
#             cube[0] = rotate_clockwise(cube[0])
#             cube[1][0], cube[2][0], cube[3][0], cube[4][0] = cube[2][0], cube[3][0], cube[4][0], cube[1][0]
#         elif method == "U-":
#             cube[0] = rotate_counterclockwise(cube[0])
#             cube[1][0], cube[2][0], cube[3][0], cube[4][0] = cube[4][0], cube[1][0], cube[2][0], cube[3][0]
#         elif method == "D+":
#             cube[5] = rotate_clockwise(cube[5])
#             cube[1][2], cube[2][2], cube[3][2], cube[4][2] = cube[4][2], cube[1][2], cube[2][2], cube[3][2]
#         elif method == "D-":
#             cube[5] = rotate_counterclockwise(cube[5])
#             cube[1][2], cube[2][2], cube[3][2], cube[4][2] = cube[2][2], cube[3][2], cube[4][2], cube[1][2]
#         elif method == "F+":
#             cube[1] = rotate_clockwise(cube[1])

#             bottom_0 = deepcopy(cube[0][2])
#             left_2 = [cube[2][i][0] for i in range(3)]
#             top_5 = deepcopy(cube[5][0])
#             right_4 = [cube[4][i][2] for i in range(3)]

#             cube[0][2] = right_4[::-1]
#             cube[5][0] = left_2[::-1]
#             for i in range(3):
#                 cube[2][i][0] = bottom_0[i]
#                 cube[4][i][2] = top_5[i]


#         elif method == "F-":
#             cube[1] = rotate_counterclockwise(cube[1])

#             bottom_0 = deepcopy(cube[0][2])
#             left_2 = [cube[2][i][0] for i in range(3)]
#             top_5 = deepcopy(cube[5][0])
#             right_4 = [cube[4][i][2] for i in range(3)]

#             cube[0][2] = left_2[::-1]
#             cube[5][0] = right_4[::-1]
#             for i in range(3):
#                 cube[2][i][0] = top_5[i]
#                 cube[4][i][2] = bottom_0[i]
                

#         elif method == "R+":
#             cube[2] = rotate_clockwise(cube[2])

#             right_0 = [cube[0][i][2] for i in range(3)]
#             left_3 = [cube[3][i][0] for i in range(3)]
#             right_5 = [cube[5][i][2] for i in range(3)]
#             right_1 = [cube[1][i][2] for i in range(3)]

#             for i in range(3):
#                 cube[0][i][2] = right_1[i]
#                 cube[1][i][2] = right_5[i]
#                 cube[5][i][2] = left_3[-i-1]
#                 cube[3][i][0] = right_0[-i-1]
            
#         elif method == "R-":
#             cube[2] = rotate_counterclockwise(cube[2])

#             right_0 = [cube[0][i][2] for i in range(3)]
#             left_3 = [cube[3][i][0] for i in range(3)]
#             right_5 = [cube[5][i][2] for i in range(3)]
#             right_1 = [cube[1][i][2] for i in range(3)]

#             for i in range(3):
#                 cube[0][i][2] = left_3[-i-1]
#                 cube[1][i][2] = right_0
#                 cube[5][i][2] = right_1
#                 cube[3][i][0] = right_5[-i-1]


#         elif method == "B+":
#             cube[3] = rotate_clockwise(cube[3])

#             right_2 = [cube[2][i][2] for i in range(3)]
#             top_0 = deepcopy(cube[0][0])
#             left_4 = [cube[4][i][0] for i in range(3)]
#             bottom_5 = deepcopy(cube[5][2])

#             cube[0][0] = right_2
#             cube[5][2] = left_4
#             for i in range(3):
#                 cube[2][i][2] = bottom_5[::-1][i]
#                 cube[4][i][0] = top_0[::-1][i]

#         elif method == "B-":
#             cube[3] = rotate_counterclockwise(cube[3])

#             right_2 = [cube[2][i][2] for i in range(3)]
#             top_0 = deepcopy(cube[0][0])
#             left_4 = [cube[4][i][0] for i in range(3)]
#             bottom_5 = deepcopy(cube[5][2])

#             cube[0][0] = left_4[::-1]
#             cube[5][2] = right_2[::-1]
#             for i in range(3):
#                 cube[2][i][2] = top_0[i]
#                 cube[4][i][0] = bottom_5[i]


#         elif method == "L+":
#             cube[4] = rotate_clockwise(cube[4])

#             left_1 = [cube[1][i][0] for i in range(3)]
#             left_5 = [cube[5][i][0] for i in range(3)]
#             right_3 = [cube[3][i][2] for i in range(3)]
#             left_0 = [cube[0][i][0] for i in range(3)]

#             for i in range(3):
#                 cube[1][i][0] = left_0[i]
#                 cube[5][i][0] = left_1[i]
#                 cube[3][i][2] = left_5[::-1][i]
#                 cube[0][i][0] = right_3[::-1][i]

#         elif method == "L-":
#             cube[4] = rotate_counterclockwise(cube[4])
        
#             left_1 = [cube[1][i][0] for i in range(3)]
#             left_5 = [cube[5][i][0] for i in range(3)]
#             right_3 = [cube[3][i][2] for i in range(3)]
#             left_0 = [cube[0][i][0] for i in range(3)]

#             for i in range(3):
#                 cube[1][i][0] = left_5[i]
#                 cube[5][i][0] = right_3[::-1][i]
#                 cube[3][i][2] = left_0[::-1][i]
#                 cube[0][i][0] = left_1[i]

#     print(*cube[0][0], sep='')
#     print(*cube[0][1], sep='')
#     print(*cube[0][2], sep='')