# 设置类，存放一些常量
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 500, 800)
# 游戏刷新帧率
FRAME_PER_SEC = 60

# 字体颜色
GOLD = 255, 251, 0
RED = 255, 0, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0

# 人物图片 上 下 左 右
FIGURE_UP = pygame.image.load(r"image\up.png")
FIGURE_DOWN = pygame.image.load(r"image\down.png")
FIGURE_LEFT = pygame.image.load(r"image\left.png")
FIGURE_RIGHT = pygame.image.load(r"image\right.png")

# 地图图片 树 灰箱子 绿箱子 箱子点 制作地图红光标 信息面板背景图
TREE = pygame.image.load(r"image\tree.png")
BOX = pygame.image.load(r"image\box.png")
BOX1 = pygame.image.load(r"image\box1.png")
END = pygame.image.load(r"image\end.png")
CURSOR = pygame.image.load(r"image\cursor.png")
MESSAGE = pygame.image.load(r"image\message.png")
