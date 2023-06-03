import pygame
import time
import random
import _thread
from blur import blur
'''
 * You may think you know what the following code does.
 * But you don't. Trust me.
 * Fiddle with it, and you'll spend many a sleepless
 * night cursing the moment you thought you'd be clever
 * enough to "optimize" the code below.
 * Now close this file and go play with something else.
 *
 * 你可能会认为你读得懂以下的代码。但是你不会懂的，相信我吧。
 * 要是你尝试玩弄这段代码的话，你将会在无尽的通宵中不断地咒骂自己为什么会认为自己聪明到可以优化这段代码。
 * 现在请关闭这个文件去玩点别的吧。
 *
'''

''''
别动,ui,检测,update模块都在这里
'''


class tools(object):
    class file(object):
        def readFile(name: str, startRow: int = 0, endRow: int = 1) -> str:
            result = ''

            with open(name, mode='r') as file:
                fileList = []
                fileList = file.readlines()
                if endRow > len(fileList):
                    endRow = len(fileList)
                for index in range(0, endRow):
                    if index >= startRow:
                        result += fileList[index]
                        continue

            return result

    class ui(object):
        def movAnimation(self,player=0, side=0):
            if player == 0:
                if side == 0:
                    i = 0
                    for i in range(5):
                        self.screen.fill([0, 0, 0])
                        self.player1_x += i
                        tools.ui.aircraft_1()
                        pygame.display.update()
                if side == 1:
                    i = 0
                    for i in range(5):
                        self.screen.fill([0, 0, 0])
                        self.player1_x -= i
                        tools.ui.aircraft_1()
                        pygame.display.update()

            if player == 1:
                if side == 0:
                    for i in range(5):
                        self.screen.fill([0, 0, 0])
                        time.sleep(0.01)
                        self.player2_x += i
                        tools.ui.player2Aircraft()
                        pygame.display.update()
                if side == 1:
                    for i in range(5):
                        self.screen.fill([0, 0, 0])
                        time.sleep(0.01)
                        self.player2_x -= i
                        tools.ui.player2Aircraft()
                        pygame.display.update()

        def aircraft_1(self,):
            # 机身 30,144,255
            # 机翼 131,206,250
            pygame.draw.circle(self.screen, self.planeColor_player, [
                self.player1_x+15, self.player1_y], 5)
            pygame.draw.rect(self.screen, self.planeColor_player, [
                self.player1_x+10, self.player1_y, 10, 31])
            pygame.draw.rect(self.screen, self.wigColor_player, [
                self.player1_x-2, self.player1_y+15, 12, 10])
            pygame.draw.rect(self.screen, self.wigColor_player, [
                self.player1_x+20, self.player1_y+15, 12, 10])
            pygame.draw.rect(self.screen, self.wigColor_player, [
                self.player1_x+5, self.player1_y+31, 20, 3])

        def enemyAircraft(self,index):
            # 机身 192,192,192
            # 机翼 178,34,34

            pygame.draw.rect(self.screen, self.planeColor_enemy, [
                self.enemy_x_list[index]+3, self.enemy_y_list[index], 22, 3])
            pygame.draw.rect(self.screen, self.planeColor_enemy, [
                self.enemy_x_list[index]+10, self.enemy_y_list[index], 10, 35])
            pygame.draw.rect(self.screen, self.wigColor_enemy, [
                self.enemy_x_list[index]-2, self.enemy_y_list[index]+10, 12, 10])
            pygame.draw.rect(self.screen, self.wigColor_enemy, [
                self.enemy_x_list[index]+20, self.enemy_y_list[index]+10, 12, 10])
            pygame.draw.circle(self.screen, self.planeColor_enemy, [
                self.enemy_x_list[index]+15, self.enemy_y_list[index]+35], 5)
            pygame.draw.rect(self.screen, [0, 0, 0], [
                self.enemy_x_list[index]+3, self.enemy_y_list[index]+2, 22, 3])
            pygame.draw.rect(self.screen, [255, 0, 0], [
                self.enemy_x_list[index]+2, self.enemy_y_list[index]-self.movAmount-3, int(self.enemyLifeList[index]/4), 3])

        def player2Aircraft(self,):
            pygame.draw.circle(self.screen, self.planeColor_player, [
                self.player2_x+15, self.player2_y], 5)
            pygame.draw.rect(self.screen, self.planeColor_player, [
                self.player2_x+10, self.player2_y, 10, 31])
            pygame.draw.rect(self.screen, self.wigColor_player, [
                self.player2_x-2, self.player2_y+15, 12, 10])
            pygame.draw.rect(self.screen, self.wigColor_player, [
                self.player2_x+20, self.player2_y+15, 12, 10])
            pygame.draw.rect(self.screen, self.wigColor_player, [
                self.player2_x+5, self.player2_y+31, 20, 3])
            pygame.draw.rect(self.screen, [255, 0, 0], [
                self.player2_x, self.player2_y+39, int(self.player2_life/3), 2])

        def medicine(self,index):
            pygame.draw.rect(self.screen, [255, 255, 255], [
                self.medicineX[index], self.medicineY[index], 20, 20])
            pygame.draw.rect(self.screen, [255, 0, 0], [
                self.medicineX[index]+2, self.medicineY[index]+8, 16, 4])
            pygame.draw.rect(self.screen, [255, 0, 0], [
                self.medicineX[index]+8, self.medicineY[index]+3, 4, 16])

        def switchAnimation(self,):
            fillPos = 0
            while fillPos <= 500:
                time.sleep(0.005)
                pygame.draw.rect(self.screen, [0, 0, 0], [
                    0, fillPos, 500, 100])
                fillPos += 10
                pygame.display.update()

        def drawString(self,index):
            if self.mode == 'normal':
                width = 3
            elif self.mode == 'artillery':
                width = 4
            elif self.mode == 'Xrate':
                width = 5
            elif self.mode == 'missile':
                width = 6
            try:
                pygame.draw.rect(self.screen, self.AttackColor, [
                    self.attackStringX[index], self.attackStringY[index]+10, width, 10])
            except:
                pass

        def bloodDock(self,player):
            text = self.font.render(
                f"{self.player1_life}", True, 'white')
            self.screen.blit(text, (self.screenWidth - 270, 20))
            text = self.font.render(
                f"{self.score}", True, "white")
            self.screen.blit(text, (30, 20))
            pygame.draw.rect(self.screen, [255, 0, 0], [
                self.screenWidth-220, 20, self.player1_life, 20])
            pygame.draw.rect(self.screen, [200, 200, 200], [
                self.screenWidth-40, 20, 10, 20])
            text = self.font.render(
                f"{self.player1_bullet}", True, "white")
            self.screen.blit(text, (self.screenWidth-90, 20))
            text = self.font.render(
                f"{self.mode}", True, "white")
            self.screen.blit(text, (70, 20))

    class bind(object):

        def watch(self,times):
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
                tools.ui.aircraft_1(self)
            if self.mov == True and self.player2:
                if self.movDirect == 0:
                    self.player2_x -= 5
                if self.movDirect == 1:
                    self.player2_x += 5
                self.mov = False
                tools.ui.aircraft_1(self)
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
                    tools.appendMedicine(self)
            else:
                if (self.player1_life < 50 or self.player2_life < 50) and times == 20:
                    tools.appendMedicine(self)
            # 每3.2秒出现一架飞机
            if times == 22 and self.planeAmount:
                # 重新计数
                times = 0
                # 在敌方位置列表中添加坐标
                tools.appendEnemy(self)
            if self.player2:
                if self.player1_life <= 0 and self.player2_life <= 0 or self.planeAmount == 0:
                    self.message.append("switch")
                    print("=======/The Game Has Finished\\========")
                    print(f"Player One Has Got:{self.player1_life} left.")
                    print(f"You Have Got : {self.score}")
                    if self.planeAmount:
                        print("YOU LOSE")
                    else:
                        tools.egg.mainProgramme(self)
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
                        tools.egg.mainProgramme(self)
                        self.message.append("egg")
            return times

        def keyEvent(self,event):
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
                        tools.appendAttack(self,)
                        self.player1_bullet -= 1
            if self.player2 and self.player2_life > 0:
                if event.key == pygame.K_a:
                    self.player2_x -= 1
                if event.key == pygame.K_d:
                    self.player2_x += 1
                if event.key == pygame.K_w:
                    if self.player2_bullet:
                        if self.player2_x != self.player1_x:
                            tools.appendAttack(self,0)
                            self.player2_bullet -= 1
    # 刷新子弹
            if event.type == pygame.MOUSEMOTION and not self.player2:
                self.player1_x = pygame.mouse.get_pos()[0]
                if self.player1_x > 480:
                    self.player1_x = 480

    def appendMedicine(self,):
        self.medicineX.append(random.randint(0, 480))
        self.medicineY.append(0)
        self.medicineAmount -= 1

    def appendEnemy(self,):
        num = random.randint(0, self.screenWidth-30)
        self.enemy_x_list.append(num)
        self.enemy_y_list.append(0)
        self.otherAttack_x.append(num+13)
        self.otherAttack_y.append(10)
        self.enemyLifeList.append(100)
        self.planeAmount -= 1

    def appendAttack(self,player=1):
        if player:
            self.attackStringX.append(self.player1_x+13)
            self.attackStringY.append(self.screenHeight - 100)
        else:
            self.attackStringX.append(self.player2_x+13)
            self.attackStringY.append(self.screenHeight - 80)

    class update(object):
        def updateStars(self,):
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

        def updateString_mov(self,):
            index = 0
            while index >= 0 and index < len(self.attackStringX):
                if index < 0 or index >= len(self.attackStringX):
                    break
                self.attackStringY[index] -= self.stringMov
                if self.attackStringY[index] < -20:
                    del self.attackStringY[index]
                    del self.attackStringX[index]
                    index -= 1
                index += 1

        def updateString_bindEnemy(self,):
            index = 0
            while index >= 0 and index < len(self.enemy_x_list):
                if index < 0 or index >= len(self.enemy_x_list):
                    break
                self.enemy_y_list[index] += self.movAmount
                if self.enemy_y_list[index] >= self.screenHeight:
                    del self.enemy_y_list[index]
                    del self.enemy_x_list[index]
                    index -= 1
                    if self.score > 0:
                        self.score -= 10
                    else:
                        self.score = 0
                if index < 0 or index >= len(self.enemy_x_list):
                    break
                index += 1

        def updateString_bindEnemyAttack_mov(self,):
            index = 0
            while index < len(self.otherAttack_x):
                if index < 0 or index >= len(self.otherAttack_x):
                    break
                self.otherAttack_y[index] += self.stringMov+2
                if self.otherAttack_y[index] > self.screenHeight:
                    del self.otherAttack_y[index]
                    del self.otherAttack_x[index]
                    index -= 1
                index += 1

        def updateString_bindEnemy_shot(self,):
            index = 0
            while index < len(self.attackStringX):
                index_enemy = 0
                if index > len(self.attackStringX) or index < 0:
                    break
                while index_enemy < len(self.enemy_x_list):
                    if index_enemy > len(self.enemy_x_list) or index_enemy < 0:
                        break
                    if index > len(self.attackStringX) or index < 0:
                        break
                    if (
                        (
                            (
                                self.attackStringX[index] >= self.enemy_x_list[index_enemy]-3
                            )
                            and
                            (
                                self.attackStringX[index] <= self.enemy_x_list[index_enemy]+31
                            )
                        )
                        and
                        (
                            (
                                self.attackStringY[index] >= self.enemy_y_list[index_enemy]-5
                            )
                            and
                            (
                                self.attackStringY[index] <= self.enemy_y_list[index_enemy] + 15
                            )
                        )
                    ):
                        self.attackStringY[index] += self.stringMov
                        self.enemyLifeList[index_enemy] -= 20

                        del self.attackStringX[index]
                        del self.attackStringY[index]
                        index -= 1

                        self.enemyLifeList[index_enemy] -= self.attack
                        if self.enemyLifeList[index_enemy] <= 0:
                            self.enemy_y_list[index_enemy] += self.movAmount
                            del self.enemy_x_list[index_enemy]
                            del self.enemy_y_list[index_enemy]
                            del self.enemyLifeList[index_enemy]
                            index_enemy -= 1
                            self.score += 10
                    index_enemy += 1
                index += 1

        def updateString_bindEnemyAttack(self,):
            index = 0
            while index >= 0 and index < len(self.otherAttack_x):
                if index < 0 or index >= len(self.otherAttack_x):
                    break
                if self.player2:
                    if ((self.otherAttack_x[index] >= self.player2_x-3 and self.otherAttack_x[index] <= self.player2_x + 31)
                            and (self.otherAttack_y[index] >= self.player2_y and self.otherAttack_y[index] < - self.player2_y+20) and self.player2):
                        del self.otherAttack_x[index]
                        del self.otherAttack_y[index]
                        self.score -= 10
                        self.player2_life -= self.hit
                        index -= 1
                if index < 0 or index >= len(self.otherAttack_x):
                    break
                if ((self.otherAttack_x[index] >= self.player1_x-3 and self.otherAttack_x[index] <= self.player1_x + 31)
                        and (self.otherAttack_y[index] >= self.player1_y and self.otherAttack_y[index] <= self.player1_y+20)):
                    del self.otherAttack_x[index]
                    del self.otherAttack_y[index]
                    self.score -= 10
                    self.player1_life -= self.hit
                    index -= 1
                index += 1
                if index < 0 or index >= len(self.otherAttack_x):
                    break

        def bind_crash(self,):

            index = 0
            while index >= 0 and index < len(self.enemy_x_list):
                if index < 0 and index >= len(self.enemy_x_list):
                    break
                if ((self.enemy_x_list[index] >= self.player1_x-30 and
                    self.enemy_x_list[index] <= self.player1_x+30)
                    and
                    (
                    self.enemy_y_list[index] >= self.player1_y-30
                    and self.enemy_y_list[index] <= self.player1_y+60
                )):

                    self.enemy_y_list[index] += 15
                    del self.enemy_x_list[index]
                    del self.enemy_y_list[index]
                    self.score -= 10
                    del self.enemyLifeList[index]
                    self.player1_life -= self.crash
                    index -= 1
                try:
                    self.enemy_x_list[index]
                except:
                    break
                if ((self.enemy_x_list[index] >= self.player2_x-30 and
                    self.enemy_x_list[index] <= self.player2_x+60)
                    and self.player2 and
                    (
                    self.enemy_y_list[index] >= self.player2_y
                    and self.enemy_y_list[index] <= self.player2_y+60 and self.player2
                )):
                    del self.enemy_x_list[index]
                    del self.enemy_y_list[index]
                    del self.enemyLifeList[index]
                    self.score -= 20
                    self.player2_life -= self.crash
                    index -= 1
                    self.enemy_y_list[index] += 10
                index += 1

        def bind_medicine(self,):
            index = 0
            while index >= 0 and index < len(self.medicineX):
                if index < 0 and index >= len(self.medicineX):
                    break
                self.medicineY[index] += 10
                if (
                    (self.medicineX[index] > self.player1_x -
                     19 and self.player1_x + 20 > self.medicineX[index])
                    and
                    (self.medicineY[index] > self.player1_y -
                     35 and self.player1_y + 35 > self.medicineY[index])

                ):
                    del self.medicineY[index]
                    del self.medicineX[index]
                    self.player1_life += self.cure
                    index -= 1
                if index < 0 and index >= len(self.medicineX):
                    break
                try:
                    self.medicineX[index]
                except:
                    break
                if (
                    (self.medicineX[index] > self.player2_x -
                     19 and self.player2_x + 20 > self.medicineX[index])
                    and
                    (self.medicineY[index] > self.player2_y -
                     35 and self.player2_y + 35 > self.medicineY[index])
                    and self.player2
                ):
                    del self.medicineY[index]
                    del self.medicineX[index]
                    self.player2_life += self.cure
                    index -= 1
                index += 1

        def bind_stone(self,):
            index_stone = 0
            while index_stone < len(self.stoneXList) and index_stone >= 0:
                if index_stone >= len(self.stoneXList) or index_stone < 0:
                    break
                self.stoneYList[index_stone] += 15
                if self.stoneYList[index_stone] >= self.screenHeight:
                    del self.stoneYList[index_stone]
                    del self.stoneXList[index_stone]
                    index_stone -= 1
                if index_stone >= len(self.stoneXList) or index_stone < 0:
                    break
                if not self.player2:
                    if ((self.player1_x-30 > self.stoneXList[index_stone] and self.stoneXList[index_stone] < self.player1_x + 30)
                            and (self.player1_y - 20 < self.stoneYList[index_stone]) and self.stoneYList[index_stone] < self.player1_y+50):
                        del self.stoneYList[index_stone]
                        del self.stoneXList[index_stone]
                        tools.ui.aircraft_1(self,)
                        self.player1_life -= self.stone
                        index_stone -= 1
                else:
                    if ((self.player2_x-20 > self.stoneXList[index_stone] and self.stoneXList[index_stone] < self.player2_x + 40)
                            and (self.player2_y - 20 < self.stoneYList[index_stone]) and self.stoneYList[index_stone] < self.player2_y + 20):
                        del self.stoneYList[index_stone]
                        del self.stoneXList[index_stone]
                        tools.ui.player2Aircraft(self,)
                        self.player2_life -= self.stone
                        index_stone -= 1
                stringIndex = 0
                while stringIndex >= 0 and stringIndex < len(self.attackStringX):
                    if stringIndex < 0 or stringIndex >= len(self.attackStringX):
                        break
                    if index_stone >= len(self.stoneXList) or index_stone < 0:
                        break
                    if self.stoneXList[index_stone] - 3 < self.attackStringX[stringIndex] and self.stoneXList[index_stone]+50 > self.attackStringX[stringIndex] and self.stoneYList[index_stone] < self.attackStringY[stringIndex] and self.stoneYList[index_stone]+20 > self.attackStringY[stringIndex]:
                        del self.stoneXList[index_stone]
                        del self.stoneYList[index_stone]
                        self.attackStringY[stringIndex] += 10
                        del self.attackStringX[stringIndex]
                        del self.attackStringY[stringIndex]
                        index_stone -= 1
                        stringIndex -= 1
                        self.score += 10
                    stringIndex += 1
                index_stone += 1

        def update(self):
            tools.update.updateString_bindEnemy(self)
            tools.update.updateString_bindEnemy_shot(self)
            tools.update.updateString_bindEnemyAttack(self)
            tools.update.bind_crash(self)
            tools.update.updateString_bindEnemyAttack_mov(self)
            tools.update.updateString_mov(self)
            tools.update.bind_medicine(self)
            tools.update.bind_stone(self)
