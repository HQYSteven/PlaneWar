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

class egg(object):
        def grvaity(self, color):

            if self.distance > 0:
                self.distance -= self.speed
            text = self.font.render(
                f"{round(self.gravity,2)}N/kg,{round(self.speed,2)}m/s", True, "white")
            self.screen.blit(text, (10, 10))
            text = self.font.render(
                f"{round(self.distance,2)}m", True, "white")
            self.screen.blit(text, (10, 40))

        def fuel(self, color):
            text = self.font.render(
                f"FUEL:{round(self.fuelAmount*100,2)}%", True, "white")
            self.screen.blit(text, (270, 10))

        def launch(self,):
            self.player1_y = 380-int(self.distance)
            pygame.draw.rect(self.screen, self.launcher,
                             [0, 480, 500, 20])

        def watch_egg(self, times):
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
                egg.aircraft(self,)
                if self.distance <= 320:
                    egg.launch(self,)
                egg.grvaity(self, color)
                egg.fuel(self, color)
                loopTimes = egg.watch_egg(self, loopTimes)
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
