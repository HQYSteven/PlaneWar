import pygame
import time
import random
from ui import ui
from pygame import RESIZABLE

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


class entrance(object):
    def startPage(self):
        self.screen.fill([0, 0, 0])
        self.font = pygame.font.Font(
            "default.ttf", 70)
        self.screen.blit(self.font.render(
            f"Plane", True, 'WHITE'), (150, 50))
        self.screen.blit(self.font.render(
            f"War", True, 'WHITE'), (180, 130))
        # 重新设置字体
        self.font = pygame.font.Font(
            "default.ttf", 20)
        self.screen.blit(self.font.render(
            f"{self.version}", True, 'white'), (0, 470))
        pygame.display.update()

    def init_entrance(self):
        pygame.display.set_caption(f"Plane War{self.version}")
        # 初始化屏幕为黑色
        entrance.startPage(self,)
        ui.switchAnimation(self,)
        # 显示标题&&标题背景

    def draw_button(self,pos=250, type='active'):
        if type == 'active':
            pygame.draw.rect(self.screen, [135, 206, 250], [
                100, pos, 300, 50])
            pygame.draw.circle(
                self.screen, [135, 206, 250], [100, pos+20], 20)
            pygame.draw.circle(
                self.screen, [135, 206, 250], [400, pos+30], 20)
            pygame.draw.circle(
                self.screen, [135, 206, 250], [100, pos+30], 20)
            pygame.draw.circle(
                self.screen, [135, 206, 250], [400, pos+20], 20)
        if type == 'inactive':
            pygame.draw.rect(self.screen, [135, 206, 235], [
                100, 250, 300, 50])
            pygame.draw.circle(
                self.screen, [135, 206, 235], [100, 270], 20)
            pygame.draw.circle(
                self.screen, [135, 206, 235], [400, 280], 20)
            pygame.draw.circle(
                self.screen, [135, 206, 235], [100, 280], 20)
            pygame.draw.circle(
                self.screen, [135, 206, 235], [400, 270], 20)

    def cover_button(self,pos=250):
        pygame.draw.rect(self.screen, [0, 0, 0], [
            100, pos, 300, 50])
        pygame.draw.circle(
            self.screen, [0, 0, 0], [100, pos+20], 20)
        pygame.draw.circle(
            self.screen, [0, 0, 0], [400, pos+30], 20)
        pygame.draw.circle(
            self.screen, [0, 0, 0], [100, pos+30], 20)
        pygame.draw.circle(
            self.screen, [0, 0, 0], [400, pos+20], 20)

    def print_screen(self,string="", pos=(210, 260), color='black'):
        self.screen.blit(self.font.render(
            string, True, color), pos)

    def draw_star(self,):
        minAmount = 0
        indexStar = 0
        while indexStar < 50:
            pygame.draw.rect(self.screen, [0, 0, 0], [
                self.starXList[indexStar], self.starYList[indexStar], 1, 1])
            indexStar += 1
        indexStar = 0
        while indexStar < 50:
            self.starYList[indexStar] += self.movAmount
            indexStar += 1
        indexStar = 0
        while indexStar < 50:
            pygame.draw.rect(self.screen, [255, 255, 255], [
                self.starXList[indexStar], self.starYList[indexStar], 1, 1])
            indexStar += 1
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
        indexStar = 0
        while indexStar < minAmount:
            self.starYList.insert(0, random.randint(0, 15))
            self.starXList.insert(
                0, random.randint(0, self.screenWidth))
            indexStar += 1

    def button_setting(self,type='inactive'):
        if type == "inactive":
            pygame.draw.rect(self.screen, [135, 206, 235], [
                460, 450, 30, 30])
            pygame.draw.circle(
                self.screen, [135, 206, 235], [490, 453], 3)
            pygame.draw.circle(
                self.screen, [135, 206, 235], [460, 453], 3)
            pygame.draw.circle(
                self.screen, [135, 206, 235], [490, 477], 3)
            pygame.draw.circle(
                self.screen, [135, 206, 235], [460, 477], 3)
            pygame.draw.rect(self.screen, [135, 206, 235], [
                457, 453, 3, 24])
            pygame.draw.rect(self.screen, [135, 206, 235], [
                490, 453, 3, 24])
        if type == "active":
            pygame.draw.rect(self.screen, [135, 206, 250], [
                460, 450, 30, 30])
            pygame.draw.circle(
                self.screen, [135, 206, 250], [490, 453], 3)
            pygame.draw.circle(
                self.screen, [135, 206, 250], [460, 453], 3)
            pygame.draw.circle(
                self.screen, [135, 206, 250], [490, 477], 3)
            pygame.draw.circle(
                self.screen, [135, 206, 250], [460, 477], 3)
            pygame.draw.rect(self.screen, [135, 206, 250], [
                457, 453, 3, 24])
            pygame.draw.rect(self.screen, [135, 206, 250], [
                490, 453, 3, 24])

    def draw_switch(self,situation, pos, position):
        if position + pos[1] >= 50:
            if situation == True:
                pygame.draw.circle(self.screen, [200, 100, 100], [
                                   pos[0], pos[1]+5+position], 12)
                pygame.draw.circle(self.screen, [200, 100, 100], [
                                   pos[0]+20, pos[1]+5+position], 12)
                pygame.draw.rect(self.screen, [200, 100, 100], [
                                 pos[0], pos[1]-7+position, 20, 24])
                pygame.draw.circle(self.screen, [255, 255, 255], [
                                   pos[0]+20, pos[1]+5+position], 8)
            if situation == False:
                pygame.draw.circle(self.screen, [100, 100, 100], [
                                   pos[0], pos[1]+5+position], 12)
                pygame.draw.circle(self.screen, [100, 100, 100], [
                                   pos[0]+20, pos[1]+5+position], 12)
                pygame.draw.rect(self.screen, [100, 100, 100], [
                                 pos[0], pos[1]-7+position, 20, 24])
                pygame.draw.circle(self.screen, [255, 255, 255], [
                                   pos[0], pos[1]+position+5], 8)

    def bind_switch(self,event, pos, position):
        if event.type == pygame.MOUSEBUTTONUP and position + pos[1] >= 30:
            try:
                if pygame.mouse.get_pos()[0] >= pos[0]-5 and pygame.mouse.get_pos()[0] <= pos[0]+30 and pygame.mouse.get_pos()[1] >= pos[1]-5+position and pygame.mouse.get_pos()[1] <= pos[1]+24+position:
                    return True
            except:
                return None
            return False

    def colorChooser(self,screen):
        '''
        简陋的选色器
        '''
        r = 0
        b = 0
        g = 0
        running = True
        x = 0
        y = 0
        down = False
        while running:
            for event in pygame.event.get():
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
            screen.fill([r, g, b])
            pygame.draw.rect(screen, [155, 155, 155], [20, 8, 200, 104])
            pygame.draw.circle(screen, [155, 155, 155], [20, 20], 12)
            pygame.draw.circle(screen, [155, 155, 155], [220, 20], 12)
            pygame.draw.circle(screen, [155, 155, 155], [220, 100], 12)
            pygame.draw.circle(screen, [155, 155, 155], [20, 100], 12)
            pygame.draw.rect(screen, [155, 155, 155], [8, 20, 12, 80])
            pygame.draw.rect(screen, [155, 155, 155], [220, 20, 12, 80])
            pygame.draw.rect(screen, [255, 235, 235], [20, 25, 200, 16])
            pygame.draw.rect(screen, [235, 255, 235], [20, 55, 200, 16])
            pygame.draw.rect(screen, [235, 235, 255], [20, 85, 200, 16])
            pygame.draw.circle(screen, [255, 235, 235], [20, 33], 8)
            pygame.draw.circle(screen, [235, 255, 235], [20, 63], 8)
            pygame.draw.circle(screen, [235, 235, 255], [20, 93], 8)
            pygame.draw.circle(screen, [255, 235, 235], [220, 33], 8)
            pygame.draw.circle(screen, [235, 255, 235], [220, 63], 8)
            pygame.draw.circle(screen, [235, 235, 255], [220, 93], 8)
            pygame.draw.circle(screen, [r, g, b], [20+r, 33], 8)
            pygame.draw.circle(screen, [r, g, b], [20+g, 63], 8)
            pygame.draw.circle(screen, [r, g, b], [20+b, 93], 8)
            pygame.draw.rect(screen, [155, 155, 155], [10, 420, 480, 70])
            pygame.display.update()

    def switch(self,situation, pos, text, position):
        entrance.draw_switch(self,
            situation, [pos[0]+360, pos[1]+10], position=position)
        entrance.print_screen(self,text, pos, color='white')

    def draw_addbox(self,value, pos, text, position):
        entrance.print_screen(self,text, pos, color='white')
        if value <= 0:
            pygame.draw.rect(self.screen, [150, 100, 100], [
                             pos[0]+330, pos[1]+position, 20, 20])
        else:
            pygame.draw.rect(self.screen, [200, 100, 100], [
                             pos[0]+330, pos[1]+position, 20, 20])
        pygame.draw.rect(self.screen, [200, 100, 100], [
                         pos[0]+352, pos[1]+position, 40, 20])
        pygame.draw.rect(self.screen, [200, 100, 100], [
                         pos[0]+394, pos[1]+position, 20, 20])
        entrance.print_screen(self,
            "-", [pos[0]+335, pos[1]-5+position], color='white')
        entrance.print_screen(self,
            "+", [pos[0]+398, pos[1]-6+position], color='white')
        entrance.print_screen(self,
            str(value), [pos[0]+356, pos[1]-4+position], color='white')

    def bind_addbox(self,pos):
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
    # Doing: ScrolledBar
    # position is the length the texts scrolled up
    # pos is the pos if th e bar
    # length is the length if the scrolledbar
    '''def scrolledBar(pos,length,position):
        pygame.draw.rect(self.screen,[200,100,100],[pos[0],pos[1],20,500])
        buttonHeight = int(2500/length)
        buttonPos = int(-position * 500/length)
        pygame.draw.rect(self.screen,[220,100,100],[pos[0],pos[1],20,buttonHeight])'''
    def setting(self,):
        ui.switchAnimation(self,)
        position = 0
        running = True
        while running:
            time.sleep(0.04)
            self.screen.fill([0, 0, 0])
            entrance.draw_star(self,)
            pygame.draw.rect(self.screen, [255, 0, 0], [0, 0, 500, 50])
            entrance.print_screen(self,"Setting", pos=(230, 10), color='white')
            entrance.print_screen(self,"<", pos=(10, 10), color='white')
            entrance.switch(self,self.god, pos=(40, 100),
                            text="作弊模式", position=position)
            entrance.draw_addbox(self,self.player1_bullet,
                                 (40, 150+position), "玩家一子弹数量", position)
            entrance.draw_addbox(self,self.player2_bullet,
                                 (40, 200+position), "玩家二子弹数量", position)
            entrance.draw_addbox(self,self.movAmount,
                                 (40, 250,), "敌人移动速度", position=position)
            entrance.print_screen(self,"玩家机身颜色", (40, 300+position), color='white')
            entrance.print_screen(self,"玩家机翼颜色", (40, 350+position), color='white')
            pygame.draw.rect(self.screen, self.planeColor_player, [
                             365, 300+position, 80, 40])
            pygame.draw.rect(self.screen, self.wigColor_player, [
                             365, 350+position, 80, 40])
            entrance.switch(self,self.blur,(40,400),"模糊效果",position)
            for event in pygame.event.get():
                # 退出检测
                try:
                    x, y = pygame.mouse.get_pos()
                except:
                    continue
                if event.type == pygame.QUIT:
                    self.running = False
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    # 获取鼠标位置
                    try:
                        x, y = pygame.mouse.get_pos()
                    except:
                        continue
                if event.type == pygame.MOUSEBUTTONUP:
                    get = entrance.bind_switch(self,
                        event, pos=(400, 100), position=position)
                    getBlur = entrance.bind_switch(self,
                        event, pos=(400, 400), position=position)
                    self.player2_bullet += entrance.bind_addbox(self,(40, 200))
                    self.player1_bullet += entrance.bind_addbox(self,(40, 150))
                    self.movAmount += entrance.bind_addbox(self,(40, 250))
                    if get != None:
                        self.god = get if self.god != True else False
                    if getBlur != None:
                        self.blur = getBlur if self.god != True else False
                    if x > 365 and x <= 480 and y > 300+position and y <= 340+position:
                        self.planeColor_player = entrance.colorChooser(self,
                            self.screen)
                    if x > 365 and x <= 480 and y > 350+position and y+position <= 390:
                        self.wigColor_player = entrance.colorChooser(self,
                            self.screen)
                    if x > 10 and x < 50 and y+position > 10 and y+position < 40:
                        ui.switchAnimation(self,)
                        running = False

            pygame.display.update()

    def entrance(self,):
        
        while self.running:
            time.sleep(0.04)
            pygame.draw.rect(self.screen, [200, 0, 0], [00, 40, 500, 70])
            self.font = pygame.font.Font(
                "default.ttf", 40)
            self.screen.blit(self.font.render(
                f"Plane War", True, 'WHITE'), (150, 50))
            # 重新设置字体
            self.font = pygame.font.Font(
                "default.ttf", 20)
            self.screen.blit(self.font.render(
                f"{self.version}", True, 'white'), (0, 470))
            entrance.draw_button(self,pos=410, type='active')
            entrance.print_screen(self,"设置", (220, 420))
            entrance.draw_button(self,type='inactive')
            entrance.draw_button(self,pos=320, type='active')
            entrance.print_screen(self,"单人模式")
            entrance.print_screen(self,"双人模式", (210, 330))
            pygame.draw.rect(self.screen, [200, 0, 0], [00, 40, 500, 70])
            self.font = pygame.font.Font(
                "default.ttf", 40)
            self.screen.blit(self.font.render(
                f"Plane War", True, 'WHITE'), (150, 50))
            # 重新设置字体
            self.font = pygame.font.Font(
                "default.ttf", 20)
            self.screen.blit(self.font.render(
                f"{self.version}", True, 'white'), (0, 470))
            entrance.draw_star(self,)
            # self 函数主循环
            # 获取事件
            for event in pygame.event.get():
                # 退出检测
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x >= 100 and x <= 400:
                        if y >= 240 and y <= 310:
                            self.screen.fill([100, 100, 100])
                            self.running = False
                            return True,1
                        if y > 320 and y <= 390:
                            self.running = False
                            self.screen.fill([100, 100, 100])
                            self.player2 = True
                            return True,2
                        if y > 410 and y < 490:
                            entrance.setting(self,)
                if event.type == pygame.MOUSEBUTTONUP and x >= 460 and y > 450 and x <= 490 and y <= 480:
                    entrance.setting(self,)
                if event.type == pygame.MOUSEMOTION:
                    # 获取鼠标位置
                    try:
                        x, y = pygame.mouse.get_pos()
                    except:
                        continue

            pygame.display.update()


