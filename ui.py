import pygame
from Append import tools
import time


class ui(tools):
    def print_screen(self, string="", pos=(210, 260), color='black'):
        self.screen.blit(self.font.render(
            string, True, color), pos)

    def finalScreen(self, player: int, pos: list, score: int, win: bool = True) -> None:
        ui.print_screen(self, f"Player{player}", pos, "white")
        ui.print_screen(self, f"You have got {score}", (pos[0], pos[1]+50))
        ui.print_screen(self, f"You {win}")
        return None

    def movAnimation(self, player=0, side=0):
        if player == 0:
            if side == 0:
                i = 0
                for i in range(5):
                    self.screen.fill([0, 0, 0])
                    self.player1_x += i
                    ui.aircraft_1()
                    pygame.display.update()
            if side == 1:
                i = 0
                for i in range(5):
                    self.screen.fill([0, 0, 0])
                    self.player1_x -= i
                    ui.aircraft_1()
                    pygame.display.update()

        if player == 1:
            if side == 0:
                for i in range(5):
                    self.screen.fill([0, 0, 0])
                    time.sleep(0.01)
                    self.player2_x += i
                    ui.player2Aircraft()
                    pygame.display.update()
            if side == 1:
                for i in range(5):
                    self.screen.fill([0, 0, 0])
                    time.sleep(0.01)
                    self.player2_x -= i
                    ui.player2Aircraft()
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

    def enemyAircraft(self, index):
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

    def medicine(self, index):
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

    def drawString(self, index):
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

    def bloodDock(self, player):
        text = self.font.render(
            f"{self.player1_life}", True, 'white')
        self.screen.blit(text, (self.screenWidth - 270, 20))
        text = self.font.render(
            f"{self.score}", True, "white")
        self.screen.blit(text, (30, 20))
        pygame.draw.rect(self.screen, [255, 0, 0], [
            self.screenWidth-220, 22, self.player1_life, 20])
        pygame.draw.rect(self.screen, [200, 200, 200], [
            self.screenWidth-40, 22, 10, 20])
        text = self.font.render(
            f"{self.player1_bullet}", True, "white")
        self.screen.blit(text, (self.screenWidth-90, 20))
        text = self.font.render(
            f"{self.mode}", True, "white")
        self.screen.blit(text, (70, 18))
