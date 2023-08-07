import pygame
import time
import random
from blur import blur
from ui import ui
import sys
from music import music
from init import init
from restorer import restorer
from kernel import programme
from tools import tools
import _thread
import os

'''
 *                                         ,s555SB@@&                          
 *                                      :9H####@@@@@Xi                        
 *                                     1@@@@@@@@@@@@@@8                       
 *                                   ,8@@@@@@@@@B@@@@@@8                      
 *                                  :B@@@@X3hi8Bs;B@@@@@Ah,                   
 *             ,8i                  r@@@B:     1S ,M@@@@@@#8;                 
 *            1AB35.i:               X@@8 .   SGhr ,A@@@@@@@@S                
 *            1@h31MX8                18Hhh3i .i3r ,A@@@@@@@@@5               
 *            ;@&i,58r5                 rGSS:     :B@@@@@@@@@@A               
 *             1#i  . 9i                 hX.  .: .5@@@@@@@@@@@1               
 *              sG1,  ,G53s.              9#Xi;hS5 3B@@@@@@@B1                
 *               .h8h.,A@@@MXSs,           #@H1:    3ssSSX@1                  
 *               s ,@@@@@@@@@@@@Xhi,       r#@@X1s9M8    .GA981               
 *               ,. rS8H#@@@@@@@@@@#HG51;.  .h31i;9@r    .8@@@@BS;i;          
 *                .19AXXXAB@@@@@@@@@@@@@@#MHXG893hrX#XGGXM@@@@@@@@@@MS        
 *                s@@MM@@@hsX#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&,      
 *              :GB@#3G@@Brs ,1GM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B,     
 *            .hM@@@#@@#MX 51  r;iSGAM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@8     
 *          :3B@@@@@@@@@@@&9@h :Gs   .;sSXH@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:    
 *      s&HA#@@@@@@@@@@@@@@M89A;.8S.       ,r3@@@@@@@@@@@@@@@@@@@@@@@@@@@r    
 *   ,13B@@@@@@@@@@@@@@@@@@@5 5B3 ;.         ;@@@@@@@@@@@@@@@@@@@@@@@@@@@i    
 *  5#@@#&@@@@@@@@@@@@@@@@@@9  .39:          ;@@@@@@@@@@@@@@@@@@@@@@@@@@@;    
 *  9@@@X:MM@@@@@@@@@@@@@@@#;    ;31.         H@@@@@@@@@@@@@@@@@@@@@@@@@@:    
 *   SH#@B9.rM@@@@@@@@@@@@@B       :.         3@@@@@@@@@@@@@@@@@@@@@@@@@@5    
 *     ,:.   9@@@@@@@@@@@#HB5                 .M@@@@@@@@@@@@@@@@@@@@@@@@@B    
 *           ,ssirhSM@&1;i19911i,.             s@@@@@@@@@@@@@@@@@@@@@@@@@@S   
 *              ,,,rHAri1h1rh&@#353Sh:          8@@@@@@@@@@@@@@@@@@@@@@@@@#:  
 *            .A3hH@#5S553&@@#h   i:i9S          #@@@@@@@@@@@@@@@@@@@@@@@@@A.
 *
 *
 *    又看源码，看你妹妹呀！
'''


