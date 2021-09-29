# 玩家退出时，我们将使用模块sys 来退出游戏。
import sys
# 模块pygame 包含开发游戏所需的功能。
import pygame


def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # ，指定了游戏窗口的尺寸。
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # 设置背景颜色
    bg_color = (210,230,210)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 每次循环时都重绘屏幕
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()