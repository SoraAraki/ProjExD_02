import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
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

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bd_img,bd_rct)
        bd_rct.move_ip(vx,vy)

        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()