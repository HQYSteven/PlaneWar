import pygame
import time
import random
from tools import programme
from tools import tools
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


def follow():
    pygame.display.init()
    screen = pygame.display.set_mode((500, 800), RESIZABLE)
    running = True
    x = 0
    y = 0
    screen.fill([255, 255, 255])
    pygame.display.update()
    while running:

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                quit()
            pygame.display.update()
        pygame.draw.circle(screen, [255, 255, 255], [x, y], 10)
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, [255, 0, 0], [x, y], 10)

### main programme###


class entrance(object):
    def startPage():
        programme.screen.fill([0, 0, 0])
        programme.font = pygame.font.Font(
            "default.ttf", 70)
        programme.screen.blit(programme.font.render(
            f"Plane", True, 'WHITE'), (150, 50))
        programme.screen.blit(programme.font.render(
            f"War", True, 'WHITE'), (180, 130))
        # 重新设置字体
        programme.font = pygame.font.Font(
            "default.ttf", 20)
        programme.screen.blit(programme.font.render(
            f"{programme.version}", True, 'white'), (0, 470))
        pygame.display.update()

    def init_entrance():
        pygame.display.set_caption(f"Plane War{programme.version}")
        # 初始化屏幕为黑色
        entrance.startPage()
        tools.ui.switchAnimation()
        # 显示标题&&标题背景

    def draw_button(pos=250, type='active'):
        if type == 'active':
            pygame.draw.rect(programme.screen, [135, 206, 250], [
                100, pos, 300, 50])
            pygame.draw.circle(
                programme.screen, [135, 206, 250], [100, pos+20], 20)
            pygame.draw.circle(
                programme.screen, [135, 206, 250], [400, pos+30], 20)
            pygame.draw.circle(
                programme.screen, [135, 206, 250], [100, pos+30], 20)
            pygame.draw.circle(
                programme.screen, [135, 206, 250], [400, pos+20], 20)
        if type == 'inactive':
            pygame.draw.rect(programme.screen, [135, 206, 235], [
                100, 250, 300, 50])
            pygame.draw.circle(
                programme.screen, [135, 206, 235], [100, 270], 20)
            pygame.draw.circle(
                programme.screen, [135, 206, 235], [400, 280], 20)
            pygame.draw.circle(
                programme.screen, [135, 206, 235], [100, 280], 20)
            pygame.draw.circle(
                programme.screen, [135, 206, 235], [400, 270], 20)

    def cover_button(pos=250):
        pygame.draw.rect(programme.screen, [0, 0, 0], [
            100, pos, 300, 50])
        pygame.draw.circle(
            programme.screen, [0, 0, 0], [100, pos+20], 20)
        pygame.draw.circle(
            programme.screen, [0, 0, 0], [400, pos+30], 20)
        pygame.draw.circle(
            programme.screen, [0, 0, 0], [100, pos+30], 20)
        pygame.draw.circle(
            programme.screen, [0, 0, 0], [400, pos+20], 20)

    def print_screen(string="", pos=(210, 260), color='black'):
        programme.screen.blit(programme.font.render(
            string, True, color), pos)

    def draw_star():
        minAmount = 0
        indexStar = 0
        while indexStar < 50:
            pygame.draw.rect(programme.screen, [0, 0, 0], [
                programme.starXList[indexStar], programme.starYList[indexStar], 1, 1])
            indexStar += 1
        indexStar = 0
        while indexStar < 50:
            programme.starYList[indexStar] += programme.movAmount
            indexStar += 1
        indexStar = 0
        while indexStar < 50:
            pygame.draw.rect(programme.screen, [255, 255, 255], [
                programme.starXList[indexStar], programme.starYList[indexStar], 1, 1])
            indexStar += 1
        indexStar = 0
        for i in range(50):
            if programme.starYList[indexStar] > programme.screenHeight:
                minAmount += 1
                del programme.starYList[indexStar]
                del programme.starXList[indexStar]
                indexStar -= 1
            indexStar += 1
        programme.starYList = programme.starYList[:50-minAmount]
        programme.starXList = programme.starXList[:50-minAmount]
        indexStar = 0
        while indexStar < minAmount:
            programme.starYList.insert(0, random.randint(0, 15))
            programme.starXList.insert(
                0, random.randint(0, programme.screenWidth))
            indexStar += 1

    def button_setting(type='inactive'):
        if type == "inactive":
            pygame.draw.rect(programme.screen, [135, 206, 235], [
                460, 450, 30, 30])
            pygame.draw.circle(
                programme.screen, [135, 206, 235], [490, 453], 3)
            pygame.draw.circle(
                programme.screen, [135, 206, 235], [460, 453], 3)
            pygame.draw.circle(
                programme.screen, [135, 206, 235], [490, 477], 3)
            pygame.draw.circle(
                programme.screen, [135, 206, 235], [460, 477], 3)
            pygame.draw.rect(programme.screen, [135, 206, 235], [
                457, 453, 3, 24])
            pygame.draw.rect(programme.screen, [135, 206, 235], [
                490, 453, 3, 24])
        if type == "active":
            pygame.draw.rect(programme.screen, [135, 206, 250], [
                460, 450, 30, 30])
            pygame.draw.circle(
                programme.screen, [135, 206, 250], [490, 453], 3)
            pygame.draw.circle(
                programme.screen, [135, 206, 250], [460, 453], 3)
            pygame.draw.circle(
                programme.screen, [135, 206, 250], [490, 477], 3)
            pygame.draw.circle(
                programme.screen, [135, 206, 250], [460, 477], 3)
            pygame.draw.rect(programme.screen, [135, 206, 250], [
                457, 453, 3, 24])
            pygame.draw.rect(programme.screen, [135, 206, 250], [
                490, 453, 3, 24])

    def draw_switch(situation, pos, position):
        if position + pos[1] >= 50:
            if situation == True:
                pygame.draw.circle(programme.screen, [200, 100, 100], [
                                   pos[0], pos[1]+5+position], 12)
                pygame.draw.circle(programme.screen, [200, 100, 100], [
                                   pos[0]+20, pos[1]+5+position], 12)
                pygame.draw.rect(programme.screen, [200, 100, 100], [
                                 pos[0], pos[1]-7+position, 20, 24])
                pygame.draw.circle(programme.screen, [255, 255, 255], [
                                   pos[0]+20, pos[1]+5+position], 8)
            if situation == False:
                pygame.draw.circle(programme.screen, [100, 100, 100], [
                                   pos[0], pos[1]+5+position], 12)
                pygame.draw.circle(programme.screen, [100, 100, 100], [
                                   pos[0]+20, pos[1]+5+position], 12)
                pygame.draw.rect(programme.screen, [100, 100, 100], [
                                 pos[0], pos[1]-7+position, 20, 24])
                pygame.draw.circle(programme.screen, [255, 255, 255], [
                                   pos[0], pos[1]+position+5], 8)

    def bind_switch(event, pos, position):
        if event.type == pygame.MOUSEBUTTONUP and position + pos[1] >= 30:
            try:
                if pygame.mouse.get_pos()[0] >= pos[0]-5 and pygame.mouse.get_pos()[0] <= pos[0]+30 and pygame.mouse.get_pos()[1] >= pos[1]-5+position and pygame.mouse.get_pos()[1] <= pos[1]+24+position:
                    return True
            except:
                return None
            return False
    def colorChooser(screen):
        '''
        简陋的选色器
        '''
        r=0
        b=0
        g=0
        running = True
        x=0
        y=0
        down = False
        while running:
            for event in  pygame.event.get() :
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEMOTION:
                    x,y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    down = True
                if event.type == pygame.MOUSEBUTTONUP:
                    down = False
                    if x > 10 and x < 490 and y > 410 and y < 490:
                        return [r,g,b]
                if down:
                    x,y = pygame.mouse.get_pos()
                    if x >= 20 and x <= 220:
                        print("True")
                        if y >= 25 and y <= 55:
                            r = x-20
                        if y >= 55 and y <= 65 :
                            g = x-20
                        if y >= 85 and y <= 95:
                            print(y)
                            b = x-20
            screen.fill([r,g,b])
            pygame.draw.rect(screen,[155,155,155],[20,8,200,104])
            pygame.draw.circle(screen,[155,155,155],[20,20],12)
            pygame.draw.circle(screen,[155,155,155],[220,20],12)
            pygame.draw.circle(screen,[155,155,155],[220,100],12)
            pygame.draw.circle(screen,[155,155,155],[20,100],12)
            pygame.draw.rect(screen,[155,155,155],[8,20,12,80])
            pygame.draw.rect(screen,[155,155,155],[220,20,12,80])
            pygame.draw.rect(screen,[255,235,235],[20,25,200,16])
            pygame.draw.rect(screen,[235,255,235],[20,55,200,16])
            pygame.draw.rect(screen,[235,235,255],[20,85,200,16])
            pygame.draw.circle(screen,[255,235,235],[20,33],8)
            pygame.draw.circle(screen,[235,255,235],[20,63],8)
            pygame.draw.circle(screen,[235,235,255],[20,93],8)
            pygame.draw.circle(screen,[255,235,235],[220,33],8)
            pygame.draw.circle(screen,[235,255,235],[220,63],8)
            pygame.draw.circle(screen,[235,235,255],[220,93],8)
            pygame.draw.circle(screen,[r,g,b],[20+r,33],8)
            pygame.draw.circle(screen,[r,g,b],[20+g,63],8)
            pygame.draw.circle(screen,[r,g,b],[20+b,93],8)
            pygame.draw.rect(screen,[155,155,155],[10,420,480,70])
            pygame.display.update()
    def switch(situation, pos, text, position):
        entrance.draw_switch(
            situation, [pos[0]+360, pos[1]+10], position=position)
        entrance.print_screen(text, pos, color='white')

    def draw_addbox(value, pos, text, position):
        entrance.print_screen(text, pos, color='white')
        if value <= 0:
            pygame.draw.rect(programme.screen, [150, 100, 100], [
                             pos[0]+330, pos[1]+position, 20, 20])
        else:
            pygame.draw.rect(programme.screen, [200, 100, 100], [
                             pos[0]+330, pos[1]+position, 20, 20])
        pygame.draw.rect(programme.screen, [200, 100, 100], [
                         pos[0]+352, pos[1]+position, 40, 20])
        pygame.draw.rect(programme.screen, [200, 100, 100], [
                         pos[0]+394, pos[1]+position, 20, 20])
        entrance.print_screen(
            "-", [pos[0]+335, pos[1]-5+position], color='white')
        entrance.print_screen(
            "+", [pos[0]+398, pos[1]-6+position], color='white')
        entrance.print_screen(
            str(value), [pos[0]+356, pos[1]-4+position], color='white')

    def bind_addbox(pos):
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

    def setting():
        tools.ui.switchAnimation()
        position = 0
        running = True
        while running:
            time.sleep(0.04)
            programme.screen.fill([0, 0, 0])
            entrance.draw_star()
            pygame.draw.rect(programme.screen, [255, 0, 0], [0, 0, 500, 50])
            entrance.print_screen("Setting", pos=(230, 10), color='white')
            entrance.print_screen("<", pos=(10, 10), color='white')
            entrance.switch(programme.god, pos=(40, 100),
                            text="作弊模式", position=position)
            entrance.draw_addbox(programme.player1_bullet,
                                 (40, 150), "玩家一子弹数量", position)
            entrance.draw_addbox(programme.player2_bullet,
                                 (40, 200), "玩家二子弹数量", position)
            entrance.draw_addbox(programme.movAmount,
                                 (40, 250,), "敌人移动速度", position=position)
            entrance.print_screen("玩家机身颜色",(40,300),color='white')
            entrance.print_screen("玩家机翼颜色",(40,350),color='white')
            for event in pygame.event.get():
                # 退出检测
                try:
                        x, y = pygame.mouse.get_pos()
                except:
                        continue
                if event.type == pygame.QUIT:
                    programme.running = False
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    # 获取鼠标位置
                    try:
                        x, y = pygame.mouse.get_pos()
                    except:
                        continue
                if event.type == pygame.MOUSEBUTTONUP:
                    get = entrance.bind_switch(
                        event, pos=(400, 100), position=position)
                    programme.player2_bullet += entrance.bind_addbox((40, 200))
                    programme.player1_bullet += entrance.bind_addbox((40, 150))
                    programme.movAmount += entrance.bind_addbox((40, 250))
                    if get != None:
                        programme.god = get if programme.god != True else False
                    if x > 10 and x <= 200 and y > 300 and y <= 340:
                        programme.planeColor_player = entrance.colorChooser(programme.screen)
                    if x > 10 and x <= 200 and y > 350 and y <= 390:
                        programme.wigColor_player = entrance.colorChooser(programme.screen)
                    if x > 10 and x < 50 and y > 10 and y < 40:
                        tools.ui.switchAnimation()
                        running = False

            pygame.display.update()
    
    def entrance():
        while programme.running:
            time.sleep(0.04)
            pygame.draw.rect(programme.screen, [200, 0, 0], [00, 40, 500, 70])
            programme.font = pygame.font.Font(
                "default.ttf", 40)
            programme.screen.blit(programme.font.render(
                f"Plane War", True, 'WHITE'), (150, 50))
            # 重新设置字体
            programme.font = pygame.font.Font(
                "default.ttf", 20)
            programme.screen.blit(programme.font.render(
                f"{programme.version}", True, 'white'), (0, 470))
            entrance.draw_button(pos=410, type='inactive')
            entrance.print_screen("设置",(220,420))
            entrance.draw_button(pos=410, type='inactive')
            entrance.print_screen("设置",(220,420))
            entrance.draw_button(type='inactive')
            entrance.draw_button(pos=320,type = 'inactive')   
            entrance.print_screen("单人模式")
            entrance.print_screen("双人模式", (210, 330))
            pygame.draw.rect(programme.screen, [200, 0, 0], [00, 40, 500, 70])
            programme.font = pygame.font.Font(
                "default.ttf", 40)
            programme.screen.blit(programme.font.render(
                f"Plane War", True, 'WHITE'), (150, 50))
            # 重新设置字体
            programme.font = pygame.font.Font(
                "default.ttf", 20)
            programme.screen.blit(programme.font.render(
                f"{programme.version}", True, 'white'), (0, 470))
            entrance.draw_star()
            # programme 函数主循环
            # 获取事件
            for event in pygame.event.get():
                # 退出检测
                if event.type == pygame.QUIT:
                    programme.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x >= 100 and x <= 400:
                        if y >= 240 and y <= 310:
                            programme.screen.fill([100, 100, 100])
                            programme.running = False
                            programme.main(False)
                        if y > 320 and y <= 390:
                            programme.running = False
                            programme.screen.fill([100, 100, 100])
                            programme.player2 = True
                            programme.main(True)
                        if y > 410 and y < 490:
                            entrance.setting()
                if event.type == pygame.MOUSEBUTTONUP and x >= 460 and y > 450 and x <= 490 and y <= 480:
                    entrance.setting()
                if event.type == pygame.MOUSEMOTION:
                    # 获取鼠标位置
                    try:
                        x, y = pygame.mouse.get_pos()
                    except:
                        continue
                    # 按钮与用户交互
                    if x >= 100 and x <= 400:
                        if y >= 240 and y <= 310:
                            # 单人模式
                            entrance.draw_button(pos=250)
                            # 显示文字
                            entrance.print_screen(
                                "单人模式", )
                        elif y > 320 and y <= 390:

                            entrance.draw_button(pos=320)
                            # 显示文字
                            entrance.print_screen(
                                "双人模式", (210, 330))
                        elif y > 410 and y < 490:
                            entrance.draw_button(pos=410, type='active')
                            entrance.print_screen("设置",(220,420))
                        else:
                            entrance.draw_button(pos=250, type='inactive')
                            # 双人模式
                            entrance.draw_button(pos=320, type='inactive')
                            # 显示文字
                            entrance.print_screen("单人模式")
                            entrance.print_screen(
                                "双人模式", (210, 330))
                else:
                    entrance.draw_button(pos=410, type='inactive')
                    entrance.print_screen("设置",(220,420))
                    entrance.draw_button(type='inactive')
                    entrance.draw_button(pos=320,type = 'inactive')   
                    entrance.print_screen("单人模式")
                    entrance.print_screen("双人模式", (210, 330))
            pygame.display.update()


if __name__ == '__main__':
    from init import init
    init.__init__()
    entrance.init_entrance()
    entrance.entrance()
    quit()
