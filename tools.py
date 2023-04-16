import pygame
import time
import random
import _thread
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
    class ui(object):
        def movAnimation(player=0, side=0):
            if player == 0:
                if side == 0:
                    i = 0
                    for i in range(5):
                        programme.screen.fill([0,0,0])
                        programme.player1_x += i
                        tools.ui.aircraft_1()
                        pygame.display.update()
                if side == 1:
                    i = 0
                    for  i in range(5):
                        programme.screen.fill([0,0,0])
                        programme.player1_x -= i
                        tools.ui.aircraft_1()
                        pygame.display.update()
                        
            if player == 1:
                if side == 0:
                    for i in range(5):
                        programme.screen.fill([0,0,0])
                        time.sleep(0.01)
                        programme.player2_x += i
                        tools.ui.player2Aircraft()
                        pygame.display.update()
                if side == 1:
                    for i in range(5):
                        programme.screen.fill([0,0,0])
                        time.sleep(0.01)
                        programme.player2_x -= i
                        tools.ui.player2Aircraft()
                        pygame.display.update()

        def aircraft_1():
            # 机身 30,144,255
            # 机翼 131,206,250
            pygame.draw.circle(programme.screen, programme.planeColor_player, [
                programme.player1_x+15, programme.player1_y], 5)
            pygame.draw.rect(programme.screen, programme.planeColor_player, [
                programme.player1_x+10, programme.player1_y, 10, 31])
            pygame.draw.rect(programme.screen, programme.wigColor_player, [
                programme.player1_x-2, programme.player1_y+15, 12, 10])
            pygame.draw.rect(programme.screen, programme.wigColor_player, [
                programme.player1_x+20, programme.player1_y+15, 12, 10])
            pygame.draw.rect(programme.screen, programme.wigColor_player, [
                programme.player1_x+5, programme.player1_y+31, 20, 3])
            
        def enemyAircraft(index):
            # 机身 192,192,192
            # 机翼 178,34,34
            
            pygame.draw.rect(programme.screen, programme.planeColor_enemy, [
                programme.enemy_x_list[index]+3, programme.enemy_y_list[index], 22, 3])
            pygame.draw.rect(programme.screen, programme.planeColor_enemy, [
                programme.enemy_x_list[index]+10, programme.enemy_y_list[index], 10, 35])
            pygame.draw.rect(programme.screen, programme.wigColor_enemy, [
                programme.enemy_x_list[index]-2, programme.enemy_y_list[index]+10, 12, 10])
            pygame.draw.rect(programme.screen, programme.wigColor_enemy, [
                programme.enemy_x_list[index]+20, programme.enemy_y_list[index]+10, 12, 10])
            pygame.draw.circle(programme.screen, programme.planeColor_enemy, [
                programme.enemy_x_list[index]+15, programme.enemy_y_list[index]+35], 5)
            pygame.draw.rect(programme.screen, [0,0,0], [
                programme.enemy_x_list[index]+3, programme.enemy_y_list[index]+2, 22, 3])
            pygame.draw.rect(programme.screen, [255,0,0], [
                programme.enemy_x_list[index]+2, programme.enemy_y_list[index]-programme.movAmount-3, int(programme.enemyLifeList[index]/4), 3])

        def player2Aircraft():
            pygame.draw.circle(programme.screen, programme.planeColor_player, [
                programme.player2_x+15, programme.player2_y], 5)
            pygame.draw.rect(programme.screen, programme.planeColor_player, [
                programme.player2_x+10, programme.player2_y, 10, 31])
            pygame.draw.rect(programme.screen, programme.wigColor_player, [
                programme.player2_x-2, programme.player2_y+15, 12, 10])
            pygame.draw.rect(programme.screen, programme.wigColor_player, [
                programme.player2_x+20, programme.player2_y+15, 12, 10])
            pygame.draw.rect(programme.screen, programme.wigColor_player, [
                programme.player2_x+5, programme.player2_y+31, 20, 3])
            pygame.draw.rect(programme.screen, [255,0,0], [
                programme.player2_x, programme.player2_y+39, int( programme.player2_life/3), 2])
        def medicine(index):
            pygame.draw.rect(programme.screen, [255, 255, 255], [
                programme.medicineX[index],programme.medicineY[index], 20, 20])
            pygame.draw.rect(programme.screen, [255, 0, 0], [
                programme.medicineX[index]+2, programme.medicineY[index]+8, 16, 4])
            pygame.draw.rect(programme.screen, [255, 0, 0], [
                programme.medicineX[index]+8, programme.medicineY[index]+3, 4, 16])
            
        def switchAnimation():
            fillPos = 0
            while fillPos <= 500:
                time.sleep(0.005)
                pygame.draw.rect(programme.screen, [0, 0, 0], [
                    0, fillPos, 500, 100])
                fillPos += 10
                pygame.display.update()
        def drawString(index):
            if programme.mode=='normal':
                width = 3
            elif programme.mode == 'artillery':
                width = 4
            elif programme.mode == 'Xrate':
                width = 5
            elif programme.mode == 'missile':
                width = 6
            try:
                pygame.draw.rect(programme.screen, programme.AttackColor, [
                    programme.attackStringX[index], programme.attackStringY[index]+10, width , 10])
            except:
                pass

        def bloodDock(player):
                pygame.draw.rect(programme.screen,[128,128,128],[20,10,460,50])
                pygame.draw.circle(programme.screen,[128,128,128],[20,20],10)
                pygame.draw.circle(programme.screen,[128,128,128],[480,20],10)
                pygame.draw.circle(programme.screen,[128,128,128],[20,50],10)
                pygame.draw.circle(programme.screen,[128,128,128],[480,50],10)
                pygame.draw.rect(programme.screen,[128,128,128],[10,20,10,35])
                pygame.draw.rect(programme.screen,[128,128,128],[480,20,10,35])
                
                text = programme.font.render(
                    f"{programme.player1_life}", True, 'white')
                programme.screen.blit(text, (programme.screenWidth - 270, 20))
                text = programme.font.render(
                    f"{programme.score}", True, "white")
                programme.screen.blit(text, (30, 20))
                pygame.draw.rect(programme.screen, [255, 0, 0], [
                    programme.screenWidth-220, 20, programme.player1_life, 20])
                pygame.draw.rect(programme.screen, [200, 200, 200], [
                    programme.screenWidth-40, 20, 10, 20])
                text = programme.font.render(
                    f"{programme.player1_bullet}", True, "white")
                programme.screen.blit(text, (programme.screenWidth-90, 20))
                text = programme.font.render(
                    f"{programme.mode}", True, "white")
                programme.screen.blit(text, (70, 20))
            
    class bind(object):

        def watch(times):
            colorPlus = 70-programme.planeColor_player[0]
            if programme.god == True:
                score = 10000
                programme.crash = 0
                programme.hit = 5
                programme.attack = 0
                programme.bullet = 0
                programme.stone = 0
                programme.cure = 100
                programme.stringMov = 1
                programme.minus = 0
            else:
                programme.minus = 10
                programme.crash = 10
                programme.hit = 5
                programme.attack = 20
                programme.bullet = 20
                programme.stone = 1
                programme.cure = 50
                programme.stringMov = 10
            if len(programme.enemy_x_list) >=2 and times % 2 == 0:
                index = random.randint(0,len(programme.enemy_x_list))
                programme.otherAttack_x.append(programme.enemy_x_list[index-1]+13)
                programme.otherAttack_y.append(programme.enemy_y_list[index-1]+50)
            if programme.mov == True:
                if programme.movDirect == 0:
                    programme.player1_x -= 5
                if programme.movDirect == 1:
                    programme.player1_x += 5
                programme.mov = False
                tools.ui.aircraft_1()
            if programme.mov == True and programme.player2:
                if programme.movDirect == 0:
                    programme.player2_x -= 5
                if programme.movDirect == 1:
                    programme.player2_x += 5
                programme.mov = False
                tools.ui.aircraft_1()
            if times == 20:
                programme.stoneXList.append(
                    random.randint(0, programme.screenWidth))
                programme.stoneYList.append(0)
            if programme.player1_life < 0:
                programme.player1_life = 0
                print("YOU LOSE")
                quit()
            if programme.player2_life < 0:
                programme.player2_life = 0
                print("YOU LOSE")
                quit()

            if programme.score < 0:
                programme.score = 0
            if not programme.player2:
                if programme.player1_life < 50 and programme.medicineAmount > 0 and times == 20:
                    tools.appendMedicine()
            else:
                if (programme.player1_life < 50 or programme.player2_life < 50) and times == 20:
                    tools.appendMedicine()
            # 每3.2秒出现一架飞机
            if times == 22 and programme.planeAmount:
                # 重新计数
                times = 0
                # 在敌方位置列表中添加坐标
                tools.appendEnemy()
            if programme.player2:
                if programme.player1_life <= 0 and programme.player2_life <= 0 or programme.planeAmount == 0:
                    programme.message.append("switch")
                    print("=======/The Game Has Finished\\========")
                    print(f"Player One Has Got:{programme.player1_life} left.")
                    print(f"You Have Got : {programme.score}")
                    if programme.planeAmount:
                        print("YOU LOSE")
                    else:
                        tools.egg.mainProgramme()
                        programme.screen.quit()
                        quit()
            else:
                if programme.player1_life <= 0 or programme.planeAmount == 0:
                    programme.message.append("switch")
                    print("=======/The Game Has Finished\\========")
                    print(f"Player One Has Got:{programme.player1_life} left.")
                    print(f"Player Two Has Got:{programme.player2_life} left.")
                    print(f"You Have Got : {programme.score}")
                    if programme.planeAmount:
                        print("YOU LOSE")
                    else:
                        tools.egg.mainProgramme()
                        programme.screen.quit()
                        quit()
            return times

        def keyEvent(event):
            # 左键处理
            if programme.player1_life > 0:
                if event.key == pygame.K_LEFT:
                    programme.mov = True
                    programme.movDirect = 0
                if event.key == pygame.K_RIGHT:
                    programme.mov = True
                    programme.movDirect = 1
                if event.key == pygame.K_F1:
                    programme.attack = programme.bullet
                    programme.mode = 'normal'
                    programme.AttackColor = programme.color1
                if event.key == pygame.K_F2:
                    programme.attack = programme.artillery
                    programme.mode = 'artillery'
                    programme.AttackColor = programme.color2
                if event.key == pygame.K_F3:
                    programme.attack = programme.Xrate
                    programme.mode = 'Xrate'
                    programme.AttackColor = programme.color3
                if event.key == pygame.K_F4:
                    programme.attack = programme.missile
                    programme.mode = 'missile'
                    programme.AttackColor = programme.color4
                if event.key == pygame.K_UP:
                    # 识别是否有剩子弹
                    if programme.player1_bullet:
                        # 添加子弹坐标
                        tools.appendAttack()
                        programme.player1_bullet -= 1
            if programme.player2 and programme.player2_life > 0:
                if event.key == pygame.K_a:
                    programme.player2_x-=1
                if event.key == pygame.K_d:
                    programme.player2_x +=1
                if event.key == pygame.K_w:
                    if programme.player2_bullet:
                        if programme.player2_x != programme.player1_x:
                            tools.appendAttack(0)
                            programme.player2_bullet -= 1
    # 刷新子弹
            if event.type == pygame.MOUSEMOTION and not programme.player2:
                programme.player1_x = pygame.mouse.get_pos()[0]
                if programme.player1_x > 480:
                    programme.player1_x = 480

    def appendMedicine():
        programme.medicineX.append(random.randint(0, 480))
        programme.medicineY.append(0)
        programme.medicineAmount -= 1

    def appendEnemy():
        num = random.randint(0, programme.screenWidth-30)
        programme.enemy_x_list.append(num)
        programme.enemy_y_list.append(50)
        programme.otherAttack_x.append(num+13)
        programme.otherAttack_y.append(10)
        programme.enemyLifeList.append(100)
        programme.planeAmount -= 1

    def appendAttack(player=1):
        if player:
            programme.attackStringX.append(programme.player1_x+13)
            programme.attackStringY.append(programme.screenHeight - 100)
        else:
            programme.attackStringX.append(programme.player2_x+13)
            programme.attackStringY.append(programme.screenHeight - 80)

    class update(object):
        def updateStars():
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
            

        def updateString_mov():
            index = 0
            while index >= 0 and index < len(programme.attackStringX):
                if index < 0 or index >= len(programme.attackStringX):
                    break
                programme.attackStringY[index] -= programme.stringMov
                if programme.attackStringY[index] < -20:
                    del programme.attackStringY[index]
                    del programme.attackStringX[index]
                    index -= 1
                index += 1

        def updateString_bindEnemy():
            index = 0
            while index >= 0 and index < len(programme.enemy_x_list):
                if index < 0 or index >= len(programme.enemy_x_list):
                    break
                programme.enemy_y_list[index] += programme.movAmount
                if programme.enemy_y_list[index] >= programme.screenHeight:
                    del programme.enemy_y_list[index]
                    del programme.enemy_x_list[index]
                    index -= 1
                    if programme.score > 0:
                        programme.score -= 10
                    else:
                        programme.score = 0
                if index < 0 or index >= len(programme.enemy_x_list):
                    break
                index += 1

        def updateString_bindEnemyAttack_mov():
            index = 0
            while index < len(programme.otherAttack_x):
                if index < 0 or index >= len(programme.otherAttack_x):
                    break
                programme.otherAttack_y[index] += programme.stringMov+2
                if programme.otherAttack_y[index] > programme.screenHeight:
                    del programme.otherAttack_y[index]
                    del programme.otherAttack_x[index]
                    index -= 1
                index += 1

        def updateString_bindEnemy_shot():
            index = 0
            while index < len(programme.attackStringX):
                index_enemy = 0
                if index > len(programme.attackStringX) or index < 0:
                    break
                while index_enemy < len(programme.enemy_x_list):
                    if index_enemy > len(programme.enemy_x_list) or index_enemy < 0:
                        break
                    if index > len(programme.attackStringX) or index < 0:
                        break
                    if (
                        (
                            (
                                programme.attackStringX[index] >= programme.enemy_x_list[index_enemy]-3
                            )
                            and
                            (
                                programme.attackStringX[index] <= programme.enemy_x_list[index_enemy]+31
                            )
                        )
                        and
                        (
                            (
                                programme.attackStringY[index] >= programme.enemy_y_list[index_enemy]-5
                            )
                            and
                            (
                                programme.attackStringY[index] <= programme.enemy_y_list[index_enemy] + 15
                            )
                        )
                    ):
                        programme.attackStringY[index] += programme.stringMov
                        programme.enemyLifeList[index_enemy] -= 20

                        del programme.attackStringX[index]
                        del programme.attackStringY[index]
                        index -= 1

                        programme.enemyLifeList[index_enemy] -= programme.attack
                        if programme.enemyLifeList[index_enemy] <= 0:
                            programme.enemy_y_list[index_enemy] += programme.movAmount
                            del programme.enemy_x_list[index_enemy]
                            del programme.enemy_y_list[index_enemy]
                            del programme.enemyLifeList[index_enemy]
                            index_enemy -= 1
                            programme.score += 10
                    index_enemy += 1
                index += 1

        def updateString_bindEnemyAttack():
            index = 0
            while index >= 0 and index < len(programme.otherAttack_x):
                if index < 0 or index >= len(programme.otherAttack_x):
                    break
                if programme.player2:
                    if ((programme.otherAttack_x[index] >= programme.player2_x-3 and programme.otherAttack_x[index] <= programme.player2_x + 31)
                            and (programme.otherAttack_y[index] >= programme.player2_y and programme.otherAttack_y[index] < - programme.player2_y+20) and programme.player2):
                        del programme.otherAttack_x[index]
                        del programme.otherAttack_y[index]
                        programme.score -= 10
                        programme.player2_life -= programme.hit
                        index -= 1
                if index < 0 or index >= len(programme.otherAttack_x):
                    break
                if ((programme.otherAttack_x[index] >= programme.player1_x-3 and programme.otherAttack_x[index] <= programme.player1_x + 31)
                        and (programme.otherAttack_y[index] >= programme.player1_y and programme.otherAttack_y[index] <= programme.player1_y+20)):
                    del programme.otherAttack_x[index]
                    del programme.otherAttack_y[index]
                    programme.score -= 10
                    programme.player1_life -= programme.hit
                    index -= 1
                index += 1
                if index < 0 or index >= len(programme.otherAttack_x):
                    break

        def bind_crash():

            index = 0
            while index >= 0 and index < len(programme.enemy_x_list):
                if index < 0 and index >= len(programme.enemy_x_list):
                    break
                if ((programme.enemy_x_list[index] >= programme.player1_x-30 and
                    programme.enemy_x_list[index] <= programme.player1_x+30)
                    and
                    (
                    programme.enemy_y_list[index] >= programme.player1_y-30
                    and programme.enemy_y_list[index] <= programme.player1_y+60
                )):

                    programme.enemy_y_list[index] += 15
                    del programme.enemy_x_list[index]
                    del programme.enemy_y_list[index]
                    programme.score -= 10
                    del programme.enemyLifeList[index]
                    programme.player1_life -= programme.crash
                    index -= 1
                try:
                    programme.enemy_x_list[index]
                except:
                    break
                if ((programme.enemy_x_list[index] >= programme.player2_x-30 and
                    programme.enemy_x_list[index] <= programme.player2_x+60)
                    and programme.player2 and
                    (
                    programme.enemy_y_list[index] >= programme.player2_y
                    and programme.enemy_y_list[index] <= programme.player2_y+60 and programme.player2
                )):
                    del programme.enemy_x_list[index]
                    del programme.enemy_y_list[index]
                    del programme.enemyLifeList[index]
                    programme.score -= 20
                    programme.player2_life -= programme.crash
                    index -= 1
                    programme.enemy_y_list[index] += 10
                index += 1

        def bind_medicine():
            index = 0
            while index >= 0 and index < len(programme.medicineX):
                if index < 0 and index >= len(programme.medicineX):
                    break
                programme.medicineY[index] += 10
                if (
                    (programme.medicineX[index] > programme.player1_x -
                     19 and programme.player1_x + 20 > programme.medicineX[index])
                    and
                    (programme.medicineY[index] > programme.player1_y -
                     35 and programme.player1_y + 35 > programme.medicineY[index])

                ):
                    del programme.medicineY[index]
                    del programme.medicineX[index]
                    programme.player1_life += programme.cure
                    index -= 1
                if index < 0 and index >= len(programme.medicineX):
                    break
                try:
                    programme.medicineX[index]
                except:
                    break
                if (
                    (programme.medicineX[index] > programme.player2_x -
                     19 and programme.player2_x + 20 > programme.medicineX[index])
                    and
                    (programme.medicineY[index] > programme.player2_y -
                     35 and programme.player2_y + 35 > programme.medicineY[index])
                    and programme.player2
                ):
                    del programme.medicineY[index]
                    del programme.medicineX[index]
                    programme.player2_life += programme.cure
                    index -= 1
                index += 1

        def bind_stone():
            index_stone = 0
            while index_stone < len(programme.stoneXList) and index_stone >= 0:
                if index_stone >= len(programme.stoneXList) or index_stone < 0:
                    break
                programme.stoneYList[index_stone] += 15
                if programme.stoneYList[index_stone] >= programme.screenHeight:
                    del programme.stoneYList[index_stone]
                    del programme.stoneXList[index_stone]
                    index_stone -= 1
                if index_stone >= len(programme.stoneXList) or index_stone < 0:
                    break
                if not programme.player2:
                    if ((programme.player1_x-30 > programme.stoneXList[index_stone] and programme.stoneXList[index_stone] < programme.player1_x + 30)
                            and (programme.player1_y - 20 < programme.stoneYList[index_stone]) and programme.stoneYList[index_stone] < programme.player1_y+50):
                        del programme.stoneYList[index_stone]
                        del programme.stoneXList[index_stone]
                        tools.ui.aircraft_1()
                        programme.player1_life -= programme.stone
                        index_stone -= 1
                else:
                    if ((programme.player2_x-20 > programme.stoneXList[index_stone] and programme.stoneXList[index_stone] < programme.player2_x + 40)
                            and (programme.player2_y - 20 < programme.stoneYList[index_stone]) and programme.stoneYList[index_stone] < programme.player2_y + 20):
                        del programme.stoneYList[index_stone]
                        del programme.stoneXList[index_stone]
                        tools.ui.player2Aircraft()
                        programme.player2_life -= programme.stone
                        index_stone -= 1
                stringIndex = 0
                while stringIndex >= 0 and stringIndex < len(programme.attackStringX):
                    if stringIndex < 0 or stringIndex >= len(programme.attackStringX):
                        break
                    if index_stone >= len(programme.stoneXList) or index_stone < 0:
                        break
                    if programme.stoneXList[index_stone] - 3 < programme.attackStringX[stringIndex] and programme.stoneXList[index_stone]+50 > programme.attackStringX[stringIndex] and programme.stoneYList[index_stone] < programme.attackStringY[stringIndex] and programme.stoneYList[index_stone]+20 > programme.attackStringY[stringIndex]:
                        del programme.stoneXList[index_stone]
                        del programme.stoneYList[index_stone]
                        programme.attackStringY[stringIndex] += 10
                        del programme.attackStringX[stringIndex]
                        del programme.attackStringY[stringIndex]
                        index_stone -= 1
                        stringIndex -= 1
                        programme.score += 10
                    stringIndex += 1
                index_stone += 1

        def update():
            tools.update.updateString_bindEnemy()
            tools.update.updateString_bindEnemy_shot()
            tools.update.updateString_bindEnemyAttack()
            tools.update.bind_crash()
            tools.update.updateString_bindEnemyAttack_mov()
            tools.update.updateString_mov()
            tools.update.bind_medicine()
            tools.update.bind_stone()
