import pygame
from update import update
from ui import ui
from graphic import graphic_update
import time
from bind import bind
from egg import egg

'''
This is the main programme of the game
You can call it the kernel of the game.
'''
class programme():
    '''
    Main Programme
    created in 2022
    '''

    def print_screen(self, string: str = "", pos: list = (210, 260), color: str = 'black'):
        '''
        @ string: The str you want to print.\n
        @ pos: The pos you want to print at.\n
        @ color: The color the text will be.\n
        This fuction is used to print a line of string on pygame screen.
        '''
        self.screen.blit(self.font.render(
            string, True, color), pos)

    def __init__(self):
        self.init = True
    def quitPage(self):
        '''
        This page will show the conclusion page of the game.
        '''
        ui.switchAnimation(self)
    def topbar(self, string: str = ""):
        pygame.draw.rect(self.screen, [255, 0, 0], [0, 0, 500, 50])
        programme.print_screen(
            self, string, pos=(230, 10), color='white')
        programme.print_screen(self, "<", pos=(10, 10), color='white')

    def bind_topbar(self,x,y,event):
        '''
        detect if the button has benn pressed
        '''
        if x > 10 and x < 50 and y > 10 and y < 40 and event.type == pygame.MOUSEBUTTONUP:
            ui.switchAnimation(self,)
            return True
        return False
    def graphics(self, a: str,  player2: bool = False) -> None:
        '''
        @ player2: Decide to draw the player2 or not.
        A fuction used to control the graghic userface\n
        It first use the switchAnimation Programme\n
        Then start the main loop\n
        Decide if it is nessary to blur the dock( which will make the loop slower )   \n
        Read the message list and react.\n
        Finally,draw all the objects\n
        '''
        # initlize the main screen.
        ui.switchAnimation(self,)
        # init the index
        index = 0
        while self.runningP:
            # decide if there is need to make the loop slower
            if not self.blur:
                time.sleep(0.05)
            self.player2 = player2
            # read the message list
            for message in self.message:
                if message == 'egg':
                    egg.egg_graphic(self)
                # refresh the index
                index += 1
            # initlize the whole screen
            self.screen.fill([0, 0, 0])
            # decide if there is need to draw player2's plane
            if self.player2:
                ui.player2Aircraft(self,)
            # draw objects
            graphic_update.string(self,)
            # draw enemies' strings
            graphic_update.ememyString(self,)
            if not self.runningP:
                return 0
            # draw medicine
            graphic_update.medicine(self,)
            # update stars
            update.updateStars(self,)
            # draw stones
            graphic_update.stone(self,)
            # draw enemies
            graphic_update.enemy(self,)
            # decide if there is need to blur the backgrounds
            if self.blur:
                graphic_update.blurdock(self,)
            if player2:
                ui.bloodDock(self, 0)
            # draw the blood dock
            ui.bloodDock(self, 1)
            # draw the player1's plane
            ui.aircraft_1(self,)
            programme.topbar(self,"Plane War")
            # update the whole screen
            pygame.display.update()

    def main(self, run: bool, player2: bool = False) -> None:
        """
        plane War kernel\n
        @ run: Decide the program will run or not
        @ player2: Tell the kernel if there is player2 or not
        """
        # record the loop times
        times = 0
        self.player2 = player2
        # start graghic service
        self.runningP = True
        # start the main loop
        while self.runningP:
            # record the screen width
            self.screenWidth = pygame.display.get_window_size()[0]
            self.screenHeight = pygame.display.get_window_size()[1]
            # decide if there is need to quit
            if not self.running:
                pygame.quit()
                break
            # decide the player2's coordinates
            if self.player2:
                self.player2_y = self.screenHeight - 45
            self.player1_y = self.screenHeight - 90
            
            # 每次循环停止1/fps秒，用于减轻CPU压力
            time.sleep(1/self.fps)
            times += 1
            # get the events
            for event in pygame.event.get():
                try:
                    x,y = pygame.mouse.get_pos()
                    if x > 10 and x < 50 and y > 10 and y < 40 and event.type == pygame.MOUSEBUTTONUP:
                        return True
                except:
                    pass
                # graghic events
                if event.type == pygame.QUIT:
                    self.running = False
                # 监测是否键盘事件发生
                if event.type == pygame.KEYDOWN:
                    bind.keyEvent(self, event)
            # bind the keyboard events
            times = bind.watch(self, times) 
            if type(times) != int:
                return times
            update.update(self)

