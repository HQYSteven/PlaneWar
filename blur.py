

class blur(object):
    def __init__(self, blurList: list, width: int) -> None:
        self.blurList = blurList
        self.width = width

    def blur(self) -> list:
        """
        @ self:Class blur
        """
        index = 4
        x = 0
        y = 0
        afterList = self.blurList
        length = len(self.blurList)-2
        while index <= length:
            if x == self.width:
                y += 1
                x = 0
            rAdd = 0
            gAdd = 0
            bAdd = 0
            if y > 2:
                index_min = index - self.width
                if index + self.width < length:
                    index_add = index + self.width
                else:
                    index_add = index_min
                rAdd = self.blurList[index_min+1][0] + \
                    self.blurList[index_min-1][0] + self.blurList[index_min][0] + \
                    self.blurList[index_add+1][0] + \
                    self.blurList[index_add-1][0] + self.blurList[index_add][0]
                gAdd = self.blurList[index_min-2][1] + \
                    self.blurList[index_min-1][1] + self.blurList[index_min][1] + \
                    self.blurList[index_add+1][1] + \
                    self.blurList[index_add-1][1] + self.blurList[index_add][1]
                bAdd = self.blurList[index_min-2][2] + \
                    self.blurList[index_min-1][2] + self.blurList[index_min][2] + \
                    self.blurList[index_add+1][2] + \
                    self.blurList[index_add-1][2] + self.blurList[index_add][2]
                r = (self.blurList[index+1][0] + self.blurList[index-1]
                     [0] + self.blurList[index][0]+rAdd) // 9
                g = (self.blurList[index+1][1] + self.blurList[index-1]
                     [1] + self.blurList[index][1]+gAdd) // 9
                b = (self.blurList[index+1][2] + self.blurList[index-1]
                     [2] + self.blurList[index][2]+bAdd) // 9
                afterList[index] = [r, g, b]
                index += 1
                x += 1
            else:
                r = (self.blurList[index+1][0] + self.blurList[index-1]
                     [0] + self.blurList[index][0]+rAdd) // 3
                g = (self.blurList[index+1][1] + self.blurList[index-1]
                     [1] + self.blurList[index][1]+gAdd) // 3
                b = (self.blurList[index+1][2] + self.blurList[index-1]
                     [2] + self.blurList[index][2]+bAdd) // 3
                afterList[index][0],afterList[index][1],afterList[index][2] = r,g,b
                #print(afterList)
                index += 1
                x += 1
        return afterList


if __name__ == '__main__':
    import random

    import pygame
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    l = []
    for i in range(25000):
        l.append([random.randint(0, 255), 100, 100])

    self = blur(l, 500)

    window.fill([255, 255, 255])
    index = 0
    y = 250
    for list in self.blurList:
        pygame.draw.rect(window, list, [index, y, 1, 1])
        if index == 500:
            index = 0
            y += 1
            continue
        index += 1
    l = blur.blur(self)
    l = blur.blur(self)
    index = 0
    y = 0
    for list in l:
        pygame.draw.rect(window, list, [index, y, 1, 1])
        if index == 500:
            index = 0
            y += 1
            continue
        index += 1
    pygame.display.update()
    pygame.Surface.get_at(window, (10, 10))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
