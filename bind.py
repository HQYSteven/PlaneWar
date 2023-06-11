from Append import Append,egg
import random
import pygame
from ui import ui
class bind(object):

        def watch(self, times):
            if self.god == True:
                self.crash = 0
                self.hit = 5
                self.attack = 0
                self.bullet = 0
                self.stone = 0
                self.cure = 100
                self.stringMov = 1
                self.minus = 0
            else:
                self.minus = 10
                self.crash = 10
                self.hit = 5
                self.attack = 20
                self.bullet = 20
                self.stone = 1
                self.cure = 50
                self.stringMov = 10
            if len(self.enemy_x_list) >= 2 and times % 2 == 0:
                index = random.randint(0, len(self.enemy_x_list))
                self.otherAttack_x.append(
                    self.enemy_x_list[index-1]+13)
                self.otherAttack_y.append(
                    self.enemy_y_list[index-1]+50)
            if self.mov == True:
                if self.movDirect == 0:
                    self.player1_x -= 5
                if self.movDirect == 1:
                    self.player1_x += 5
                self.mov = False
                ui.aircraft_1(self)
            if self.mov == True and self.player2:
                if self.movDirect == 0:
                    self.player2_x -= 5
                if self.movDirect == 1:
                    self.player2_x += 5
                self.mov = False
                ui.aircraft_1(self)
            if times == 20:
                self.stoneXList.append(
                    random.randint(0, self.screenWidth))
                self.stoneYList.append(0)
            if self.player1_life < 0:
                self.player1_life = 0
                print("YOU LOSE")
                quit()
            if self.player2_life < 0:
                self.player2_life = 0
                print("YOU LOSE")
                quit()

            if self.score < 0:
                self.score = 0
            if not self.player2:
                if self.player1_life < 50 and self.medicineAmount > 0 and times == 20:
                    Append.appendMedicine(self)
            else:
                if (self.player1_life < 50 or self.player2_life < 50) and times == 20:
                    Append.appendMedicine(self)
            # 每3.2秒出现一架飞机
            if times == 22 and self.planeAmount:
                # 重新计数
                times = 0
                # 在敌方位置列表中添加坐标
                Append.appendEnemy(self)
            if self.player2:
                if self.player1_life <= 0 and self.player2_life <= 0 or self.planeAmount == 0:
                    self.message.append("switch")
                    print("=======/The Game Has Finished\\========")
                    print(f"Player One Has Got:{self.player1_life} left.")
                    print(f"You Have Got : {self.score}")
                    if self.planeAmount:
                        print("YOU LOSE")
                    else:
                        egg.mainProgramme(self)
                        self.screen.quit()
                        quit()
            else:
                if self.player1_life <= 0 or self.planeAmount == 0:
                    self.message.append("switch")
                    print("=======/The Game Has Finished\\========")
                    print(f"Player One Has Got:{self.player1_life} left.")
                    print(f"Player Two Has Got:{self.player2_life} left.")
                    print(f"You Have Got : {self.score}")
                    if self.planeAmount:
                        print("YOU LOSE")
                    else:
                        egg.mainProgramme(self)
                        self.message.append("egg")
            return times

        def keyEvent(self, event):
            # 左键处理
            if self.player1_life > 0:
                if event.key == pygame.K_LEFT:
                    self.mov = True
                    self.movDirect = 0
                if event.key == pygame.K_RIGHT:
                    self.mov = True
                    self.movDirect = 1
                if event.key == pygame.K_F1:
                    self.attack = self.bullet
                    self.mode = 'normal'
                    self.AttackColor = self.color1
                if event.key == pygame.K_F2:
                    self.attack = self.artillery
                    self.mode = 'artillery'
                    self.AttackColor = self.color2
                if event.key == pygame.K_F3:
                    self.attack = self.Xrate
                    self.mode = 'Xrate'
                    self.AttackColor = self.color3
                if event.key == pygame.K_F4:
                    self.attack = self.missile
                    self.mode = 'missile'
                    self.AttackColor = self.color4
                if event.key == pygame.K_UP:
                    # 识别是否有剩子弹
                    if self.player1_bullet:
                        # 添加子弹坐标
                        Append.appendAttack(self,)
                        self.player1_bullet -= 1
            if self.player2 and self.player2_life > 0:
                if event.key == pygame.K_a:
                    self.player2_x -= 1
                if event.key == pygame.K_d:
                    self.player2_x += 1
                if event.key == pygame.K_w:
                    if self.player2_bullet:
                        if self.player2_x != self.player1_x:
                            Append.appendAttack(self, 0)
                            self.player2_bullet -= 1
    # 刷新子弹
            if event.type == pygame.MOUSEMOTION and not self.player2:
                self.player1_x = pygame.mouse.get_pos()[0]
                if self.player1_x > 480:
                    self.player1_x = 480