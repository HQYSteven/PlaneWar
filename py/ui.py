import pygame
from tools import tools
import time
'''
This file contains nearly all the UIs in the game while running the main programme
created in 2022.
'''


class ui(tools):
    '''
    All the UIs are in it.
    '''

    def print_screen(self, string: str = "", pos: list = (210, 260), color: str = 'black') -> None:
        '''
        @ string: The string you want to print at.
        @ pos: The pso you want to print the string at.
        @ color: The color th estring will be.\n
        This fuc prints a message on a pygame screen
        '''
        self.screen.blit(self.font.render(
            string, True, color), pos)

    def finalScreen(self, player: int, pos: list, score: int, win: bool = True) -> None:
        '''
        @ player: The player you want to print at.
        @ pos: The po you want to place it
        @ score: the score players have got
        @ win: It judges if the players have won.
        The final screen of the game
        '''
        ui.print_screen(self, f"Player{player}", pos, "white")
        ui.print_screen(self, f"You have got {score}", (pos[0], pos[1]+50))
        ui.print_screen(self, f"You {win}")
        return None

    def movAnimation(self, player: int = 0, side: int = 0) -> None:
        """
        @ player: int = [0,1], decide which player you want to move.\n
        @ side: The direction you want to move to\n
        This fuction achieved a simple animate effect of the players' moving.
        """
        # player1's
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
        # player2's
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

    def aircraft_1(self,) -> None:
        '''
        This fuc draws the player1's plane.\n
        Color Values:\n
         * 机身 30,144,255
         * 机翼 131,206,250
        '''
        pygame.draw.rect(self.screen, self.planeColor_player, [
            self.player1_x+10, self.player1_y, 10, 31],border_radius=3)
        pygame.draw.rect(self.screen, self.wigColor_player, [
            self.player1_x-2, self.player1_y+15, 12, 10],border_top_left_radius=5)
        pygame.draw.rect(self.screen, self.wigColor_player, [
            self.player1_x+20, self.player1_y+15, 12, 10],border_top_right_radius=5)
        pygame.draw.rect(self.screen, self.wigColor_player, [
            self.player1_x+5, self.player1_y+31, 20, 3],border_radius=3)

    def enemyAircraft(self, index: int) -> None:
        '''
        @ index: The index of the enemy.\n
        This fuc draws the player1's plane.\n
        Color Values:\n
         * 机身 192,192,192
         *  机翼 178,34,34
        '''

        pygame.draw.rect(self.screen, self.planeColor_enemy, [
            self.enemy_x_list[index]+3, self.enemy_y_list[index], 22, 3],border_radius=3)
        pygame.draw.rect(self.screen, self.planeColor_enemy, [
            self.enemy_x_list[index]+10, self.enemy_y_list[index], 10, 35],border_radius=3)
        pygame.draw.rect(self.screen, self.wigColor_enemy, [
            self.enemy_x_list[index]-2, self.enemy_y_list[index]+10, 12, 10])
        pygame.draw.rect(self.screen, self.wigColor_enemy, [
            self.enemy_x_list[index]+20, self.enemy_y_list[index]+10, 12, 10])
        pygame.draw.rect(self.screen, [0, 0, 0], [
            self.enemy_x_list[index]+3, self.enemy_y_list[index]+2, 22, 3],border_radius=3)
        try:
            self.enemyLifeList[index]
        except:
            return 0
        pygame.draw.rect(self.screen, [255, 0, 0], [
            self.enemy_x_list[index]+2, self.enemy_y_list[index]-self.movAmount-3, int(self.enemyLifeList[index]/4), 3],border_radius=3)

    def player2Aircraft(self,) -> None:
        '''
        This fuc draws the player2's plane.\n
        Color Values:\n
         * 机身 30,144,255
         * 机翼 131,206,250
        '''
        pygame.draw.rect(self.screen, self.planeColor_player, [
            self.player2_x+10, self.player2_y, 10, 31],border_radius=3)
        pygame.draw.rect(self.screen, self.wigColor_player, [
            self.player2_x-2, self.player2_y+15, 12, 10],border_radius=3)
        pygame.draw.rect(self.screen, self.wigColor_player, [
            self.player2_x+20, self.player2_y+15, 12, 10],border_radius=3)
        pygame.draw.rect(self.screen, self.wigColor_player, [
            self.player2_x+5, self.player2_y+31, 20, 3],border_radius=3)
        pygame.draw.rect(self.screen, [255, 0, 0], [
            self.player2_x, self.player2_y+39, int(self.player2_life/3), 2],border_radius=3)

    def medicine(self, index: int) -> None:
        '''
        @ index: The index of the medicine in the list.\n
        This fuc draws the medicines.\n
        '''
        pygame.draw.rect(self.screen, [255, 255, 255], [
            self.medicineX[index], self.medicineY[index], 20, 20],border_radius=5)
        pygame.draw.rect(self.screen, [255, 0, 0], [
            self.medicineX[index]+2, self.medicineY[index]+8, 16, 4],border_radius=3)
        pygame.draw.rect(self.screen, [255, 0, 0], [
            self.medicineX[index]+8, self.medicineY[index]+3, 4, 16],border_radius=3)

    def switchAnimation(self,) -> None:
        '''
        This fuction achieved a simple animate effect of switching the screen.
        '''
        fillPos = 0
        while fillPos <= 500:
            time.sleep(0.00005)
            pygame.draw.rect(self.screen, [0, 0, 0], [
                0, fillPos, 500, 5])
            fillPos += 5
            pygame.display.update()

    def drawString(self, index: int) -> None:
        '''
        @ index: The index of the string in the list\n
        The string has many modes such as:\n
         * normal
         * artillery
         * Xray
         * missile
        '''
        # decide which mode to show
        if self.mode == 'normal':
            width = 3
        elif self.mode == 'artillery':
            width = 4
        elif self.mode == 'Xrate':
            width = 5
        elif self.mode == 'missile':
            width = 6
        # draw the string.
        try:
            pygame.draw.rect(self.screen, self.AttackColor, [
                self.attackStringX[index], self.attackStringY[index]+10, width, 10],border_radius=3)
        except:
            pass

    def bloodDock(self, player: int) -> None:
        '''
        @ player: The player you want to print.\n
        This fucton draws the blood dock on the blured background(You can disable it in the settings).
        '''
        text = self.font.render(
            f"{self.player1_life}", True, 'white')
        self.screen.blit(text, (self.screenWidth - 270, 60))
        text = self.font.render(
            f"{self.score}", True, "white")
        self.screen.blit(text, (30, 60))
        pygame.draw.rect(self.screen, self.bloodColor, [
            280, 62, self.player1_life, 20],border_radius=5)
        pygame.draw.rect(self.screen, self.bulletIconColor, [
            460, 62, 10, 20],border_radius=5)
        text = self.font.render(
            f"{self.player1_bullet}", True, "white")
        self.screen.blit(text, (410, 60))
        text = self.font.render(
            f"{self.mode}", True, "white")
        self.screen.blit(text, (70, 58))