class start(object):
    '''
        @ string: the text you want to print at the topbar.\n
        A fuc used to draw the toopbar
        '''
    def detect_restores(self):
        """
        @ self: self
        This fuc is used to restore the backup of the game.
        """
        files = os.listdir("./save")
        if files != []:
            return True
        else:
            return False
    def topbar(self, string: str = ""):
        pygame.draw.rect(self.screen, [25, 25, 25], [
                         0, 0, 500, 50], border_radius=10)
        start.print_screen(
            self, string, pos=(230, 10), color='#FDFDFD')
        self.screen.blit(self.backIconPath, (10, 10))

    def bind_topbar(x, y, event):
        '''
        detect if the button has benn pressed
        '''
        if x > 10 and x < 50 and y > 10 and y < 40 and event.type == pygame.MOUSEBUTTONUP:
            return True
        return False

    def startPage(self):
        x = 140
        y = 45
        width = 215
        height = 165
        value = 200
        while x > 0 and y > 0:
            x -= 4
            y -= 1
            value -= 4
            width += 8
            for index in range(256):
                pygame.draw.rect(self.screen, [255, 0, 0], [
                                 index, 0, 10, 10], border_radius=2)
            height += 10
            self.screen.fill([0, 0, 0])
            pygame.draw.rect(self.screen, [value, 0, 0], [
                             x, y, width, height], border_radius=10)
            self.font = pygame.font.Font(
                self.fontPath, 70)
            self.screen.blit(self.font.render(
                f"Plane", True, 'WHITE'), (150, 50))
            self.screen.blit(self.font.render(
                f"War", True, 'WHITE'), (180, 130))
            # 重新设置字体
            self.font = pygame.font.Font(
                self.fontPath, 20)
            self.screen.blit(self.font.render(
                f"{self.version}", True, 'white'), (0, 470))
            self.screen.blit(pygame.image.load(self.startPhotoPath), (120, 220))
            pygame.display.update()
        self.screen.fill([0, 0, 0])

    def init_start(self):
        pygame.display.set_caption(f"Plane War{self.version}")
        # 初始化屏幕为黑色
        start.startPage(self,)
        ui.switchAnimation(self,)
        # 显示标题&&标题背景

    def draw_button(self, pos: int = 250, type: str = 'active'):
        '''
        @pos: The pos you want to draw at.\n
        @type: The situation the button are.\n
        This is a fuction used to draw a button(without text) on.
        '''
        # draw when active
        if type == 'active':
            pygame.draw.rect(self.screen, self.buttonColor, [
                100, pos, 300, 50], border_radius=8)
        # draw the inactive button
        if type == 'inactive':
            pygame.draw.rect(self.screen, self.buttonColor, [
                100, 250, 300, 50], border_radius=8)

    def cover_button(self, pos: int = 250):
        pygame.draw.rect(self.screen, [0, 0, 0], [
            100, pos, 300, 50])

    def print_screen(self, string: str = "", pos: list = (210, 260), color: str = '#CCCCCC'):
        '''
        @ string: The str you want to print.\n
        @ pos: The pos you want to print at.\n
        @ color: The color the text will be.\n
        This fuction is used to print a line of string on pygame screen.
        '''
        self.screen.blit(self.font.render(
            string, True, color), pos)

    def draw_star(self):
        '''
        A fuction used to draw stars on your screen\n
        The maximum amount of the stars: 50\n
        '''
        # fill the stars
        minAmount = 0
        indexStar = 0
        while indexStar < 50:
            pygame.draw.rect(self.screen, [0, 0, 0], [
                self.starXList[indexStar], self.starYList[indexStar], 1, 1])
            indexStar += 1
        # move the stars
        indexStar = 0
        while indexStar < 50:
            self.starYList[indexStar] += self.movAmount
            indexStar += 1
        indexStar = 0
        # draw the stars
        while indexStar < 50:
            pygame.draw.rect(self.screen, [255, 255, 255], [
                self.starXList[indexStar], self.starYList[indexStar], 1, 1])
            indexStar += 1
        # bind stars
        indexStar = 0
        for i in range(50):
            if self.starYList[indexStar] > self.screenHeight:
                minAmount += 1
                del self.starYList[indexStar]
                del self.starXList[indexStar]
                indexStar -= 1
            indexStar += 1
        self.starYList = self.starYList[:50-minAmount]
        self.starXList = self.starXList[:50-minAmount]
        # add stars
        indexStar = 0
        while indexStar < minAmount:
            self.starYList.insert(0, random.randint(0, 15))
            self.starXList.insert(
                0, random.randint(0, self.screenWidth))
            indexStar += 1

    def button_setting(self, type='inactive'):
        '''
        @ type: The situation the button is ["active","inactive"]\n
        a fuction used to draw setting button\n
        '''
        # draw the button when inactive
        pygame.draw.rect(self.screen, self.buttonColor, [
            460, 450, 30, 30], border_radius=3)
        pygame.draw.rect(self.screen, self.buttonColor, [
            457, 453, 3, 24], border_radius=3)
        pygame.draw.rect(self.screen, self.buttonColor, [
            490, 453, 3, 24], border_radius=3)
        # draw the button when active

    def draw_switch(self, situation: str, pos: list,):
        '''
        @ situation: The situation the button is.["active","inactive"]\n
        @ pos: The pos the button is.\n
        @ : Scrolledbar will use it.\n
        a fuction used to draw switch.
        '''
        # judge if the space is enough for the elements to draw
        if + pos[1] >= 50:
            if situation == True:
                pygame.draw.circle(self.screen, [200, 100, 100], [
                                   pos[0], pos[1]+5], 12)
                pygame.draw.circle(self.screen, [200, 100, 100], [
                                   pos[0]+20, pos[1]+5], 12)
                pygame.draw.rect(self.screen, [200, 100, 100], [
                                 pos[0], pos[1]-7, 20, 24])
                pygame.draw.circle(self.screen, [255, 255, 255], [
                                   pos[0]+20, pos[1]+5], 8)
            if situation == False:
                pygame.draw.circle(self.screen, [100, 100, 100], [
                                   pos[0], pos[1]+5], 12)
                pygame.draw.circle(self.screen, [100, 100, 100], [
                                   pos[0]+20, pos[1]+5], 12)
                pygame.draw.rect(self.screen, [100, 100, 100], [
                                 pos[0], pos[1]-7, 20, 24])
                pygame.draw.circle(self.screen, [255, 255, 255], [
                                   pos[0], pos[1]+5], 8)

    def bind_switch(self, event: str, pos: list, ) -> bool:
        '''
        @ event: The event you get
        @ pos: The pos the switch at.
        @ : Scrolledbar will use it.\n
        A fuction used to draw switch.
        '''
        # bind the switch
        if event.type == pygame.MOUSEBUTTONUP and + pos[1] >= 30:
            try:
                if pygame.mouse.get_pos()[0] >= pos[0]-5 and pygame.mouse.get_pos()[0] <= pos[0]+30 and pygame.mouse.get_pos()[1] >= pos[1]-5 and pygame.mouse.get_pos()[1] <= pos[1]+24:
                    return True
            except:
                return None

            return False

    def chooser_graghic(self, screen):
        x = 0
        y = 0
        # init the colors
        down = False
        for event in pygame.event.get():
            # bind the events
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                down = True
            if event.type == pygame.MOUSEBUTTONUP:
                down = False
                if x > 10 and x < 490 and y > 410 and y < 490:
                    return [r, g, b]
            if down:
                x, y = pygame.mouse.get_pos()
                if x >= 20 and x <= 220:
                    print("True")
                    if y >= 25 and y <= 55:
                        r = x-20
                    if y >= 55 and y <= 65:
                        g = x-20
                    if y >= 85 and y <= 95:
                        print(y)
                        b = x-20

    def colorChooser(self, screen):
        '''
        简陋的选色器
        @ screen: The screen the colorchooser will appear in.
        '''
        r = 0
        b = 0
        g = 0
        running = True

        while running:

            screen.fill([r, g, b])
            # draw the chooser frame
            pygame.draw.rect(screen, [255, 235, 235], [
                             20, 25, 200, 16], border_radius=3)
            pygame.draw.rect(screen, [235, 255, 235], [
                             20, 55, 200, 16], border_radius=3)
            pygame.draw.rect(screen, [235, 235, 255], [
                             20, 85, 200, 16], border_radius=3)
            # draw the circle border
            pygame.draw.circle(screen, [255, 235, 235], [20, 33], 8)
            pygame.draw.circle(screen, [235, 255, 235], [20, 63], 8)
            pygame.draw.circle(screen, [235, 235, 255], [20, 93], 8)
            pygame.draw.circle(screen, [255, 235, 235], [220, 33], 8)
            pygame.draw.circle(screen, [235, 255, 235], [220, 63], 8)
            pygame.draw.circle(screen, [235, 235, 255], [220, 93], 8)
            pygame.draw.circle(screen, [r, g, b], [20+r, 33], 8)
            pygame.draw.circle(screen, [r, g, b], [20+g, 63], 8)
            pygame.draw.circle(screen, [r, g, b], [20+b, 93], 8)
            pygame.draw.rect(screen, [155, 155, 155], [
                             10, 420, 480, 70], border_radius=3)

    def switch(self, situation: str, pos: list, text: str, ):
        """
        @ situation: The status the switch is.
        @ pos: The pos the switch is at.
        @ text: The text you want to show next to the switch
        @ : The scrolledbar will soon use it.\n
        A fuction used to draw a switch
        """
        start.draw_switch(self,
                          situation, [pos[0]+360, pos[1]+10], )
        start.print_screen(self, text, pos, color='white')

    def draw_addbox(self, value, pos, text, ):
        """
        @ value: The number you want to show in the addbox.
        @ pos: The pos the addbox is at.
        @ text: The text you want to show at the pos the addbox at
        @ : Scrolledbar will soon use it.\n
        A fuction used to draw addbox.
        """
        start.print_screen(self, text, pos, color='white')
        if value <= 0:
            pygame.draw.rect(self.screen, [150, 100, 100], [
                             pos[0]+330, pos[1], 20, 20], border_radius=3)
        else:
            pygame.draw.rect(self.screen, [200, 100, 100], [
                             pos[0]+330, pos[1], 20, 20], border_radius=3)
        pygame.draw.rect(self.screen, [200, 100, 100], [
                         pos[0]+352, pos[1], 40, 20], border_radius=3)
        pygame.draw.rect(self.screen, [200, 100, 100], [
                         pos[0]+394, pos[1], 20, 20], border_radius=3)
        start.print_screen(self,
                           "-", [pos[0]+335, pos[1]-5], color='white')
        start.print_screen(self,
                           "+", [pos[0]+398, pos[1]-6], color='white')
        start.print_screen(self,
                           str(value), [pos[0]+356, pos[1]-4], color='white')

    def bind_addbox(self, pos: list) -> int:
        """
        @ pos: The pos the addbox at\n
        A fuction used to bind addbox.
        """
        try:
            [pos1, pos2] = pygame.mouse.get_pos()
        except:
            return 0
        if pos1 > pos[0]+330 and pos1 < pos[0]+350 and pos2 > pos[1] and pos2 < pos[1]+20:
            return -1
        elif pos1 > pos[0]+394 and pos1 < pos[0]+414 and pos2 > pos[1] and pos2 < pos[1]+20:
            return 1
        else:
            return 0

    def setting(self,):
        """
        The setting userface
        """
        running = True

        while running:
            self.screen.fill([0, 0, 0])
            pygame.draw.rect(self.screen, [70, 70, 70], [
                             30, 80, 440, 50], border_radius=5)
            pygame.draw.rect(self.screen, [70, 70, 70], [
                             30, 135, 440, 50], border_radius=5)
            pygame.draw.rect(self.screen, [70, 70, 70], [
                             30, 190, 440, 50], border_radius=5)
            pygame.draw.rect(self.screen, [70, 70, 70], [
                             30, 245, 440, 50], border_radius=5)
            start.topbar(self, "Setting")
            start.switch(self, self.god, pos=(38, 100),
                         text="作弊模式", )
            start.draw_addbox(self, self.player1_bullet,
                              (40, 153), "玩家一子弹数量", )
            start.draw_addbox(self, self.player2_bullet,
                              (40, 203), "玩家二子弹数量", )
            start.draw_addbox(self, self.movAmount,
                              (40, 253,), "敌人移动速度", )
            start.print_screen(
                self, "玩家机身颜色", (40, 300), color='white')
            start.print_screen(
                self, "玩家机翼颜色", (40, 350), color='white')
            pygame.draw.rect(self.screen, self.planeColor_player, [
                365, 300, 80, 40], border_radius=3)
            pygame.draw.rect(self.screen, self.wigColor_player, [
                365, 350, 80, 40], border_radius=3)
            start.switch(self, self.blur, (40, 400), "模糊效果", )
            start.switch(self, self.music, (40, 450), "音乐", )
            pygame.draw.rect(self.screen, self.planeColor_player, [
                365, 300, 80, 40], border_radius=3)
            pygame.draw.rect(self.screen, self.wigColor_player, [
                365, 350, 80, 40], border_radius=3)
            for m in self.graghicCommand:
                if m == "colorchose_planeColor":
                    self.planeColor_player = start.colorChooser(self,
                                                                self.screen)
                    start.chooser_graghic(self, self.screen)
                if m == "colorchose_wigColor":
                    self.wigColor_player = start.colorChooser(self,
                                                              self.screen)
                    start.chooser_graghic(self, self.screen)

            pygame.display.update()

    def about(self) -> None:
        '''
        It shows the about page
        '''
        self.screen.fill([0, 0, 0])
        pygame.draw.rect(self.screen, [232, 64, 38], [0, 90, 500, 90])
        start.topbar(self, "About")
        self.font = pygame.font.Font(self.fontPath, 60)
        start.print_screen(self, "Plane War", (100, 100), 'white')
        self.font = pygame.font.Font(self.fontPath, 15)
        paragraghLists = tools.file.readFile("about.txt", 0, 9)
        pygame.draw.rect(self.screen, [45, 45, 45], [
                         50, 190, 400, 280], border_radius=10)
        plist = []
        m = ''
        for moderate in paragraghLists:
            if moderate == '\n':
                plist.append(m)
                m = ''
                continue
            m += moderate
        plist.append(m)
        coordinate = 200
        for m in plist:
            start.print_screen(self, m, (60, coordinate), '#F1F3F5')
            coordinate += 20
        pygame.display.update()

        while True:
            for e in pygame.event.get():
                try:
                    x, y = pygame.mouse.get_pos()
                except:
                    pass
                if x > 10 and x < 50 and y > 10 and y < 40 and e.type == pygame.MOUSEBUTTONUP:
                    return 0
                if e.type == pygame.QUIT:
                    quit()

    def kernel(self,) -> bool:
        '''
        The start of this game\n
        Size:500x500\n
        Module: random,pygame,time.\n
        created in 2022 in Shangrao
        '''
        self.message = []
        self.message.append("start")
        startPage = True
        _thread.start_new_thread(start.start_graghic.kernel, (self, ""))
        while self.running:
            # self 函数主循环
            # 获取事件

            for event in pygame.event.get():
                # 退出检测
                try:
                    x, y = pygame.mouse.get_pos()
                except:
                    continue
                if event.type == pygame.QUIT:
                    self.running = False
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if x >= 100 and x <= 400 and startPage:
                        if y >= 220 and y <= 280:
                            startPage = False
                            self.message.append("single")
                            self.runningP = True
                            r = programme.main(self, True, False)
                            init.init_restart(self)
                            try:
                                start.start_graghic.finishPage(
                                    self, r[0], True if r[1] == 'win' else False)
                            except:
                                pass
                            time.sleep(1)
                            startPage = True
                        if y > 290 and y <= 350:
                            startPage = False
                            self.player2 = True
                            init.init_restart(self)
                            self.message.append("double")
                            self.runningP = True
                            r = programme.main(self, True, True)
                            time.sleep(1)
                            startPage = True
                        if y > 360 and y < 420:
                            startPage = False
                            self.message.append("setting")
                            running = True
                            q = False
                            while running:
                                for event in pygame.event.get():
                                    # 退出检测
                                    try:
                                        x, y = pygame.mouse.get_pos()
                                    except:
                                        continue
                                    if event.type == pygame.QUIT:
                                        self.running = False
                                        quit()
                                    if event.type == pygame.MOUSEMOTION:
                                        # 获取鼠标位置
                                        try:
                                            x, y = pygame.mouse.get_pos()
                                        except:
                                            continue
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        get = start.bind_switch(self,
                                                                event, pos=(400, 100), )
                                        getBlur = start.bind_switch(self,
                                                                    event, pos=(400, 400), )
                                        getMusic = start.bind_switch(self,
                                                                     event, pos=(400, 450), )
                                        self.player2_bullet += start.bind_addbox(
                                            self, (40, 200))
                                        self.player1_bullet += start.bind_addbox(
                                            self, (40, 150))
                                        self.movAmount += start.bind_addbox(
                                            self, (40, 250))
                                        if get != None:
                                            self.god = get if self.god != True else False
                                        if getBlur != None:
                                            self.blur = getBlur if self.blur != getBlur else self.blur
                                        if getMusic != None:
                                            self.music = getMusic if self.music != getMusic else self.music
                                            if not self.music:
                                                music.pause()
                                            else:
                                                try:
                                                    music.play()
                                                finally:
                                                    pass
                                            getMusic = None
                                        if x > 10 and x < 50 and y > 10 and y < 40:
                                            q = True
                                            break

                                        if x > 365 and x <= 480 and y > 300 and y <= 340:
                                            self.graghicCommand.append(
                                                "colorchose_planeColor")

                                        if x > 365 and x <= 480 and y > 350 and y <= 390:
                                            self.graghicCommand.append(
                                                "colorchose_wigColor")
                                if q:
                                    startPage = True
                                    break
                            startPage = True

                        if y > 420 and y < 460:
                            startPage = False
                            self.message.append("about")
                if x > 10 and x < 50 and y > 10 and y < 40 and event.type == pygame.MOUSEBUTTONDOWN:
                    startPage = True
                    self.runningP = False

    class start_graghic():
        '''
        This class is used to store the graghic parts of the start.
        '''

        def finishPage(self, score, win):
            '''
            This is the finish page of the game
            '''

            blurList = blur.get(self.screen, 10, 490, 10, 490)
            s = blur(blurList, 480)
            blur.kernel(s, 0)
            blur.blender(s, self.screen, 480, 0, 10)
            start.print_screen(self, f"Score:{score}", (20, 20), color='white')
            victory = "win"if win == True else "lose"
            start.print_screen(self, f"you {victory}", (20, 50), color='white')
            pygame.display.update()
            time.sleep(1)

        def startPage_graghic(self):
            pygame.draw.rect(self.screen, [232, 64, 38], [
                             00, 40, 500, 70])
            self.font = pygame.font.Font(
                self.fontPath, 40)
            self.screen.blit(self.font.render(
                f"Plane War", True, 'WHITE'), (150, 50))
            # 重新设置字体
            self.font = pygame.font.Font(
                self.fontPath, 20)
            self.screen.blit(self.font.render(
                f"{self.version}", True, 'white'), (0, 470))
            start.draw_button(self, pos=220, type='active')
            start.draw_button(self, pos=290, type='active')
            start.draw_button(self, pos=360, type='active')
            start.draw_button(self, pos=420, type='active')
            self.screen.blit(self.settingIconPath, (103, 363))
            self.screen.blit(self.singleIconPath, (105, 215))
            self.screen.blit(self.doubleIconPath, (105, 284))
            self.screen.blit(self.aboutIconPath, (103, 423))
            start.print_screen(self, "关于", (220, 430))
            start.print_screen(self, "设置", (220, 370))
            start.print_screen(self, "单人模式", (210, 230))
            start.print_screen(self, "双人模式", (210, 300))
            pygame.draw.rect(self.screen, [212, 64, 38], [
                             00, 40, 500, 70])
            self.font = pygame.font.Font(
                self.fontPath, 40)
            self.screen.blit(self.font.render(
                f"Plane War", True, 'WHITE'), (150, 50))
            # 重新设置字体
            self.font = pygame.font.Font(
                self.fontPath, 20)
            self.screen.blit(self.font.render(
                f"{self.version}", True, 'white'), (0, 470))

        def kernel(self, a: str):
            '''
            The main programme of this class
            The graghic programme if the start page.
            '''
            start.startPage(self)
            startPage = True
            setting = False
            aboutPage = False
            while self.running:
                time.sleep(0.05)
                for m in self.message:
                    if m == 'start' and startPage != True:
                        del self.message[self.message.index(m)]
                        ui.switchAnimation(self)
                        startPage = True
                    if m == 'setting' and setting != True:
                        del self.message[self.message.index(m)]
                        startPage = False
                        setting = True
                        aboutPage = False
                    if m == 'about' and aboutPage != True:
                        del self.message[self.message.index(m)]
                        ui.switchAnimation(self)
                        aboutPage = True
                        startPage = False
                        setting = False
                    if m == 'single':
                        del self.message[self.message.index(m)]
                        ui.switchAnimation(self)
                        programme.graphics(self, True, False)
                        ui.switchAnimation(self)
                    if m == 'double':
                        del self.message[self.message.index(m)]
                        ui.switchAnimation(self)
                        programme.graphics(self, True, True)
                        ui.switchAnimation(self)
                    if m == 'switch':
                        del self.message[self.message.index(m)]
                        ui.switchAnimation(self)
                        startPage = True
                        setting = False
                        aboutPage = False
                start.draw_star(self,)
                if startPage:
                    aboutPage = False
                    setting = False
                    time.sleep(0.01)
                    start.start_graghic.startPage_graghic(self)
                if setting:
                    ui.switchAnimation(self)
                    start.setting(self)
                    ui.switchAnimation(self)
                    setting = False
                    startPage = True
                if aboutPage:
                    start.about(self)
                    ui.switchAnimation(self)
                    aboutPage = False
                    startPage = True
                pygame.display.update()

    
if __name__ == '__main__':
    inputArg = sys.argv[1]
    if inputArg == '-e':
        from editor import editor
        s = editor()
        editor.main(s)
        quit()
    elif inputArg == '-h' or inputArg == '--help':
        print('''
Thank you for using Plane War!
CLI Commands:
-e            plane war theme editor
-h            help page
''')
        quit()
    elif inputArg == 'start':
        pass
    else:
        print('''
Thank you for using Plane War!
add -h to start help page
''')
        quit()
    self = programme()
    init.init(self)
    if  start.detect_restores(self):
        answer=restorer.askRestores(self)
        if type(answer) == int:
            print(os.listdir('./save')[answer-1])
            restoreFile = f"./save/{os.listdir('./save')[answer-1]}"
            init.restore(self,restoreFile)
    pygame.display.set_caption(f"Plane War {self.version}")
    self.screen = pygame.display.set_mode((tools.file.config("screenWidth"),tools.file.config("screenHeight")))
    self.screen.fill(tools.file.uiConfig("initColor"))
    start.kernel(self)