#################################################################

    class egg(object):
        def grvaity(self,color):

            if self.distance > 0:
                self.distance -= self.speed
            text = self.font.render(
                f"{round(self.gravity,2)}N/kg,{round(self.speed,2)}m/s", True, "white")
            self.screen.blit(text, (10, 10))
            text = self.font.render(
                f"{round(self.distance,2)}m", True, "white")
            self.screen.blit(text, (10, 40))

        def fuel(self,color):
            text = self.font.render(
                f"FUEL:{round(self.fuelAmount*100,2)}%", True, "white")
            self.screen.blit(text, (270, 10))

        def launch(self,):
            self.player1_y = 380-int(self.distance)
            pygame.draw.rect(self.screen, self.launcher,
                             [0, 480, 500, 20])

        def watch_egg(self,times):
            if times % 10 == 0:
                self.gravity += self.add
                if self.distance > 0:
                    self.speed += self.gravity
                times = 0
            if self.lostFuel and self.fuelAmount > 0:
                self.fuelAmount -= self.lost
                self.speed -= self.lost*50
                if self.speed < 0:
                    self.gravity -= self.add
                if self.gravity < 0:
                    self.gravity = 0
            return times

        def aircraft(self):
            # 机身 30,144,255
            # 机翼 131,206,250
            pygame.draw.circle(self.screen, self.planeColor_player, [
                self.player1_x+20, self.player1_y], 10)
            pygame.draw.rect(self.screen, self.planeColor_player, [
                self.player1_x+10, self.player1_y, 20, 80])
            pygame.draw.rect(self.screen, self.wigColor_player, [
                self.player1_x-32, self.player1_y+25, 42, 25])
            pygame.draw.rect(self.screen, self.wigColor_player, [
                self.player1_x+30, self.player1_y+25, 42, 25])
            pygame.draw.rect(self.screen, self.wigColor_player, [
                self.player1_x+2, self.player1_y+80, 35, 5])
            pygame.draw.polygon(self.screen, self.planeColor_player, [(
                self.player1_x-10, self.player1_y+25), (self.player1_x-23, self.player1_y+25),
                (self.player1_x-17, self.player1_y+15)])
            pygame.draw.polygon(self.screen, self.planeColor_player, [(
                self.player1_x+43, self.player1_y+25), (self.player1_x+56, self.player1_y+25),
                (self.player1_x+50, self.player1_y+15)])
            pygame.draw.polygon(self.screen, self.planeColor_player, [(
                self.player1_x+43, self.player1_y+25), (self.player1_x+56, self.player1_y+25),
                (self.player1_x+50, self.player1_y+15)])
            if self.lostFuel:
                pygame.draw.polygon(self.screen, self.fire, [
                    (self.player1_x+45, self.player1_y +
                     66), (self.player1_x+55, self.player1_y+66),
                    (self.player1_x+50, self.player1_y+self.length)])
                pygame.draw.polygon(self.screen, self.fire, [
                    (self.player1_x-15, self.player1_y +
                     66), (self.player1_x-25, self.player1_y+66),
                    (self.player1_x-20, self.player1_y+self.length)])

        def mainProgramme(self,):
            colorTimes = 0
            self.running = True
            loopTimes = 0
            color = 40
            self.player1_y = 50
            self.player1_x = 230
            while self.running:
                loopTimes += 1
                colorTimes += 1
                if colorTimes % 50 == 0 and color <= 220:
                    color += 1
                self.initColor = [10, 10, color]
                pygame.draw.rect(self.screen, [color-(150 if color > 150 else color), color-(
                    100 if color > 100 else color), color], [0, 0, 500, 500])
                time.sleep(0.015)
                tools.egg.aircraft(self,)
                if self.distance <= 320:
                    tools.egg.launch(self,)
                tools.egg.grvaity(self,color)
                tools.egg.fuel(self,color)
                loopTimes = tools.egg.watch_egg(self,loopTimes)
                if self.player1_y <= 200:
                    self.player1_y = 0
                if self.gravity <= 0:
                    self.gravity = 0
                if self.gravity >= 9.80:
                    self.gravity = 9.80
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and self.fuelAmount > 0:
                            self.lostFuel = True
                        if event.key == pygame.K_F1:
                            self.lost *= 1.5
                            self.length += 10
                        if event.key == pygame.K_F2:
                            self.lost /= 1.5
                            self.length -= 10
                    if event.type == pygame.KEYUP:
                        if self.lostFuel:
                            self.lostFuel = False

                    if (self.player1_y == 380 and self.speed <= 3):
                        print("YOU WIN")
                        pygame.quit()
                        quit()
                    elif (self.player1_y == 380 and self.speed > 3):
                        print("YOU LOSE")
                        pygame.quit()
                        quit()
                pygame.display.update()

