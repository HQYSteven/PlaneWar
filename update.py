import pygame
import random
from ui import ui
class update():
        def update(master):
            update.updateString_bindEnemy(master)
            update.updateString_bindEnemy_shot(master)
            update.updateString_bindEnemyAttack(master)
            update.bind_crash(master)
            update.updateString_bindEnemyAttack_mov(master)
            update.updateString_mov(master)
            update.bind_medicine(master)
            update.bind_stone(master)
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
                        ui.aircraft_1(self,)
                        self.player1_life -= self.stone
                        index_stone -= 1
                else:
                    if ((self.player2_x-20 > self.stoneXList[index_stone] and self.stoneXList[index_stone] < self.player2_x + 40)
                            and (self.player2_y - 20 < self.stoneYList[index_stone]) and self.stoneYList[index_stone] < self.player2_y + 20):
                        del self.stoneYList[index_stone]
                        del self.stoneXList[index_stone]
                        ui.player2Aircraft(self,)
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

        