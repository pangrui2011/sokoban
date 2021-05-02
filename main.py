import sys
import pandas as pd
from setting import *
import pygame
import pygame.freetype


# 游戏类
class Game(object):
    def __init__(self):
        # 初始化pygame
        pygame.init()

        # 加载字体
        self.fl = pygame.freetype.Font('C://Windows//Fonts//simsun.ttc', 30)

        # 创建界面
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # 界面大小

        # 修改标题
        pygame.display.set_caption("推箱子")

        # 修改时钟
        self.clock = pygame.time.Clock()

        # 加载开始界面背景
        self.start = pygame.image.load(r"image\start.png")

        # 设置当前关卡数
        self.checkpoint = 1

        # 设置最大步数记录
        self.max_checkpoint = 999

    # 游戏菜单界面
    def star(self, fps=60):
        # 界面上选择三角的初始位置
        single_rect = [[170, 630], [170, 660], [170 + (30 ** 2 - 15 ** 2) ** 0.5, 645]]

        # 刷新界面
        self.start = pygame.image.load(r"image\start.png")

        # 绘制用户信息

        # 绘制文本菜单到start界面上
        # self.fl.render_to(self.start, (180, 660), "开始游戏", fgcolor=RED, size=40)
        # self.fl.render_to(self.start, (180, 710), "选择关卡", fgcolor=RED, size=40)

        # 播背景音乐
        pygame.mixer.music.load('audio\star.wav')
        pygame.mixer.music.play(-1, 0.0)

        """开始界面"""
        while True:
            # 绘制选择三角
            pygame.draw.rect(self.screen, (0, 0, 0), (260, single_rect[0][1], 26, 31))

            # 事件监听
            for i in pygame.event.get():
                # 判断推出事件
                if i.type == pygame.QUIT:
                    sys.exit()
                # 判断是否按键，调用开始界面的按键事件
                elif i.type == pygame.KEYDOWN:
                    # 跳转按键事件处理
                    single_rect = self.single_move(single_rect, i, mode=1)

            # 添加背景图片到主画板
            self.screen.blit(self.start, (0, 0))

            # 更新选择三角位置
            pygame.draw.polygon(self.screen, RED, single_rect)

            pygame.display.update()  # 刷新屏幕
            self.clock.tick(fps)  # 游戏时钟

    # 功能选择界面
    def single_move(self, sin_rect, p, mode=1):
        """
        选项移动
        :param sin_rect: 原三角坐标
        :param p: 按键检测
        :param mode: 模式1是开始菜单 模式2地图选择 模式3是地图制作
        :return: 修改后的三角坐标
        """
        # 游戏菜单选择
        if mode == 1:
            # 判断按键修改选择三角位置
            if p.key == pygame.K_UP:
                for j in sin_rect:
                    j[1] -= 50
            elif p.key == pygame.K_DOWN:
                for j in sin_rect:
                    j[1] += 50
            # 判断是否按下回车
            elif p.key == pygame.K_RETURN or p.key == pygame.K_KP_ENTER:
                # 判断三角位置实现对应功能
                if sin_rect[0][1] == 660:  # 开始游戏
                    # 设置当前关卡为管卡一
                    self.checkpoint = 1
                    self.action()
                elif sin_rect[0][1] == 710:  # 选择地图
                    self.select_map()
            # 判断选择三角的位置，进行越界处理
            if sin_rect[0][1] < 660:
                for j in sin_rect:
                    j[1] += 100

            elif sin_rect[0][1] > 710:
                for j in sin_rect:
                    j[1] -= 100
            return sin_rect
        # 游戏结束界面选择
        elif mode == 2:
            # 判断按键设置选择三角位置
            if p.key == pygame.K_UP:
                for j in sin_rect:
                    j[1] -= 50
            elif p.key == pygame.K_DOWN:
                for j in sin_rect:
                    j[1] += 50
            # 判断是否按下回车
            elif p.key == pygame.K_RETURN or p.key == pygame.K_KP_ENTER:
                # 判断三角位置实现对应功能
                if sin_rect[0][1] == 310:
                    # 进入下一关
                    if self.checkpoint < self.max_checkpoint:
                        # 当前关卡记录+1
                        self.checkpoint += 1
                        self.action(key1=False)
                elif sin_rect[0][1] == 360:
                    # 返回开始菜单
                    self.star()
            # 判断选择三角的位置，进行越界处理
            if sin_rect[0][1] < 310:
                for j in sin_rect:
                    j[1] += 100
            elif sin_rect[0][1] > 360:
                for j in sin_rect:
                    j[1] -= 100
            return sin_rect
        # 达到最大地图，溢出界面
        elif mode == 3:
            # 判断按键设置选择三角位置
            if p.key == pygame.K_UP:
                for j in sin_rect:
                    j[1] -= 50
            elif p.key == pygame.K_DOWN:
                for j in sin_rect:
                    j[1] += 50
            # 判断是否按下回车
            elif p.key == pygame.K_RETURN or p.key == pygame.K_KP_ENTER:
                # 判断三角位置实现对应功能
                if sin_rect[0][1] == 310:
                    # 重新从第一关开始游戏
                    # 设置当前游戏关卡记录为1
                    self.checkpoint = 1
                    self.action()
                elif sin_rect[0][1] == 360:
                    # 返回开始菜单
                    self.star()
            # 判断选择三角的位置，进行越界处理
            if sin_rect[0][1] < 310:
                for j in sin_rect:
                    j[1] += 100
            elif sin_rect[0][1] > 360:
                for j in sin_rect:
                    j[1] -= 100
            return sin_rect
        # 地图选择界面
        elif mode == 4:
            # 判断按键设置选择三角位置
            if p.key == pygame.K_LEFT:
                for j in sin_rect:
                    j[0] -= 160
            elif p.key == pygame.K_RIGHT:
                for j in sin_rect:
                    j[0] += 160
            # 判断是否按下回车
            elif p.key == pygame.K_RETURN or p.key == pygame.K_KP_ENTER:
                # 判断三角位置实现对应功能
                if sin_rect[0][0] == 10:
                    # 上一地图
                    # 判断当前选择地图是否为第一个
                    if self.checkpoint > 1:
                        self.checkpoint -= 1
                        self.select_map(x=10)
                elif sin_rect[0][0] == 170:
                    # 选择地图
                    self.action()
                elif sin_rect[0][0] == 330:
                    # 下一地图
                    # 判断当前选择地图是否为最后一个
                    if self.checkpoint < self.max_checkpoint:
                        self.checkpoint += 1
                        self.select_map(x=330)

            # 判断选择三角的位置，进行越界处理
            if sin_rect[0][0] < 10:
                for j in sin_rect:
                    j[0] += 480
            elif sin_rect[0][0] > 330:
                for j in sin_rect:
                    j[0] -= 480
            return sin_rect

    # 正常游戏界面
    def action(self, fps=60, key1=True):
        """
        游戏界面
        :param fps: 刷新率
        :param key1: 用来判断游戏是否需要重新加载音乐 下一关 从开 不需要重新加载音乐
        :return:
        """
        # 加载有效背景
        bank = pygame.image.load(r"image\bank.png")

        # 停止播放开始界面背景音乐，播放游戏背景音乐（判断是否需要重新加载）
        if key1:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(r'audio\action.wav')
            pygame.mixer.music.play(-1, 0.0)

        # 初始化人物地图
        figure = Figure()
        map = Map()

        # 地图id
        map_id = 1
        max_stepCount = 999

        # 读地图数据
        data = map.read()
        self.max_checkpoint = len(data)
        # 判断当前地图是否处于正常范围
        if 0 < self.checkpoint <= self.max_checkpoint:
            # 取出对应地图内容文本
            res = data[self.checkpoint - 1]
            try:
                # 加载地图
                map.load(res[0], figure)
                # 地图最佳记录赋值
                max_stepCount = res[1]
                # 地图id赋值，用来修改地图最佳记录
                map_id = self.checkpoint - 1
            except:
                self.max_map(bank)
        else:
            self.max_map(bank)

        while True:
            """游戏主循环"""
            key = False
            # 事件监听
            for i in pygame.event.get():
                # 退出监听
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    # 按键判断（判断上下左右，调整人物方向，调用人物移动方法）
                    if i.key == pygame.K_UP:
                        figure.figure_direction = 0
                        figure.move()
                    elif i.key == pygame.K_DOWN:
                        figure.figure_direction = 1
                        figure.move()
                    elif i.key == pygame.K_LEFT:
                        figure.figure_direction = 2
                        figure.move()
                    elif i.key == pygame.K_RIGHT:
                        figure.figure_direction = 3
                        figure.move()
                    # ESC退出
                    elif i.key == pygame.K_ESCAPE:
                        self.star()
                    # R重开
                    elif i.key == pygame.K_r:
                        pygame.mixer.Sound(r'audio\R.wav').play()
                        self.action(key1=False)
                    # T跳关
                    elif i.key == pygame.K_t:
                        # 判断当前关卡是否为最后一关
                        if self.checkpoint < self.max_checkpoint:
                            pygame.mixer.Sound(r'audio\R.wav').play()
                            self.checkpoint += 1
                            self.action(key1=False)
                    # 判断游戏胜利
                    if self.is_victory():
                        key = True

            # 加载背景图片刷新
            bank = pygame.image.load(r"image\bank.png")

            # 画出地图
            map.draw(bank, figure)

            # 画背景
            self.screen.blit(bank, (0, 0))

            # 画出文字信息
            self.fl.render_to(self.screen, (380, 25), "当前步数:{}".format(figure.stepCount), fgcolor=WHITE, size=20)
            self.fl.render_to(self.screen, (380, 2), "最高纪录:{}".format(max_stepCount), fgcolor=WHITE, size=20)

            self.fl.render_to(self.screen, (0, 780), "小键盘控制移动,R重新开始,ESC返回菜单,T键进入下一关", fgcolor=WHITE, size=20)

            # 判断游戏是否结束
            if key:
                # 判断是否破记录
                if figure.stepCount < max_stepCount:
                    map.save(map_id,figure.stepCount)

                # 游戏结束界面
                self.victory(bank)

            pygame.display.update()  # 刷新屏幕

            self.clock.tick(fps)  # 游戏时钟

    # 游戏胜利判断
    def is_victory(self):
        """判断箱子是否都在箱子点"""
        # 遍历地图数据
        for i, x in enumerate(Map.this_map):
            for j, y in enumerate(x):
                # 判断是否为箱子
                if y == 2:
                    # 判断箱子是否在坐标点
                    if (i, j) not in Map.this_end_li:
                        # 不在返回False
                        return False
        return True

    # 游戏胜利界面
    def victory(self, screen, fps_s=60):
        """结束界面"""

        # 播放游戏胜利音效
        pygame.mixer.Sound(r'audio\victory.wav').play()
        # 设置选择三角位置
        single_rect = [[180, 310], [180, 330], [180 + (20 ** 2 - 10 ** 2) ** 0.5, 320]]

        # 设置提示内容
        self.fl.render_to(screen, (60, 240), "游戏胜利({}/{})".format(self.checkpoint, self.max_checkpoint), fgcolor=GOLD,
                          size=60)
        self.fl.render_to(screen, (200, 310), "下一关", fgcolor=WHITE, )
        self.fl.render_to(screen, (200, 360), "返回菜单", fgcolor=WHITE, )

        while True:
            # 事件监听
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    # 按键事件
                    single_rect = self.single_move(single_rect, i, mode=2)

            # 画背景
            self.screen.blit(screen, (0, 0))

            # 画三角
            pygame.draw.polygon(self.screen, RED, single_rect)

            pygame.display.update()  # 刷新屏幕
            self.clock.tick(fps_s)  # 游戏时钟

    # 最大地图界面
    def max_map(self, screen, fps_s=60):
        """
        最大地图界面，数据库异常才会显示
        :param screen: 画板对象
        :param fps_s: 刷新率
        :return: 无
        """
        # 设置选择三角位置
        single_rect = [[160, 310], [160, 330], [160 + (20 ** 2 - 10 ** 2) ** 0.5, 320]]

        # 设置目录和提示内容
        self.fl.render_to(screen, (120, 250), "最后地图", fgcolor=GOLD, size=60)
        self.fl.render_to(screen, (180, 310), "返回第一关", fgcolor=WHITE, )
        self.fl.render_to(screen, (180, 360), "返回主菜单", fgcolor=WHITE, )

        while True:
            # 事件监听
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    # 按键事件
                    single_rect = self.single_move(single_rect, i, mode=3)

            # 画背景
            self.screen.blit(screen, (0, 0))

            # 画三角
            pygame.draw.polygon(self.screen, RED, single_rect)

            pygame.display.update()  # 刷新屏幕
            self.clock.tick(fps_s)  # 游戏时钟

    # 地图选择界面
    def select_map(self, fps=60, x=170):
        """
        地图选择界面
        :param fps: 刷新率
        :param x: 选择三角的左边位置
        :return: 无
        """
        # 加载有效背景
        self.screen.fill((0, 0, 0))

        # 停止播放开始界面背景音乐，播放游戏背景音乐
        pygame.mixer.music.stop()
        pygame.mixer.music.load(r'audio\select_map.wav')
        pygame.mixer.music.play(-1, 0.0)

        # 加载游戏界面背景
        bank = pygame.image.load(r"image\bank.png")

        # 初始化人物地图
        figure = Figure()
        map = Map()

        # 读地图数据
        data = map.read()

        self.max_checkpoint = len(data)
        # 判断当前地图是否大于最大地图数量或者小于0
        if 0 < self.checkpoint <= self.max_checkpoint:
            # 取出当前地图文本
            res = data[self.checkpoint - 1]
            try:
                # 加载地图
                map.load(res[0], figure)
            except:
                self.max_map(bank)
        else:
            self.max_map(bank)

        # 加载背景图片刷新
        bank = pygame.image.load(r"image\bank.png")

        # 画出地图
        map.draw(bank, figure)

        # 缩小游戏地图
        bank = pygame.transform.scale(bank, (250, 400))

        # 选择三角初始位置
        single_rect = [[x, 605], [x, 625], [x + (20 ** 2 - 10 ** 2) ** 0.5, 613]]

        while True:
            """游戏主循环"""
            # 事件监听
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    # 按键事件ESC返回
                    if i.key == pygame.K_ESCAPE:
                        self.star()
                    else:
                        single_rect = self.single_move(single_rect, i, mode=4)

            # 背景填充黑色
            self.screen.fill((0, 0, 0))

            # 画游戏地图到背景上
            self.screen.blit(bank, (125, 100))

            # 画出界面文字
            # 游戏地图数量
            self.fl.render_to(self.screen, (220, 510), "{}/{}".format(self.checkpoint, self.max_checkpoint),
                              fgcolor=WHITE, size=45)
            self.fl.render_to(self.screen, (30, 600), "上一地图", fgcolor=WHITE, size=30)
            self.fl.render_to(self.screen, (190, 600), "选择地图", fgcolor=GOLD, size=30)
            self.fl.render_to(self.screen, (350, 600), "下一地图", fgcolor=WHITE, size=30)

            # 画三角
            pygame.draw.polygon(self.screen, RED, single_rect)

            pygame.display.update()  # 刷新屏幕

            self.clock.tick(fps)  # 游戏时钟

    # 提示界面
    def message(self, screen, text, left=160, fps_s=60):
        """
        提示界面
        :param screen: 画板对象
        :param text: 需要提示的文本
        :param left: 提示文本的左边位置
        :param fps_s: 刷新率
        :return: 无
        """

        # 初始化提示背景
        mess = MESSAGE.convert_alpha()
        # 修改背景透明度
        mess.set_alpha(3)
        # 设置目录和提示内容提示内容
        self.fl.render_to(mess, (left, 0), "{}".format(text), fgcolor=BLACK, size=40)
        self.fl.render_to(mess, (130, 50), "回车继续游戏", fgcolor=RED, size=40)
        while True:
            # 事件监听
            # 设置key判断是否结束提示
            key = False
            for i in pygame.event.get():
                # 关闭按钮监听
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    # 按键事件
                    # 判断是否为回车键
                    if i.key == pygame.K_RETURN or i.key == pygame.K_KP_ENTER:
                        key = True
            # 跳出界面循环，返回原界面
            if key:
                break

            # 画背景
            screen.blit(mess, (0, 300))

            # 添加背景到主画板
            self.screen.blit(screen, (0, 0))

            pygame.display.update()  # 刷新屏幕
            self.clock.tick(fps_s)  # 游戏时钟


