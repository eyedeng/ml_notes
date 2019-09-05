import numpy as np
import time
import os

N = 20
cell_map = np.zeros((N, N), np.int)
cell_map_next = np.zeros((N, N), np.int)


def print_map(m):
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def init_map(case):
    if case == 0:
        cell_map[:, :] = np.random.randint(0, 2, (N, N), np.int)
    elif case == 1:
        cell_map[10:15, 10:15] = np.array([[0, 0, 0, 0, 0],
                                           [0, 0, 1, 0, 0],
                                           [0, 0, 1, 0, 0],
                                           [0, 0, 1, 0, 0],
                                           [0, 0, 0, 0, 0]], np.int)
    elif case == 2:
        cell_map[2:5, 2:5] = np.array([[1, 0, 0],
                                       [0, 1, 1],
                                       [1, 1, 0]], np.int)


def change(x, y):
    dir_ = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
            [0, 1], [1, -1], [1, 0], [1, 1]]
    cnt = 0
    for i in range(8):
        next_x, next_y = x + dir_[i][0], y + dir_[i][1]
        # if next_x>=0 and next_x<N and next_y>=0 and next_y<N:
        if next_x in range(0, N) and next_y in range(0, N):
            if cell_map[next_x][next_y] == 1:
                cnt += 1
    if cnt < 2:
        cell_map_next[x][y] = 0
    elif cnt == 2:
        cell_map_next[x][y] = cell_map[x][y]
    elif cnt == 3:
        cell_map_next[x][y] = 1
    else:
        cell_map_next[x][y] = 0


T = 50
init_map(0)
print_map(cell_map)
while T > 0:
    for i in range(N):
        for j in range(N):
            change(i, j)
    print_map(cell_map_next)
    cell_map = cell_map_next.copy()  # 非引用
    time.sleep(0.2)
    if T != 1:
        os.system('cls')
    T -= 1
