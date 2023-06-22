import pygame
import time
import random
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

    
class Append(object):
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

    def appendAttack(self, player=1):
        if player:
            self.attackStringX.append(self.player1_x+13)
            self.attackStringY.append(self.screenHeight - 100)
        else:
            self.attackStringX.append(self.player2_x+13)
            self.attackStringY.append(self.screenHeight - 80)

#################################################################
