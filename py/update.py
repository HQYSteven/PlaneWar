import pygame
import random


class update():
    """
    This class is used to detect every crash\n
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
        update.updateString_detectEnemy(master)
        update.updateString_detectEnemy_shot(master)
        update.updateString_detectEnemyAttack_mov(master)
        update.updateString_mov(master)
        update.move_medicines(master)
        index = 0
        for index in range(len(master.playerxList)):
            update.detect_crash(master,index)
            update.updateString_detectEnemyAttack(master,index)
            update.detect_medicine(master,index)
            update.detect_stone(master,index)

    class judge():
        """
        This class is used to detect if two objects have crashed\n
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
                del self.starYList[indexStar],self.starXList[indexStar]
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
                del self.attackStringY[index],self.attackStringX[index]
                index -= 1
            index += 1

    def updateString_detectEnemy(self,):
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
                del self.enemy_y_list[index],self.enemy_x_list[index],self.enemyLifeList[index]
                index -= 1
                if self.score > 0:
                    self.score -= 10
                else:
                    self.score = 0
            if index < 0 or index >= len(self.enemy_x_list):
                break
            index += 1

    def updateString_detectEnemyAttack_mov(self,):
        """
        This fuction is used to move the enemies' strings you see and print it.\n
        strings out of the window will be deleted\n
        created in 2022,in Poyang
        """
        index = 0
        min = 0
        while index < len(self.otherAttack_x)-1:
            try:
                self.otherAttack_y[index+min] += self.stringMov+1
            except:
                break
            if self.otherAttack_y[index+min] >= 500:
                del self.otherAttack_x[index+min],self.otherAttack_y[index+min]
                min -= 1
            index += 1

    def updateString_detectEnemy_shot(self,):
        '''
        It detects if the enemies has been shot.
        '''
        index = 0
        min_enemy = 0
        min = 0
        while index < len(self.attackStringX):
            index_enemy = 0
            while index_enemy < len(self.enemy_x_list):
                if (update.judge.judge(self.attackStringX[index+min], self.attackStringY[index+min], 5, 15, self.enemy_x_list[index_enemy+min_enemy], self.enemy_y_list[index_enemy+min_enemy], 25, 25)):
                    
                    del self.attackStringX[index+min] ,self.attackStringY[index+min]
                    min -= 1
                    self.enemyLifeList[index_enemy+min_enemy] -= self.attack
                    if self.enemyLifeList[index_enemy+min_enemy] -20 <= 0:
                        del self.enemy_x_list[index_enemy+min_enemy],self.enemy_y_list[index_enemy+min_enemy],self.enemyLifeList[index_enemy+min_enemy]
                        min_enemy -= 1
                        self.score += 10
                index_enemy += 1
            index += 1

    def updateString_detectEnemyAttack(self, playerIndex):
        '''
        It detects if the enemies's stings has hurt the players.
        '''
        index = 0
        min = 0
        while index >= 0 and index < len(self.otherAttack_x)-1:
            if (update.judge.judge(self.otherAttack_x[index+min], self.otherAttack_y[index+min], 5, 15, self.playerxList[playerIndex], self.playeryList[playerIndex], 25, 25)):
                del self.otherAttack_y[index+min],self.otherAttack_x[index+min]
                self.score -= 10
                self.player1_life -= self.hit
                min -=1
            index += 1

    def detect_crash(self, playerIndex):
        '''
        It detects if the enemies has crashed the players.
        '''
        index = 0
        min = 0
        while index >= 0 and index < len(self.enemy_x_list)-1:
            if (update.judge.judge(self.playerxList[playerIndex], self.playeryList[playerIndex], 50, 50, self.enemy_x_list[index+min], self.enemy_y_list[index+min], 50, 50)):
                self.enemy_y_list[index+min] += 15
                del self.enemy_x_list[index+min],self.enemyLifeList[index+min],self.enemy_y_list[index+min],
                self.score -= 10
                self.player1_life -= self.crash
                min -=1
            index += 1

    def detect_medicine(self, playerIndex):
        '''
        It detects if the medicine have reached players and cured players
        '''
        index = 0
        min = 0
        while index >= 0 and index < len(self.medicineX)-1:
            if (update.judge.judge(self.playerxList[playerIndex], self.playeryList[playerIndex], 50, 50, self.medicineX[index+min], self.medicineY[index+min], 20, 20)
                    ):
                del self.medicineY[index+min],self.medicineX[index+min]
                self.player1_life += self.cure
                min -= 1
            index += 1
    def move_medicines(self):
        index = 0
        while index >= 0 and index < len(self.medicineX):
            self.medicineY[index] += 10
            index +=1
    def move_stones(self):
        index = 0
        while index < len(self.stoneXList) and index >= 0:
            self.stoneYList[index] += 15
            index +=1
    def detect_stone(self, playerIndex):
        '''
        It detects the stones if the stone has hurt the players.
        '''
        index = 0
        min = 0
        min_string = 0
        while index < len(self.stoneXList) and index >= 0:
            if self.stoneYList[index+min] >= self.screenHeight:
                del self.stoneYList[index+min],self.stoneXList[index+min]
                min -= 1

            if (update.judge.judge(self.playerxList[playerIndex], self.playeryList[playerIndex], 50, 50, self.stoneXList[index+min], self.stoneYList[index+min], 20, 20)):
                del self.stoneYList[index+min],self.stoneXList[index+min]
                self.player1_life -= self.stone
                min -= 1
            stringIndex = 0
            while stringIndex >= 0 and stringIndex < len(self.attackStringX):
                if (update.judge.judge(self.stoneXList[index+min],self.stoneYList[index+min],20,20,self.attackStringX[stringIndex+min_string],self.attackStringY[stringIndex+min_string],5,20)):
                    del self.stoneXList[index+min],self.stoneYList[index+min],self.attackStringX[stringIndex+min_string],self.attackStringY[stringIndex+min_string]
                    min -= 1
                    min_string -= 1
                    self.score += 10
                stringIndex += 1
            index += 1