# 地图类
class Map:
    # 创建默认地图，防止数据出问题，导致游戏错误
    this_map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 4, 2, 3, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    # 创建地图中箱子点的列表，用于判断原坐标点是否为箱子点
    this_end_li = []

    # 初始化方法
    def __init__(self):
        # 初始化 树 灰箱子 箱子点 绿箱子
        self.tree = TREE
        self.box = BOX
        self.end = END
        self.box1 = BOX1

    # 读取地图
    def read(self):
        data = pd.read_csv('maps.csv', encoding='utf-8')
        li = data.values.tolist()
        return li

    # 修改分数
    def save(self, index, score):
        df = pd.read_csv('maps.csv', encoding='utf-8')
        df.loc[index:index, 'score'] = score
        df.to_csv('maps.csv', index=False)

    # 画地图方法
    def draw(self, screen, figure):
        """
        画地图
        :param screen: 画板对象
        :param figure: 人物对象
        :return: 无
        """
        # 遍历地图数据
        for i, x in enumerate(Map.this_map):
            for j, y in enumerate(x):
                # 判断是否为树
                if y == 1:
                    screen.blit(self.tree, (50 * j, 50 * i - 10))
                # 判断是否为箱子
                elif y == 2:
                    # 判断是否为箱子点，是就画绿箱子否则画灰箱子
                    if (i, j) in Map.this_end_li:
                        screen.blit(self.box1, (50 * j, 50 * i - 10))
                    else:
                        screen.blit(self.box, (50 * j, 50 * i - 10))
                # 判断是否为箱子点
                elif y == 3:
                    screen.blit(self.end, (50 * j, 50 * i - 10))
                # 判断是否为人物
                elif y == 4:
                    figure.draw(screen)
                # 判断是否为箱子加箱子点
                elif y == 5:
                    screen.blit(self.box1, (50 * j, 50 * i - 10))

    # 加载地图
    def load(self, text, figure):
        """
        加载地图
        :param text: 数据库存储的地图文本
        :param figure: 人物对象，用于存储人物坐标
        :return: 无返回
        """
        # 清空箱子点坐标
        Map.this_end_li = []
        # 逗号分隔文本
        li = text.split(',')
        # 去除最后空位置文本
        li.pop()
        # 便利li 使用map方法，把文本转为数字，最终转成列表
        li = [list(map(int, list(i))) for i in li]
        # 为当前地图赋值
        Map.this_map = li
        # 遍历地图，找到人物坐标和箱子点坐标，进行存储
        for i, x in enumerate(Map.this_map):
            for j, y in enumerate(x):
                # 判断为箱子点和箱子加箱子点
                if y == 3 or y == 5:
                    Map.this_end_li.append((i, j))
                # 判断为人物
                if y == 4:
                    figure.figure_x = j
                    figure.figure_y = i


