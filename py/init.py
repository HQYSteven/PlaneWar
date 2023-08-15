import pygame
import random
from tools import tools
from kernel import programme
from music import music
'''
 * When I wrote this, only God and I understood what I was doing
 * Now, God only knows
 * 写这段代码的时候，只有上帝和我知道它是干嘛的
 * 现在，只有上帝知道
'''


class init(programme):
    '''
    A class used to init all the modules together.
    '''
    def restore(master,path):
        master.stringMov = tools.file.config("stringMov",path)
        master.medicineAmount = tools.file.config("medicineAmount",path)
        master.medicineX = tools.file.config("medicineX",path)
        master.medicineY = tools.file.config("medicineY",path)
        master.attackStringX = tools.file.config("attackStringX",path)
        master.attackStringY = tools.file.config("attackStringY",path)
        master.player1_bullet = tools.file.config("player1_bullet",path)
        master.player2_bullet = tools.file.config("player2_bullet",path)
        master.stringMov = tools.file.config("stringMov",path)
        master.otherAttack_x = tools.file.config("otherAttack_x",path)
        master.otherAttack_y = tools.file.config("otherAttack_y",path)
        master.enemy_x_list = tools.file.config("enemy_x_list",path)
        master.enemy_y_list = tools.file.config("enemy_y_list",path)
        master.enemyLifeList = tools.file.config("enemyLifeList",path)
        master.planeAmount = tools.file.config("planeAmount",path)
        
    def init(master):
        '''
        @ master: The class you want to init 
        A fuc used to init all the modules togrther
        '''
        master.egg = False
        master.color = 0
        
        musics = music(tools.file.sourceConfig("audio"))
        #musics.play()
        # 运行指示量
        master.blur = False
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
    def init_restart(master):
        '''
        It inits the game when the player want to play again.
        '''
        master.running = True
        master.reply = ''
        init.init_planeAmount(master,)
        init.init_players(master,)
        init.init_attackStrings(master,)
        init.init_enemy(master,)
        init.init_medicine(master,)
        init.init_bullet(master,)
        init.init_fps(master,)
        init.init_egg(master,)
        init.initStone(master,)
    def init_gui(master,):
        '''
        @ master: The class you want to init 
         * A fuc used to init gui modules\n
         * Such as font,the first enemy,start screen,set repeat.
        '''
        
        text = master.font.render(f"100", True, 'white')
        master.screen.blit(text, (250, 10))
        pygame.display.set_caption(f"Plane War [{master.version}]")
        # 在屏幕上绘制敌人s
        pygame.key.set_repeat(3, 25)

    def init_modules(master,):
        '''
        @ master: The class you want to init 
         * A fuc used to init pygame and music modules\n
        '''
        master.settingIconPath = pygame.image.load(tools.file.sourceConfig("settingIconPath"),)
        master.backIconPath = pygame.image.load(tools.file.sourceConfig("backIconPath"),)
        master.singleIconPath = pygame.image.load(tools.file.sourceConfig("singleIconPath"),)
        master.doubleIconPath = pygame.image.load(tools.file.sourceConfig("doubleIconPath"),)
        master.aboutIconPath = pygame.image.load(tools.file.sourceConfig("aboutIconPath"),)
        master.music = True
        master.player2 = False
        # init pygame
        pygame.init()
        # init pygame music player
        pygame.mixer.init()
        #pygame.key.set_repeat(5, tools.file.config("repeat"))
    def init_medicine(master,):
        '''
        @ master: The class you want to init 
        A fuc used to init \n
         * medicine Amount\n
         * medicine lists\n
         * the length of every step you went. 
        '''
        master.stringMov = tools.file.config("stringMov")
        master.medicineAmount = tools.file.config("medicineAmount")
        master.medicineX = []
        master.medicineY = []
        master.graghicCommand = []

    def init_stars(master,):
        '''
        @ master: The class you want to init 
        A fuc used to init \n
         * star Amount\n
         * star lists\n
         * the coordinates of stars. 
        '''
        master.starXList = []
        master.starYList = []
        for i in range(200):
            master.starXList.append(random.randint(0, 500))
            master.starYList.append(random.randint(0, 500))

    def init_attackStrings(master,):
        '''
        @ master: The class you want to init 
        A fuc used to init \n
         * players' attack strings' Amount\n
         * players' attack strings' lists\n
         * the color of players' attack strings'. 
        '''
        master.AttackColor = tools.file.uiConfig("attackColor")
        master.attackStringX = []
        master.attackStringY = []

    def init_bullet(master,):
        '''
        @ master: The class you want to init 
        A fuc used to init \n
         * players' bullets' Amount\n
         * players' bullets' lists\n
         * the color of players' bullet'. \n
         * The color of every wapon modes\n
         * The hurt of every kind of wapons\n
         * The speed of the bullets
        '''
        master.player1_bullet = master.planeAmount * 10+10
        master.player2_bullet = master.planeAmount * 10+10
        master.minus = tools.file.config("min")
        master.mode = tools.file.config("defaultMode")
        master.crash = tools.file.config("crash")
        master.hit = tools.file.config("hit")
        master.attack = tools.file.config("attack")
        master.bullet = tools.file.config("bullet")
        master.stone = tools.file.config("stone")
        master.cure = tools.file.config("cure")
        master.artillery = tools.file.config("artillery")
        master.Xrate = tools.file.config("xray")
        master.missile = tools.file.config("missile")
        master.color1 = tools.file.uiConfig("color1")
        master.color2 = tools.file.uiConfig("color2")
        master.color3 = tools.file.uiConfig("color3")
        master.color4 = tools.file.uiConfig("color4")
        master.stringMov = tools.file.config("stringMov")

    def init_egg(master,):
        '''
        A fuction used to init eggs
        '''
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
        '''
        @ master: The class you want to init 
        A fuc used to init \n
         * enemies' Amount\n
         * enemies' bullets' lists\n
         * enemies' list. \n
         * enemies' lives\n
        '''
        master.otherAttack_x = []
        master.otherAttack_y = []
        master.enemy_x_list = []
        master.enemy_y_list = []
        master.enemyLifeList = []

    def init_planeAmount(master,):
        '''
        @ master: The class you want to init 
        A fuc used to init\n
         * players' wigs' color\n
         * players' plane's body's color\n
         * players are moving or not\n
         * The amount of the players
         * The speed of the players
        '''
        master.mov = False
        master.planeColor_player = tools.file.uiConfig("planeColor_player")
        master.wigColor_player = tools.file.uiConfig("wigColor_player")
        master.planeColor_enemy = tools.file.uiConfig("planeColor_enemy")
        master.wigColor_enemy = tools.file.uiConfig("wigColor_enemy")
        master.planeAmount = random.randint(10, 30)
        master.speed = 0

    def init_screen(master,):
        '''
        @ master: The class you want to init 
        A fuc used to init\n
         * screen color\n
         * screen height\n
         * screen height\n
         * The speed of the enemies
         * The font
        '''
        master.message = []
        master.buttonColor= tools.file.uiConfig("buttonColor")
        master.bloodColor = [255,0,0]
        master.bulletIconColor = [100,100,100]
        master.fontPath = tools.file.sourceConfig("fontPath")
        master.startPhotoPath = tools.file.sourceConfig("startPhotoPath")
        master.font = pygame.font.Font(
            tools.file.sourceConfig("fontPath"), tools.file.sourceConfig("fontSize"))
        
        master.screenWidth = tools.file.config("screenWidth")
        master.screenHeight = tools.file.config("screenHeight")
        master.movAmount = 5
        # make the frame resizeable
        pygame.RESIZABLE = True

    def initStone(master,):
        '''
        @ master: The class you want to init 
        A fuc used to init\n
         * stone x\n
         * stone y\n
        '''
        master.stoneXList = []
        master.stoneYList = []

    def init_players(master,):
        '''
        @ master: The class you want to init 
        A fuc used to init\n
         * The color of the fire\n
         * The players' life\n
         * The players' x\n
         * The players' y\n
         * The fuel of the players\n
         * The list of the strings that players has sent out\n
         * The score of the players
        '''
        master.fire = tools.file.uiConfig("fire")
        master.playing = True
        master.player1_life = tools.file.configPlayers("player1_life")
        master.player2_life = tools.file.configPlayers("player2_life")
        master.player2_bullet = master.planeAmount * 20 + 10
        master.player1_bullet = master.planeAmount * 20 + 10
        master.score = tools.file.configPlayers("score")
        master.attackXList = []
        master.attackYList = []
        master.playerxList = [tools.file.configPlayers("player1_x")]
        master.playeryList = [tools.file.configPlayers("player1_y")]
        master.player1_fuel = 1
        master.control = 0
        master.frame_player1 = 0
        master.frame_player2 = 0
        master.wigman = False

    def init_fps(master, fps=15):
        '''
        @ master: The class you want to init 
        A fuc used to init\n
         * version of the game
         * The fpsof the game
        '''
        master.version = tools.file.config("version")
        master.fps = tools.file.config("fps")