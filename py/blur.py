
import pygame
'''
This file contains the blur module of the game
Such as kernel and the blender of it.
'''


class blur(object):
    '''
    This class is used to blur pixels by calculate the average.
    '''
    def __init__(self, blurList: list, width: int) -> None:
        """
        @ blurList The list you want to blur\n
        @ width The screen width
        """
        self.blurList = blurList
        self.width = width

    def kernel(self, add=0) -> list:
        """
        @ add: It judges the theme is light or dark\n
        This is the kernel of the blur effect.\n
        It receives a list of rgba lists and calculate the average of every nine lists,save it and return.
        """
        index = 4
        x = 0
        y = 0
        self.length = len(self.blurList)-2
        while index <= self.length:
            if x == self.width:
                y += 1
                x = 0
            rAdd = 0
            gAdd = 0
            bAdd = 0
            index_min = index - self.width
            before_min = 1
            after_min = 0
            before_add = 1
            after_add = 0
            before = 1
            after = 0
            if index + self.width < self.length:
                index_add = index + self.width
            else:
                index_add = index_min
            if y > 2:
                # calculate the average when the column is more than 2
                rAdd = self.blurList[after_min][0] + \
                    self.blurList[before_min][0] + self.blurList[index_min][0] + \
                    self.blurList[after_add][0] + \
                    self.blurList[before_add][0] + self.blurList[index_add][0]
                gAdd = self.blurList[after_min][1] + \
                    self.blurList[before_min][1] + self.blurList[index_min][1] + \
                    self.blurList[after_add][1] + \
                    self.blurList[before_add][1] + self.blurList[index_add][1]
                bAdd = self.blurList[after_min][2] + \
                    self.blurList[before_min][2] + self.blurList[index_min][2] + \
                    self.blurList[after_add][2] + \
                    self.blurList[before_add][2] + self.blurList[index_add][2]
                r = int((self.blurList[before][0] + self.blurList[after]
                         [0] + self.blurList[index][0]+rAdd) // 9)+add
                g = int((self.blurList[before][1] + self.blurList[after]
                         [1] + self.blurList[index][1]+gAdd)) // 9+add
                b = int((self.blurList[before][2] + self.blurList[after]
                         [2] + self.blurList[index][2]+bAdd) // 9) + add
                # judge of the color is too bright that it's not valid
                if r > 255:
                    r = 255
                if g > 255:
                    g = 255
                if b > 255:
                    b = 255
                if r < 0:
                    r = 0
                if g < 0:
                    g = 0
                if b < 0:
                    b = 0
                # save the lists
                self.blurList[before_add] = [r, g, b]
                self.blurList[before_min] = [r, g, b]
                self.blurList[after_min] = [r, g, b]
                self.blurList[after_add] = [r, g, b,]
                self.blurList[index_add] = [r, g, b]
                self.blurList[index_min] = [r, g, b]
                self.blurList[before] = [r, g, b]
                self.blurList[after] = [r, g, b]
                self.blurList[index] = [r, g, b]
                index += 1
                x += 1
            else:
                # calculate three nums' average
                r = int((self.blurList[index-2][0] + self.blurList[index-1]
                         [0] + self.blurList[index][0]+rAdd) // 3)+add
                g = int((self.blurList[index-2][1] + self.blurList[index-1]
                         [1] + self.blurList[index][1]+gAdd) // 3)+add
                b = int((self.blurList[index-2][2] + self.blurList[index-1]
                         [2] + self.blurList[index][2]+bAdd) // 3)+add
                # judge of the color is too bright that it's not valid
                if r > 255:
                    r = 255
                if g > 255:
                    g = 255
                if b > 255:
                    b = 255
                if r < 0:
                    r = 0
                if g < 0:
                    g = 0
                if b < 0:
                    b = 0
                index += 1
                x += 1
            if self.length >= self.width and self.length < self.length - self.width:
                # if the length reached the width limit.
                # Switch to the next column.
                before_min += 1
                after_min += 1
                before_add += 1
                after_add += 1
                before += 1
                after += 1
                index_add += 1
                index_min += 1
        return self.blurList

    def blender(self, surface, width=500, xstart=0, ystart=0):
        '''
        @ surface: The pygame window you have created\n
        @ width: The width of you pygame screen\n
        @ xstart: The coordinate(x) of the element\n
        @ ystart: The coordinate(y) of the element\n
        This is a fuction used to print all the elements on the screen.\n
        It reads the list you have blured and print it on the screen one by one\n
        When the length of the list reached the width limit. It switch to the next column\n
        Example:
        ```
            class test():
                pass
            self = test()
            width = 100
            bList = [[255,255,255],[56,34,55],[234,234,54],[67,98,143]]
            blured_Object = blur(self,bList,100)
        ```
        '''
        # init the nums
        x = xstart
        y = ystart
        width += xstart
        for rgba in self.blurList:
            # read the inputed list and print it.
            if x == width:
                # if the length reached the width limit
                # It switches to the next column
                y += 1
                x = xstart
            # print on the screen.
            pygame.draw.rect(surface, rgba, [x, y, 1, 1])
            # preparing to print the next pixel
            x += 1
    def get(surface,xstart:int,xend:int,ystart:int,yend:int)->list:
        '''
        @ surface: The pygame window you have created\n
        @ xstart: The coordinate(x) of the element\n
        @ ystart: The coordinate(y) of the element\n
        @ xend: The coordinate(x) you want to end getting\n
        @ yend: The coordinate(y) you want to stop getting\n
        This is a fuction used to get all the elements' pixels on the screen.\n
        It reads the list you are going to blur one by one\n
        When the length of the list reached the width limit. It switch to the next column\n
        '''
        blurlist = []
        for y in range(ystart, yend):
            for x in range(xstart, xend):
                rgba = pygame.Surface.get_at(surface, (x, y))
                blurlist.append(rgba)
        return blurlist
if __name__ == '__main__':
    '''
    test
    '''
    import random
    import pygame
    pygame.init()
    # make a list of 45000 rgba values
    window = pygame.display.set_mode((500, 500))
    l = []
    for i in range(250000):
        l.append([random.randint(0, 255), 100, 100])
    # preparing to blur
    self = blur(l, 500)
    # init the screen
    window.fill([255, 255, 255])
    # print the rgba list before blur
    index = 0
    y = 250
    for list in self.blurList:
        pygame.draw.rect(window, list, [index, y, 1, 1])
        if index == 500:
            index = 0
            y += 1
            continue
        index += 1
    # start to blur
    l = blur.kernel(self, )
    # print the blured elements on the window.
    blur.blender(self, window, 500)
    # update the screen
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