# 人物类
class Figure:
    # 初始化方法
    def __init__(self):
        # 初始化人物图片
        self.figure_up = FIGURE_UP
        self.figure_down = FIGURE_DOWN
        self.figure_left = FIGURE_LEFT
        self.figure_right = FIGURE_RIGHT
        # 指定默认图片 默认朝下
        self.figure = self.figure_down

        # 记录人物位置
        self.figure_x = 4
        self.figure_y = 6

        # 记录人物朝向 0-上 1下 2左 3右
        self.figure_direction = 1

        # 记录使用步数
        self.stepCount = 0

    # 移动方法一
    def move(self):
        # 根据人物朝向不同，向不同位置移动
        if self.figure_direction == 0:
            # 判断人物行走后是否越界 和 调用移动方法二判断人物是否可以向前方移动
            if self.figure_y > 0 and self.go(self.figure_y - 1, self.figure_x, self.figure_y - 2, self.figure_x):
                # 没有障碍，人物位置修改
                self.figure_y -= 1
            # 修改人物朝向图片
            self.figure = self.figure_up
        # 以下同理
        elif self.figure_direction == 1:
            if self.figure_y < 15 and self.go(self.figure_y + 1, self.figure_x, self.figure_y + 2, self.figure_x):
                self.figure_y += 1
            self.figure = self.figure_down
        elif self.figure_direction == 2:
            if self.figure_x > 0 and self.go(self.figure_y, self.figure_x - 1, self.figure_y, self.figure_x - 2):
                self.figure_x -= 1
            self.figure = self.figure_left
        elif self.figure_direction == 3:
            if self.figure_x < 9 and self.go(self.figure_y, self.figure_x + 1, self.figure_y, self.figure_x + 2):
                self.figure_x += 1
            self.figure = self.figure_right

    # 移动方法二
    def go(self, x, y, x1, y1, ):
        """
        :param x 人物前方一格的x坐标:
        :param y 人物前方一格的y坐标:
        :param x1 人物前方二格的x坐标:
        :param y1 人物前方二格的y坐标:
        :return 返回移动结果，是否可以移动:
        """
        # 前方判断是否为树木
        if Map.this_map[x][y] == 1:
            # 是树木禁止移动
            return False
        # 判断前方是否为箱子 和 箱子和点重合
        if Map.this_map[x][y] == 2 or Map.this_map[x][y] == 5:
            # 前方为箱子，判断前方第二格内容
            # 判断第二格坐标是否越界 判断第二格坐标是否为树 箱子 箱子和点重合
            if x1 < 0 or x1 > 15 or y1 < 0 or y1 > 9 or Map.this_map[x1][y1] == 1 or Map.this_map[x1][y1] == 2 or \
                    Map.this_map[x1][y1] == 5:
                # 树 箱子 箱子和点重合 禁止移动
                return False
            else:
                # 可以移动，判断箱子前是否为箱子点，是箱子点就播放音乐
                if Map.this_map[x1][y1] == 3:
                    pygame.mixer.Sound(r'audio\box.wav').play()
                # 把地图中人物前方的第二点改为箱子
                Map.this_map[x1][y1] = 2
        # 修改原人物点为空地
        Map.this_map[self.figure_y][self.figure_x] = 0
        # 判断原人物点是否为箱子点
        if (self.figure_y, self.figure_x) in Map.this_end_li:
            # 是箱子点就还原为箱子点
            Map.this_map[self.figure_y][self.figure_x] = 3
        # 修改人物前方点为人物
        Map.this_map[x][y] = 4
        # 人物移动步数加一
        self.stepCount += 1
        return True

    # 把人物画在画板上
    def draw(self, screen):
        """
        :param screen: 画板对象
        :return: 无返回
        """
        screen.blit(self.figure, (self.figure_x * 50 - 7, self.figure_y * 50 - 30))


if __name__ == '__main__':
    game = Game()
    game.star()
