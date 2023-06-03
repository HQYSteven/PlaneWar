

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
        length = len(self.blurList)-2
        while index <= length:
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
            if index + self.width < length:
                    index_add = index + self.width
            else:
                    index_add = index_min
            if y > 2:
                
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
                r = (self.blurList[before][0] + self.blurList[after]
                     [0] + self.blurList[index][0]+rAdd) // 9
                g = (self.blurList[before][1] + self.blurList[after]
                     [1] + self.blurList[index][1]+gAdd) // 9
                b = (self.blurList[before][2] + self.blurList[after]
                     [2] + self.blurList[index][2]+bAdd) // 9
                self.blurList[before_add] = [r,g,b]
                self.blurList[before_min] = [r,g,b]
                self.blurList[after_min] = [r,g,b]
                self.blurList[after_add] = [r,g,b,]
                self.blurList[index_add] = [r,g,b]
                self.blurList[index_min] = [r,g,b]
                self.blurList[before] = [r,g,b]
                self.blurList[after] = [r,g,b]
                self.blurList[index] =[r,g,b]
                index += 1
                x += 1
            else:
                r = (self.blurList[index-2][0] + self.blurList[index-1]
                     [0] + self.blurList[index][0]+rAdd) // 3
                g = (self.blurList[index-2][1] + self.blurList[index-1]
                     [1] + self.blurList[index][1]+gAdd) // 3
                b = (self.blurList[index-2][2] + self.blurList[index-1]
                     [2] + self.blurList[index][2]+bAdd) // 3
                index += 1
                x += 1
            if length >= self.width and length < length - self.width:
                before_min += 1 
                after_min += 1
                before_add += 1
                after_add += 1
                before += 1
                after += 1
                index_add +=1
                index_min +=1
        return self.blurList


if __name__ == '__main__':
    import random

    import pygame
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    l = []
    for i in range(45000):
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
