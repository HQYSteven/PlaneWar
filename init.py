import pygame
import random

from tools import tools, programme
'''
 * When I wrote this, only God and I understood what I was doing
 * Now, God only knows
 */
/***
* 写这段代码的时候，只有上帝和我知道它是干嘛的
* 现在，只有上帝知道
*/
'''


class init(object):
    def __init__(self):

        # 运行指示量
        self.running = True
        init.init_modules(self,)
        init.init_planeAmount(self,)
        init.init_players(self,)
        init.init_attackStrings(self,)
        init.init_screen(self,)
        init.init_enemy(self,)
        init.init_medicine(self,)
        init.init_bullet(self,)
        init.init_stars(self,)
        init.init_fps(self,)
        init.init_egg(self,)
        self.god = False
        init.initStone(self,)

    def init_gui(self,):
        text = self.font.render(f"100", True, 'white')
        self.screen.blit(text, (250, 10))
        # 绘制 玩家血条
        pygame.draw.rect(self.screen, [255, 0, 0], [300, 10, 100, 20])
        # 添加游戏初始的敌人的坐标
        tools.appendEnemy()
        tools.ui.aircraft_1()
        pygame.display.set_caption(f"Plane War [{self.version}]")
        # 初始化玩家2
        if self.player2:
            tools.ui.player2Aircraft()
        # 在屏幕上绘制敌人s
        pygame.key.set_repeat(3, 25)

    def init_modules(self,):
        self.player2 = False
        # init pygame
        pygame.init()
        # init pygame music player
        pygame.mixer.init()
        pygame.key.set_repeat(3, 25)

    def init_medicine(self,):
        self.stringMov = 5
        self.medicineAmount = 20
        self.medicineX = []
        self.medicineY = []

    def init_stars(self,):
        self.starXList = []
        self.starYList = []
        for i in range(200):
            self.starXList.append(random.randint(0, 500))
            self.starYList.append(random.randint(0, 500))

    def init_attackStrings(self,):
        self.AttackColor = [0, 255, 255]
        self.attackStringX = []
        self.attackStringY = []

    def init_bullet(self,):
        self.player1_bullet = self.planeAmount * 10+10
        self.player2_bullet = self.planeAmount * 10+10
        self.minus = 10
        self.mode = 'normal'
        self.crash = 10
        self.hit = 5
        self.attack = 20
        self.bullet = 20
        self.stone = 1
        self.cure = 50
        self.artillery = 30
        self.Xrate = 40
        self.missile = 50
        self.color1 = [0, 255, 255]
        self.color2 = [30, 144, 255]
        self.color3 = [0, 0, 139]
        self.color4 = [255, 20, 147]
        self.stringMov = 10

    def init_egg(self,):
        self.initColor = [0, 0, 0]
        self.fuelAmount = 0.5
        self.gravity = 0.05
        self.add = 0.00001
        self.distance = 1000

        self.length = 90
        self.lostFuel = False
        self.lost = 0.000001
        self.launcher = [248, 248, 255]
        self.fuel = 1

    def init_enemy(self,):
        self.otherAttack_x = []
        self.otherAttack_y = []
        self.enemy_x_list = []
        self.enemy_y_list = []
        self.enemyLifeList = []

    def init_planeAmount(self,):
        self.mov = False
        self.planeColor_player = [30, 144, 255]
        self.wigColor_player = [131, 206, 250]
        self.planeColor_enemy = [192, 192, 192]
        self.wigColor_enemy = [178, 34, 34]
        self.planeAmount =  random.randint(10, 30)
        self.speed = 0

    def init_screen(self,):
        self.message = []
        self.font = pygame.font.Font(
            "default.ttf", 20)
        self.screen = pygame.display.set_mode((500, 500))
        self.screen.fill((0, 0, 0))
        self.screenWidth = 500
        self.screenHeight = 500
        self.movAmount = 5
        # set the frame resizeable
        pygame.RESIZABLE = True

    def initStone(self,):
        self.stoneXList = []
        self.stoneYList = []

    def init_players(self,):
        self.fire = [255, 0, 0]
        self.playing = True
        self.player1_life = 100
        self.player2_life = 100
        self.player2_bullet = self.planeAmount * 20 + 10
        self.player1_bullet = self.planeAmount * 20 + 10
        self.score = 0
        self.attackXList = []
        self.attackYList = []
        self.player2_x = 225
        self.player1_x = 240
        self.player1_y = 440
        self.player2_y = 470
        self.player1_fuel = 1
        self.frame_player1 = 0
        self.frame_player2 = 0

    def init_fps(self,fps=15):
        self.version = "0.5.6"
        self.fps = fps