class programme():
    def __init__(self):
        self.init = True
  
    def graphics(self, a,  player2=False):
        
        tools.ui.switchAnimation(self,)
        index = 0
        while self.running:
            self.player2 = player2
            for message in self.message:
                if message == 'egg':
                    while True:
                        time.sleep(100)
                if message == 'switch':
                    tools.ui.switchAnimation(self,)
                    del self.message[index]
                    continue

                index += 1
            self.screen.fill([0, 0, 0])
            
            
            if self.player2:
                tools.ui.player2Aircraft(self,)
            graphic_update.string(self,)
            graphic_update.ememyString(self,)
            graphic_update.medicine(self,)
            tools.update.updateStars(self,)
            
            graphic_update.stone(self,)
            graphic_update.enemy(self,)
            graphic_update.blurdock(self,)
            if player2:
                tools.ui.bloodDock(self,0)
            tools.ui.bloodDock(self,1)
            tools.ui.aircraft_1(self,)
            pygame.display.update()
    
    def main(self,player2=False):
        """
        plane War
        """

        # 显示玩家血量
        times = 0
        self.running = True
        _thread.start_new_thread(
            self.graphics, (self,self.player2))
        while self.running:
            self.screenWidth = pygame.display.get_window_size()[0]
            self.screenHeight = pygame.display.get_window_size()[1]

            if not self.playing:
                pygame.quit()
                break

            if self.player2:
                self.player2_y = self.screenHeight - 45
            self.player1_y = self.screenHeight - 90
            tools.ui.aircraft_1(self,)
            # 当没有飞机时，退出
            times = tools.bind.watch(self,times)
            # 每次循环停止0.015秒，25FPS/s,用于减轻CPU压力
            time.sleep(1/self.fps)
            times += 1
            # 事件识别
            for event in pygame.event.get():
                # 退出监测
                if event.type == pygame.QUIT:
                    self.running = False
                # 监测是否键盘事件发生
                if event.type == pygame.KEYDOWN:
                    tools.bind.keyEvent(self,event)
            tools.update.update(self)
