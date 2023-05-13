#! /usr/bin/python
# -*- coding: utf-8 -*-

# witten by chat gpt

import pygame
import numpy as np

# ボードのサイズ
BOARD_SIZE = WIDTH, HEIGHT = 640, 480

# セルのサイズ
CELL_SIZE = 10

# セルの色
ALIVE_COLOR = (255, 255, 255)
DEAD_COLOR = (0, 0, 0)

# ボードの初期化
def init_board():
    board = np.zeros((HEIGHT//CELL_SIZE, WIDTH//CELL_SIZE), dtype=int)
    board[5, 1:4] = 1
    board[6, 4] = 1
    board[6, 5] = 1
    board[7, 2:5] = 1
    return board

# セルの描画
def draw_cell(surface, x, y, alive):
    color = ALIVE_COLOR if alive else DEAD_COLOR
    rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)

# ボードの描画
def draw_board(surface, board):
    surface.fill(DEAD_COLOR)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            draw_cell(surface, j*CELL_SIZE, i*CELL_SIZE, board[i, j])

# ボードの更新
def update_board(board):
    # 周囲8セルの状態を計算する
    neighbor_count = np.zeros_like(board)
    neighbor_count[1:, 1:] += board[:-1, :-1]
    neighbor_count[1:, :-1] += board[:-1, 1:]
    neighbor_count[:-1, 1:] += board[1:, :-1]
    neighbor_count[:-1, :-1] += board[1:, 1:]
    neighbor_count[:-1, :] += board[1:, :]
    neighbor_count[1:, :] += board[:-1, :]
    neighbor_count[:, :-1] += board[:, 1:]
    neighbor_count[:, 1:] += board[:, :-1]

    # ルールに従って次の状態を計算する
    next_board = np.zeros_like(board)
    next_board[(board == 1) & (neighbor_count == 2) | (neighbor_count == 3)] = 1
    next_board[(board == 0) & (neighbor_count == 3)] = 1
    return next_board

def main():
    pygame.init()
    screen = pygame.display.set_mode(BOARD_SIZE)
    clock = pygame.time.Clock()

    board = init_board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        draw_board(screen, board)
        board = update_board(board)

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
