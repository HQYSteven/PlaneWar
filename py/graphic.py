import pygame
from blur import blur
from ui import ui 
import time

class graphic_update(object):
    def shortcut_graghic(self):
            
            '''l = blur.get(self.screen,150,350,150,350)
            s = blur(l,200)
            blur.kernel(s,10)
            blur.blender(s,self.screen,200,150,150)'''
            blurl = blur.get(self.screen,40,460,150,350)
            i = blur(blurl, 420)
            blur.kernel(i, add=10)
            blur.blender(i, self.screen, 420, 40, 150)
            pygame.display.update()
            while True:
                time.sleep(0.05)
                for m in self.message:
                    if m == 'esc':
                        return 0
    def string(self,):
        '''

        graphical update: string player sent\n
        read and print the strings\n
        created in 2023
        '''
        index = 0
        while index >= 0 and index < len(self.attackStringX):
            ui.drawString(self, index)
            index += 1

    def ememyString(self,):
        '''
        graphical update: string enemies sent\n
        read and print enemies' strings\n
        created in 2023
        '''
        index = 0
        while index < len(self.otherAttack_x):
            try:
                self.otherAttack_y[index]
            except:
                return 
            pygame.draw.rect(self.screen, [182,198,67], [
                self.otherAttack_x[index], self.otherAttack_y[index], 3, 10])
            index += 1

    def medicine(self,):
        '''
        graphical update: medicine\n
        ead and draw medicines\n
        created in 2023
        '''
        index = 0
        while index >= 0 and index < len(self.medicineX):
            ui.medicine(self, index)
            index += 1

    def stone(self,):
        '''
        graphical update: stone\n
        Read and draw stones\n
        created in 2023
        Module:pygame
        Author:HQY
        '''
        index_stone = 0
        while index_stone < len(self.stoneXList) and index_stone >= 0:
            pygame.draw.rect(self.screen, [255, 255, 255], [
                self.stoneXList[index_stone], self.stoneYList[index_stone], 20, 20])
            index_stone += 1

    def enemy(self,):
        '''
        graphical update: enemies\n
        read and draw enemies\n
        created in 2023
        '''
        index = 0
        while index >= 0 and index < len(self.enemy_x_list):
            ui.enemyAircraft(self, index)
            index += 1

    def blurdock(self,):
        """
        A fuction used to blur the backround of dock\n
        read the pixels and draw it
        create in April 2023
        """
        blurl = blur.get(self.screen,20,480,50,90)
        i = blur(blurl, 460)
        blur.kernel(i, add=-10)
        blur.blender(i, self.screen, 460, 20, 50)
