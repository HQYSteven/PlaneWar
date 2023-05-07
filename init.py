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
    def __init__():

        # 运行指示量
        programme.running = True
        init.init_modules()
        init.init_planeAmount()
        init.init_players()
        init.init_attackStrings()
        init.init_screen()
        init.init_enemy()
        init.init_medicine()
        init.init_bullet()
        init.init_stars()
        init.init_fps()
        init.init_egg()
        programme.god = False
        init.initStone()

    def init_gui():
        text = programme.font.render(f"100", True, 'white')
        programme.screen.blit(text, (250, 10))
        # 绘制 玩家血条
        pygame.draw.rect(programme.screen, [255, 0, 0], [300, 10, 100, 20])
        # 添加游戏初始的敌人的坐标
        tools.appendEnemy()
        tools.ui.aircraft_1()
        pygame.display.set_caption(f"Plane War [{programme.version}]")
        # 初始化玩家2
        if programme.player2:
            tools.ui.player2Aircraft()
        # 在屏幕上绘制敌人s
        pygame.key.set_repeat(3, 25)

    def init_modules():
        programme.player2 = False
        # init pygame
        pygame.init()
        # init pygame music player
        pygame.mixer.init()
        pygame.key.set_repeat(3, 25)

    def init_medicine():
        programme.medicineAmount = 20
        programme.medicineX = []
        programme.medicineY = []

    def init_stars():
        programme.starXList = []
        programme.starYList = []
        for i in range(200):
            programme.starXList.append(random.randint(0, 500))
            programme.starYList.append(random.randint(0, 500))

    def init_attackStrings():
        programme.AttackColor = [0, 255, 255]
        programme.attackStringX = []
        programme.attackStringY = []

    def init_bullet():
        programme.player1_bullet = programme.planeAmount * 10+10
        programme.player2_bullet = programme.planeAmount * 10+10
        programme.minus = 10
        programme.mode = 'normal'
        programme.crash = 10
        programme.hit = 5
        programme.attack = 20
        programme.bullet = 20
        programme.stone = 1
        programme.cure = 50
        programme.artillery = 30
        programme.Xrate = 40
        programme.missile = 50
        programme.color1 = [0, 255, 255]
        programme.color2 = [30, 144, 255]
        programme.color3 = [0, 0, 139]
        programme.color4 = [255, 20, 147]
        programme.stringMov = 10

    def init_egg():
        programme.initColor = [0, 0, 0]
        programme.fuelAmount = 0.5
        programme.gravity = 0.05
        programme.add = 0.00001
        programme.distance = 1000

        programme.length = 90
        programme.lostFuel = False
        programme.lost = 0.000001
        programme.launcher = [248, 248, 255]
        programme.fuel = 1

    def init_enemy():
        programme.otherAttack_x = []
        programme.otherAttack_y = []
        programme.enemy_x_list = []
        programme.enemy_y_list = []
        programme.enemyLifeList = []

    def init_planeAmount():
        programme.mov = False
        programme.planeColor_player = [30, 144, 255]
        programme.wigColor_player = [131, 206, 250]
        programme.planeColor_enemy = [192, 192, 192]
        programme.wigColor_enemy = [178, 34, 34]
        programme.planeAmount =  random.randint(10, 30)
        programme.speed = 0

    def init_screen():
        programme.message = []
        programme.font = pygame.font.Font(
            "default.ttf", 20)
        programme.screen = pygame.display.set_mode((500, 500))
        programme.screen.fill((0, 0, 0))
        programme.screenWidth = 500
        programme.screenHeight = 500
        programme.movAmount = 5
        # set the frame resizeable
        pygame.RESIZABLE = True

    def initStone():
        programme.stoneXList = []
        programme.stoneYList = []

    def init_players():
        programme.fire = [255, 0, 0]
        programme.playing = True
        programme.player1_life = 100
        programme.player2_life = 100
        programme.player2_bullet = programme.planeAmount * 20 + 10
        programme.player1_bullet = programme.planeAmount * 20 + 10
        programme.score = 0
        programme.attackXList = []
        programme.attackYList = []
        programme.player2_x = 225
        programme.player1_x = 240
        programme.player1_y = 440
        programme.player2_y = 470
        programme.player1_fuel = 1
        programme.frame_player1 = 0
        programme.frame_player2 = 0

    def init_fps(fps=15):
        programme.version = "0.5.6"
        programme.fps = fps