#################################################################
    class egg(object):
        def grvaity(color):

            if programme.distance > 0:
                programme.distance -= programme.speed
            text = programme.font.render(
                f"{round(programme.gravity,2)}N/kg,{round(programme.speed,2)}m/s", True, "white")
            programme.screen.blit(text, (10, 10))
            text = programme.font.render(
                f"{round(programme.distance,2)}m", True, "white")
            programme.screen.blit(text, (10, 40))

        def fuel(color):
            text = programme.font.render(
                f"FUEL:{round(programme.fuelAmount*100,2)}%", True, "white")
            programme.screen.blit(text, (270, 10))

        def launch():
            programme.player1_y = 380-int(programme.distance)
            pygame.draw.rect(programme.screen, programme.launcher,
                             [0, 480, 500, 20])

        def watch_egg(times):
            if times % 10 == 0:
                programme.gravity += programme.add
                if programme.distance > 0:
                    programme.speed += programme.gravity
                times = 0
            if programme.lostFuel and programme.fuelAmount > 0:
                programme.fuelAmount -= programme.lost
                programme.speed -= programme.lost*50
                if programme.speed < 0:
                    programme.gravity -= programme.add
                if programme.gravity < 0:
                    programme.gravity = 0
            return times

        def aircraft():
            # 机身 30,144,255
            # 机翼 131,206,250
            pygame.draw.circle(programme.screen, programme.planeColor_player, [
                programme.player1_x+20, programme.player1_y], 10)
            pygame.draw.rect(programme.screen, programme.planeColor_player, [
                programme.player1_x+10, programme.player1_y, 20, 80])
            pygame.draw.rect(programme.screen, programme.wigColor_player, [
                programme.player1_x-32, programme.player1_y+25, 42, 25])
            pygame.draw.rect(programme.screen, programme.wigColor_player, [
                programme.player1_x+30, programme.player1_y+25, 42, 25])
            pygame.draw.rect(programme.screen, programme.wigColor_player, [
                programme.player1_x+2, programme.player1_y+80, 35, 5])
            pygame.draw.polygon(programme.screen, programme.planeColor_player, [(
                programme.player1_x-10, programme.player1_y+25), (programme.player1_x-23, programme.player1_y+25),
                (programme.player1_x-17, programme.player1_y+15)])
            pygame.draw.polygon(programme.screen, programme.planeColor_player, [(
                programme.player1_x+43, programme.player1_y+25), (programme.player1_x+56, programme.player1_y+25),
                (programme.player1_x+50, programme.player1_y+15)])
            pygame.draw.polygon(programme.screen, programme.planeColor_player, [(
                programme.player1_x+43, programme.player1_y+25), (programme.player1_x+56, programme.player1_y+25),
                (programme.player1_x+50, programme.player1_y+15)])
            if programme.lostFuel:
                pygame.draw.polygon(programme.screen, programme.fire, [
                    (programme.player1_x+45, programme.player1_y +
                     66), (programme.player1_x+55, programme.player1_y+66),
                    (programme.player1_x+50, programme.player1_y+programme.length)])
                pygame.draw.polygon(programme.screen, programme.fire, [
                    (programme.player1_x-15, programme.player1_y +
                     66), (programme.player1_x-25, programme.player1_y+66),
                    (programme.player1_x-20, programme.player1_y+programme.length)])
        
        def mainProgramme():
            colorTimes = 0
            programme.running = True
            loopTimes = 0
            color = 40
            programme.player1_y = 50
            programme.player1_x = 230
            while programme.running:
                loopTimes += 1
                colorTimes += 1
                if colorTimes % 50 == 0 and color <= 220:
                    color += 1
                programme.initColor = [10, 10, color]
                pygame.draw.rect(programme.screen, [color-(150 if color > 150 else color), color-(
                    100 if color > 100 else color), color], [0, 0, 500, 500])
                time.sleep(0.015)
                tools.egg.aircraft()
                if programme.distance <= 320:
                    tools.egg.launch()
                tools.egg.grvaity(color)
                tools.egg.fuel(color)
                loopTimes = tools.egg.watch_egg(loopTimes)
                if programme.player1_y <= 200:
                    programme.player1_y =0
                if programme.gravity <= 0:
                    programme.gravity = 0
                if programme.gravity >= 9.80:
                    programme.gravity = 9.80
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and programme.fuelAmount > 0:
                            programme.lostFuel = True
                        if event.key == pygame.K_F1:
                            programme.lost *= 1.5
                            programme.length += 10
                        if event.key == pygame.K_F2:
                            programme.lost /= 1.5
                            programme.length -= 10
                    if event.type == pygame.KEYUP:
                        if programme.lostFuel:
                            programme.lostFuel = False

                    if (programme.player1_y == 380 and programme.speed <= 3):
                        print("YOU WIN")
                        pygame.quit()
                        quit()
                    elif (programme.player1_y == 380 and programme.speed > 3):
                        print("YOU LOSE")
                        pygame.quit()
                        quit()
                pygame.display.update()


