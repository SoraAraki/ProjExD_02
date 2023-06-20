import random
import sys
import pygame as pg
delta = {                  
        pg.K_UP:(0,-5), # 移動量の上
        pg.K_DOWN:(0,+5), # 移動量の下
        pg.K_LEFT:(-5,0), # 移動量の左
        pg.K_RIGHT:(+5,0) #　移動量の右
        }



WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
     # こうかとんSurface（kk_img）からこうかとんRect（kk_rct）を抽出する
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bd_img = pg.Surface((20,20)) # 爆弾の作成
    pg.draw.circle(bd_img,(255,0,0),(10,10),10) # 爆弾を設定
    bd_img.set_colorkey((0,0,0)) # 背景を透過
    x = random.randint(0,WIDTH)   # 爆弾の座標をランダムの位置に
    y = random.randint(0,HEIGHT) 
    bd_rct = bd_img.get_rect()
    bd_rct.center = x, y
    vx,vy = +1,+1

    clock = pg.time.Clock()
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 合計移動量
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(kk_img,kk_rct)
        screen.blit(bd_img,bd_rct)
        bd_rct.move_ip(vx,vy)# 練習２

        pg.display.update()
        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(bb_img, bb_rct)
        bb_rct.move_ip(vx, vy)
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()