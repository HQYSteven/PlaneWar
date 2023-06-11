import pygame
import random
from Append import Append
from programme import programme
'''
 * When I wrote this, only God and I understood what I was doing
 * Now, God only knows
 */
/***
* 写这段代码的时候，只有上帝和我知道它是干嘛的
* 现在，只有上帝知道
*/
'''


class init(programme):
    def init(master):
        

        # 运行指示量
        master.blur = True
        master.running = True
        init.init_modules(master,)
        init.init_planeAmount(master,)
        init.init_players(master,)
        init.init_attackStrings(master,)
        init.init_screen(master,)
        init.init_enemy(master,)
        init.init_medicine(master,)
        init.init_bullet(master,)
        init.init_stars(master,)
        init.init_fps(master,)
        init.init_egg(master,)
        master.god = False
        init.initStone(master,)
        return master

    def init_gui(master,):
        text = master.font.render(f"100", True, 'white')
        master.screen.blit(text, (250, 10))
        # 绘制 玩家血条
        pygame.draw.rect(master.screen, [255, 0, 0], [300, 10, 100, 20])
        # 添加游戏初始的敌人的坐标
        Append.appendEnemy()
        pygame.display.set_caption(f"Plane War [{master.version}]")
        # 在屏幕上绘制敌人s
        pygame.key.set_repeat(3, 25)

    def init_modules(master,):
        master.player2 = False
        # init pygame
        pygame.init()
        # init pygame music player
        pygame.mixer.init()
        pygame.key.set_repeat(3, 25)

    def init_medicine(master,):
        master.stringMov = 5
        master.medicineAmount = 20
        master.medicineX = []
        master.medicineY = []

    def init_stars(master,):
        master.starXList = []
        master.starYList = []
        for i in range(200):
            master.starXList.append(random.randint(0, 500))
            master.starYList.append(random.randint(0, 500))

    def init_attackStrings(master,):
        master.AttackColor = [0, 255, 255]
        master.attackStringX = []
        master.attackStringY = []

    def init_bullet(master,):
        master.player1_bullet = master.planeAmount * 10+10
        master.player2_bullet = master.planeAmount * 10+10
        master.minus = 10
        master.mode = 'normal'
        master.crash = 10
        master.hit = 5
        master.attack = 20
        master.bullet = 20
        master.stone = 1
        master.cure = 50
        master.artillery = 30
        master.Xrate = 40
        master.missile = 50
        master.color1 = [0, 255, 255]
        master.color2 = [30, 144, 255]
        master.color3 = [0, 0, 139]
        master.color4 = [255, 20, 147]
        master.stringMov = 10

    def init_egg(master,):
        master.initColor = [0, 0, 0]
        master.fuelAmount = 0.5
        master.gravity = 0.05
        master.add = 0.00001
        master.distance = 1000

        master.length = 90
        master.lostFuel = False
        master.lost = 0.000001
        master.launcher = [248, 248, 255]
        master.fuel = 1

    def init_enemy(master,):
        master.otherAttack_x = []
        master.otherAttack_y = []
        master.enemy_x_list = []
        master.enemy_y_list = []
        master.enemyLifeList = []

    def init_planeAmount(master,):
        master.mov = False
        master.planeColor_player = [30, 144, 255]
        master.wigColor_player = [131, 206, 250]
        master.planeColor_enemy = [192, 192, 192]
        master.wigColor_enemy = [178, 34, 34]
        master.planeAmount =  random.randint(10, 30)
        master.speed = 0

    def init_screen(master,):
        master.message = []
        master.font = pygame.font.Font(
            "default.ttf", 20)
        master.screen = pygame.display.set_mode((500, 500))
        master.screen.fill((0, 0, 0))
        master.screenWidth = 500
        master.screenHeight = 500
        master.movAmount = 5
        # set the frame resizeable
        pygame.RESIZABLE = True

    def initStone(master,):
        master.stoneXList = []
        master.stoneYList = []

    def init_players(master,):
        master.fire = [255, 0, 0]
        master.playing = True
        master.player1_life = 100
        master.player2_life = 100
        master.player2_bullet = master.planeAmount * 20 + 10
        master.player1_bullet = master.planeAmount * 20 + 10
        master.score = 0
        master.attackXList = []
        master.attackYList = []
        master.player2_x = 225
        master.player1_x = 240
        master.player1_y = 440
        master.player2_y = 470
        master.player1_fuel = 1
        master.frame_player1 = 0
        master.frame_player2 = 0

    def init_fps(master,fps=15):
        master.version = "0.5.6"
        master.fps = fps