class programme:
    class graphic_update(object):
        def string():
            index = 0
            while index >= 0 and index < len(programme.attackStringX):
                tools.ui.drawString(index)
                index +=1
        def ememyString():
            index = 0
            while index < len(programme.otherAttack_x):
                pygame.draw.rect(programme.screen, [0, 255, 0], [
                    programme.otherAttack_x[index], programme.otherAttack_y[index], 3, 10])
                index +=1
        def medicine():
            index = 0
            while index >= 0 and index < len(programme.medicineX):
                tools.ui.medicine(index)
                index +=1
        def stone():
            index_stone = 0
            while index_stone < len(programme.stoneXList) and index_stone >= 0:
                pygame.draw.rect(programme.screen, [255, 255, 255], [
                    programme.stoneXList[index_stone], programme.stoneYList[index_stone], 20, 20])
                index_stone +=1
        def enemy():
            index = 0
            while index >= 0 and index < len(programme.enemy_x_list):
                tools.ui.enemyAircraft(index)
                index +=1
    def graphics(a,player2 = False):
        programme.player2 = player2
        tools.ui.switchAnimation()
        index = 0
        while programme.running:
            time.sleep(0.08)
            for message in programme.message:

                if message == 'switch':
                    tools.ui.switchAnimation()
                    del programme.message[index]
                    continue
                
                index +=1
            programme.screen.fill([0,0,0])
            if player2:
                tools.ui.bloodDock(0)
            tools.ui.bloodDock(1)
            tools.ui.aircraft_1()
            if programme.player2:
                tools.ui.player2Aircraft()
            programme.graphic_update.string()
            programme.graphic_update.ememyString()
            programme.graphic_update.medicine()
            tools.update.updateStars()
            programme.graphic_update.stone()
            programme.graphic_update.enemy()
            pygame.display.update()
            
            
    def main(player2=False):
        """
        plane War
        """
        

        # 显示玩家血量
        times = 0
        programme.running = True
        _thread.start_new_thread(programme.graphics,(False,programme.player2))
        while programme.running:
            programme.screenWidth = pygame.display.get_window_size()[0]
            programme.screenHeight = pygame.display.get_window_size()[1]
            
            if not programme.playing:
                pygame.quit()
                break
            
            if programme.player2:
                programme.player2_y = programme.screenHeight - 45
            programme.player1_y = programme.screenHeight - 90
            tools.ui.aircraft_1()
            # 当没有飞机时，退出
            times = tools.bind.watch(times)
            # 每次循环停止0.015秒，25FPS/s,用于减轻CPU压力
            time.sleep(1/programme.fps)
            times += 1
            # 事件识别
            for event in pygame.event.get():
                # 退出监测
                if event.type == pygame.QUIT:
                    programme.running = False
                # 监测是否键盘事件发生
                if event.type == pygame.KEYDOWN:
                    tools.bind.keyEvent(event)
            tools.update.update()
            
