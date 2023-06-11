import pygame
from blur import blur
from ui import ui 

class graphic_update(object):
    def string(self,):
        index = 0
        while index >= 0 and index < len(self.attackStringX):
            ui.drawString(self, index)
            index += 1

    def ememyString(self,):
        index = 0
        while index < len(self.otherAttack_x):
            pygame.draw.rect(self.screen, [0, 255, 0], [
                self.otherAttack_x[index], self.otherAttack_y[index], 3, 10])
            index += 1

    def medicine(self,):
        index = 0
        while index >= 0 and index < len(self.medicineX):
            ui.medicine(self, index)
            index += 1

    def stone(self,):
        index_stone = 0
        while index_stone < len(self.stoneXList) and index_stone >= 0:
            pygame.draw.rect(self.screen, [255, 255, 255], [
                self.stoneXList[index_stone], self.stoneYList[index_stone], 20, 20])
            index_stone += 1

    def enemy(self,):
        index = 0
        while index >= 0 and index < len(self.enemy_x_list):
            ui.enemyAircraft(self, index)
            index += 1

    def blurdock(self,):
        blurl = []
        x = 10
        y = 10
        for y in range(10, 50):
            for x in range(20, 480):
                rgba = pygame.Surface.get_at(self.screen, (x, y))
                blurl.append(rgba)

        i = blur(blurl, 460)
        blur.kernel(i, add=10)
        blur.blender(i, self.screen, 480, 20, 10)
        '''x = 20
            y = 10
            for l in after:
                pygame.draw.rect(self.screen,l,[x,y,1,1])
                if x == 480:
                    y +=1
                    x = 20
                x +=1'''
