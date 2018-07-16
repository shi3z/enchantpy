# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
    (w,h) = (400,400)   # 画面サイズ
    (x,y) = (w/2, h/2)
    pygame.init()       # pygame初期化
    pygame.display.set_mode((w, h), 0, 32)  # 画面設定
    screen = pygame.display.get_surface()
    im = pygame.image.load("chara1.png").convert_alpha()
    rect = im.get_rect()
    rect.center = (w/2, h/2)

    while (1):
        # キーイベント処理(キャラクタ画像の移動)
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            rect.move_ip(-1, 0)
        if pressed_key[K_RIGHT]:
            rect.move_ip(1, 0)
        if pressed_key[K_UP]:
            rect.move_ip(0, -1)
        if pressed_key[K_DOWN]:
            rect.move_ip(0, 1)

        pygame.display.update()     # 画面更新
        pygame.time.wait(30)        # 更新時間間隔
        screen.fill((0, 20, 0, 0))  # 画面の背景色
        screen.blit(im, rect)       # 画像の描画
        # 終了用のイベント処理
        for event in pygame.event.get():
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:       # キーを押したとき
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
