import pygame
import time


class egg(object):
    def bind(self):
        if self.distance > 0:
            self.distance -= self.speed
        self.player1_y = 380-int(self.distance)

    def grvaity(self, color):
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
        '''
        机身 30,144,255\n
        机翼 131,206,250
        '''
        
        pygame.draw.rect(self.screen, self.planeColor_player, [
            self.player1_x+10, self.player1_y, 20, 80]
            ,border_radius=10)
        pygame.draw.rect(self.screen, self.wigColor_player, [
            self.player1_x-32, self.player1_y+25, 42, 25],border_radius=10)
        pygame.draw.rect(self.screen, self.wigColor_player, [
            self.player1_x+30, self.player1_y+25, 42, 25],border_right_radius=10)
        pygame.draw.rect(self.screen, self.wigColor_player, [
            self.player1_x+2, self.player1_y+80, 35, 5],border_left_radius=10)
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

    def egg_graphic(self):

        while self.running:
            time.sleep(0.01)
            self.screen.fill([0,0,self.color])
            egg.grvaity(self, self.color)
            egg.fuel(self, self.color)
            if self.distance <= 320:
                egg.launch(self,)
            egg.aircraft(self,)

    def mainProgramme(self,):
        self.color = 40
        colorTimes = 0
        colorTimes += 1
        if colorTimes % 50 == 0 and self.color <= 220:
            self.color += 1
        self.running = True
        self.player1_y = 50
        self.player1_x = 230
        loopTimes = 0
        while self.running:
            loopTimes += 1
            time.sleep(0.01)
            egg.bind(self)
            loopTimes = egg.watch_egg(self, loopTimes)
            if self.player1_y <= 250:
                self.player1_y = 250
            if self.gravity <= 0:
                self.gravity = 0
            if self.gravity >= 9.80:
                self.gravity = 9.80
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
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
                    self.running = False
                    return self.score,'win'
                elif (self.player1_y == 380 and self.speed > 3):
                    self.running = False
                    return self.score,'lose'
                elif self.distance < 0:
                    self.running = False
                    return self.score,'lose'
            pygame.display.update()