class graphic_update(programme):
        def string(self,):
            index = 0
            while index >= 0 and index < len(self.attackStringX):
                tools.ui.drawString(self,index)
                index += 1

        def ememyString(self,):
            index = 0
            while index < len(self.otherAttack_x):
                pygame.draw.rect(self.screen, [0, 255, 0], [
                    self.otherAttack_x[index], self.otherAttack_y[index], 3, 10])
                index += 1

        def medicine(self,):
            index = 0
            while index >= 0 and index < len(self.medicineX):
                tools.ui.medicine(self,index)
                index += 1

        def stone(self,):
            index_stone = 0
            while index_stone < len(self.stoneXList) and index_stone >= 0:
                pygame.draw.rect(self.screen, [255, 255, 255], [
                    self.stoneXList[index_stone], self.stoneYList[index_stone], 20, 20])
                index_stone += 1

        def enemy(self,):
            index = 0
            while index >= 0 and index < len(self.enemy_x_list):
                tools.ui.enemyAircraft(self,index)
                index += 1
        def blurdock(self,):
            blurl = []
            x=10
            y = 10
            for y in range(20,55):
                for x in range(20,480):
                    blurl.append(pygame.Surface.get_at(self.screen,(x,y)))
            i = blur(blurl,460)
            after = blur.blur(i)
            
            x = 20
            y = 20
            for l in after:
                pygame.draw.rect(self.screen,l,[x,y,1,1])
                if x == 480:
                    y +=1
                    x = 20
                x +=1

