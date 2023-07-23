import pygame
import random


class update():
    """
    This class is used to bind every crash\n
    Also,update the moving stars\n
    created in 2022
    """
    def update(master) -> None:
        """
        This fuction is used to update all the userface:\n
        stars\n
        strings players have sent out\n
        strings enemy have sent out\n
        """
        update.updateString_bindEnemy(master)
        update.updateString_bindEnemy_shot(master)
        update.updateString_bindEnemyAttack(master)
        update.bind_crash(master)
        update.updateString_bindEnemyAttack_mov(master)
        update.updateString_mov(master)
        update.bind_medicine(master)
        update.bind_stone(master)

    class judge():
        """
        This class is used to bind if two objects have crashed\n
        created on June 23rd 2023
        """
        def judgeX(object1x: int, object1Width: int,
                   object2x: int, object2Width: int) -> bool:
            '''
            This fuction is used to judge that if two object have crashed\n
            created on June 23rd 2023
            '''
            return object1x <= object2x+object2Width and object1x+object1Width >= object2x

        def judgeY(object1y: int, object1Height: int,
                   object2y: int, object2Height: int) -> bool:
            '''
            This fuction is used to judge that if two object have crashed\n
            created on June 23rd 2023
            '''
            return object1y+object1Height > object2y and object1y <= object2y+object2Height

        def judge(object1x: int, object1y: int, object1Width: int, object1Height: int,
                  object2x: int, object2y: int, object2Width: int, object2Height: int,) -> bool:
            '''
            This fuction is used to judge that if two object have crashed\n
            created on June 23rd 2023
            '''
            return (update.judge.judgeX(object1x, object1Width, object2x, object2Width) and
                    update.judge.judgeY(object1y, object1Height, object2y, object2Height))

    def updateStars(self) -> None:
        """
        This fuction is used to update stars\n
        It creates 10 or more stars per second\n
        module uesd:random\n
        created in 2022 in Poyang
        """
        minAmount = 0
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

    def updateString_mov(self,) -> None:
        """
        This fuction is used to update the string players have sent out\n
        return nothing(None)\n
        created in 2022\n
        """
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
        """
        This fuction is used to move the enemy you see and print it.\n
        enemies out of the window will be deleted\n
        created in 2022,in Poyang
        """
        index = 0
        while index >= 0 and index < len(self.enemy_x_list):
            if index < 0 or index >= len(self.enemy_x_list):
                break
            self.enemy_y_list[index] += self.movAmount
            if self.enemy_y_list[index] >= self.screenHeight:
                del self.enemy_y_list[index]
                del self.enemy_x_list[index]
                del self.enemyLifeList[index]
                index -= 1
                if self.score > 0:
                    self.score -= 10
                else:
                    self.score = 0
            if index < 0 or index >= len(self.enemy_x_list):
                break
            index += 1

    def updateString_bindEnemyAttack_mov(self,):
        """
        This fuction is used to move the enemies' strings you see and print it.\n
        strings out of the window will be deleted\n
        created in 2022,in Poyang
        """
        index = 0
        while index < len(self.otherAttack_x):
            if index < 0 or index > len(self.otherAttack_x):
                break
            try:
                self.otherAttack_y[index]
            except:
                return
            self.otherAttack_y[index] += self.stringMov+2
            if self.otherAttack_y[index] > self.screenHeight:
                del self.otherAttack_y[index]
                del self.otherAttack_x[index]
                index -= 1
            index += 1

    def updateString_bindEnemy_shot(self,):
        '''
        It binds if the enemies has been shot.
        '''
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
                if (update.judge.judge(self.attackStringX[index], self.attackStringY[index], 5, 15, self.enemy_x_list[index_enemy], self.enemy_y_list[index_enemy], 25, 25)):
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
        '''
        It binds if the enemies's stings has hurt the players.
        '''
        index = 0
        while index >= 0 and index < len(self.otherAttack_x):
            if index < 0 or index >= len(self.otherAttack_x):
                break
            if self.player2:
                if (update.judge.judge(self.otherAttack_x[index], self.otherAttack_y[index], 5, 15, self.player2_x, self.player2_y, 25, 25)):
                    del self.otherAttack_x[index]
                    del self.otherAttack_y[index]
                    self.score -= 10
                    self.player2_life -= self.hit
                    index -= 1
            if index < 0 or index >= len(self.otherAttack_x):
                break
            try:
                self.otherAttack_y[index]
            except:
                break
            if (update.judge.judge(self.otherAttack_x[index], self.otherAttack_y[index], 5, 15, self.player2_x, self.player2_y, 25, 25)):
                del self.otherAttack_y[index]
                self.score -= 10
                self.player1_life -= self.hit
                index -= 1
            index += 1
            if index < 0 or index >= len(self.otherAttack_x):
                break

    def bind_crash(self,):
        '''
        It binds if the enemies has crashed the players.
        '''
        index = 0
        while index >= 0 and index < len(self.enemy_x_list):
            if index < 0 and index >= len(self.enemy_x_list):
                break
            if (update.judge.judge(self.player1_x, self.player1_y, 50, 50, self.enemy_x_list[index], self.enemy_y_list[index], 50, 50)):

                self.enemy_y_list[index] += 15
                del self.enemy_x_list[index]
                del self.enemy_y_list[index]
                del self.enemyLifeList[index]
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
        '''
        It binds if the medicine have reached players and cured players
        '''
        index = 0
        while index >= 0 and index < len(self.medicineX):
            if index < 0 and index >= len(self.medicineX):
                break
            self.medicineY[index] += 10
            if (update.judge.judge(self.player1_x, self.player1_y, 50, 50, self.medicineX[index], self.medicineY[index], 20, 20)
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
            if self.player2 and update.judge.judge(self.player1_x, self.player1_y, 50, 50, self.medicineX[index], self.medicineY[index], 20, 20):
                del self.medicineY[index]
                del self.medicineX[index]
                self.player2_life += self.cure
                index -= 1
            index += 1

    def bind_stone(self,):
        '''
        It binds the stones if the stone has hurt the players.
        '''
        index = 0
        while index < len(self.stoneXList) and index >= 0:
            if index >= len(self.stoneXList) or index < 0:
                break
            self.stoneYList[index] += 15
            if self.stoneYList[index] >= self.screenHeight:
                del self.stoneYList[index]
                del self.stoneXList[index]
                index -= 1
            if index >= len(self.stoneXList) or index < 0:
                break
            if not self.player2:
                if (update.judge.judge(self.player1_x, self.player1_y, 50, 50, self.stoneXList[index], self.stoneYList[index], 20, 20)):
                    del self.stoneYList[index]
                    del self.stoneXList[index]
                    self.player1_life -= self.stone
                    index -= 1
            else:
                if (update.judge.judge(self.player1_x, self.player1_y, 50, 50, self.stoneXList[index], self.stoneYList[index], 20, 20)):
                    del self.stoneYList[index]
                    del self.stoneXList[index]
                    self.player2_life -= self.stone
                    index -= 1
            stringIndex = 0
            while stringIndex >= 0 and stringIndex < len(self.attackStringX):
                if stringIndex < 0 or stringIndex >= len(self.attackStringX):
                    break
                if index >= len(self.stoneXList) or index < 0:
                    break
                if self.stoneXList[index] - 3 < self.attackStringX[stringIndex] and self.stoneXList[index]+50 > self.attackStringX[stringIndex] and self.stoneYList[index] < self.attackStringY[stringIndex] and self.stoneYList[index]+20 > self.attackStringY[stringIndex]:
                    del self.stoneXList[index]
                    del self.stoneYList[index]
                    self.attackStringY[stringIndex] += 10
                    del self.attackStringX[stringIndex]
                    del self.attackStringY[stringIndex]
                    index -= 1
                    stringIndex -= 1
                    self.score += 10
                stringIndex += 1
            index += 1
