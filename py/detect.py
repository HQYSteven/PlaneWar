from Append import Append
import random
import pygame
from egg import egg
import time

class Detect(object):
    '''
    This class is used to detect all the events.
    For example: k_left pressed.
    '''

    def detect_Moving(self):
        '''
        This fuction is used to detect all the moving options
        '''
        # if the left key pressed,move the players' plane
        if self.mov == True:
            if self.movDirect == 0:
                self.playerxList[self.control] -= 5
            if self.movDirect == 1:
                self.playerxList[self.control] += 5
            self.mov = False
        if self.mov == True and self.player2:
            if self.movDirect == 0:
                self.playerxList[1] -= 5
            if self.movDirect == 1:
                self.playerxList[1] += 5
            self.mov = False

    def sendAttack(self, loopTimes: int,) -> None:
        '''
        @ loopTimes: loop times\n
        this fuc is used to detect and send enemies
        '''
        # decide if it is the right time to send emenies.
        if len(self.enemy_x_list) >= 2 and loopTimes % 2 == 0:
            # calculate a random pos between the width and 0
            coordinate = random.randint(0, len(self.enemy_x_list))
            self.otherAttack_x.append(
                self.enemy_x_list[coordinate-1]+13)
            self.otherAttack_y.append(
                self.enemy_y_list[coordinate-1]+50)

    def sendStones(self, loopTimes: int) -> None:
        '''
        @ loopTimes: The time the programme has looped\n
        This fuction is used to send stones at the right time
         * detect if it is time to send stones
         * The coordinate of the stone is a random num between screewidth and 0
        '''
        if loopTimes == 20:
            self.stoneXList.append(
                random.randint(0, self.screenWidth))
            self.stoneYList.append(0)

    def sendMedicines(self,loopTimes:int) -> None:
        '''
        detect if it is neccesary to send medicines for the players
        '''
        
        if not self.player2:
            if self.player1_life < 50 and self.medicineAmount > 0 and loopTimes == 20:
                Append.appendMedicine(self)
        else:
            if (self.player1_life < 50 or self.player2_life < 50) and loopTimes == 20:
                Append.appendMedicine(self)
    def detectQuit(self)->None:
        '''
        This fuction is used to detect quit event.
        '''
        # if the life of the players have ran out
        # quit
        if self.planeAmount == 0 and self.enemy_x_list == []:
            pass
        if self.player1_life < 0:
            if self.planeAmount:
                self.runningP = False
                return self.score,"lose"
        if self.planeAmount == 0 and self.enemy_x_list ==[]:
                self.message.append("egg")
                time.sleep(1)
                return egg.mainProgramme(self),egg
        if self.player2_life < 0:
            self.runningP = False
            return self.score,'lose'
    def shortcut(self,event)->None:
        '''
        @ event:The event you got
        This fuction is used to detect the shortcut option
        '''
        if event.key == pygame.K_F12:
            self.message.append("shortcut")
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            run = False
                            self.message.append("esc")
            return None
    def watch(self, times) -> int:
        '''
        @ times: The loop times\n
        This fuction is used to watch the key events\n
        created in 2022
        '''
        Detect.sendAttack(self, times)
        Detect.detect_Moving(self)
        Detect.sendStones(self,times)
        r = Detect.detectQuit(self)
        Detect.sendMedicines(self,times)
        
        if r != None:
            return r
        # make score over zero
        if self.score < 0:
            self.score = 0
        if times == 22 and self.planeAmount:
            # 重新计数
            times = 0
            # 在敌方位置列表中添加坐标
            Append.appendEnemy(self)
        return times

    def keyEvent(self, event) -> None:
        '''
        @ event: The event you received\n
        The is a fuction used to detect the key events.
        '''
        # 左键处理
        # switch the arm mode
        if event.key == pygame.K_0:
            self.control = 0
        if event.key == pygame.K_1:
            self.control = 1
        if event.key == pygame.K_2:
            self.control = 2
        if event.key == pygame.K_f and not self.wigman:
            self.wigman = False if self.wigman else True
            self.playerxList.append(50)
            self.playeryList.append(445)
            self.playerxList.append(150)
            self.playeryList.append(400)
        if event.key == pygame.K_F1:
            self.attack = self.bullet
            self.mode = 'normal'
            self.AttackColor = self.color1
        elif event.key == pygame.K_F2:
            self.attack = self.artillery
            self.mode = 'artillery'
            self.AttackColor = self.color2
        elif event.key == pygame.K_F3:
            self.attack = self.Xrate
            self.mode = 'Xrate'
            self.AttackColor = self.color3
        elif event.key == pygame.K_F4:
            self.attack = self.missile
            self.mode = 'missile'
            self.AttackColor = self.color4
        if self.player1_life > 0:
            # move player1
            if event.key == pygame.K_LEFT:
                self.mov = True
                self.movDirect = 0
            if event.key == pygame.K_RIGHT:
                self.mov = True
                self.movDirect = 1
            
            if event.key == pygame.K_UP:
                # 识别是否有剩子弹
                if self.player1_bullet:
                    # 添加子弹坐标
                    Append.appendAttack(self,self.control)
                    self.player1_bullet -= 1
        if self.player2 and self.player2_life > 0:
            # move and send attacks of player2
            if event.key == pygame.K_a:
                self.playerxList[1] -= 1
            if event.key == pygame.K_d:
                self.playerxList[1] += 1
            if event.key == pygame.K_w:
                if self.player2_bullet:
                    if self.playerxList[2] != self.playerxList[1]:
                        Append.appendAttack(self, 0)
                        self.player2_bullet -= 1
        
        Detect.shortcut(self,event)
        
