import pygame
from update import update
from ui import ui
from graphic import graphic_update
import time
from bind import bind
from egg import egg
import _thread
import _thread


class programme():
    def __init__(self):
        self.init = True

    def graphics(self, a,  player2=False):
        ui.switchAnimation(self,)
        index = 0
        while self.running:

            if not self.blur:
                time.sleep(0.05)
            self.player2 = player2
            for message in self.message:
                if self.planeAmount == 0:
                    egg.egg_graphic(self)
                if message == 'switch':
                    ui.switchAnimation(self,)
                    del self.message[index]
                    continue

                index += 1
            self.screen.fill([0, 0, 0])

            if self.player2:
                ui.player2Aircraft(self,)
            graphic_update.string(self,)
            graphic_update.ememyString(self,)
            graphic_update.medicine(self,)
            update.updateStars(self,)

            graphic_update.stone(self,)
            graphic_update.enemy(self,)
            if self.blur:
                graphic_update.blurdock(self,)
            if player2:
                ui.bloodDock(self, 0)
            ui.bloodDock(self, 1)
            ui.aircraft_1(self,)
            pygame.display.update()

    def main(self, run, player2=False):
        """
        plane War
        """

        times = 0
        self.running = run
        _thread.start_new_thread(
            self.graphics, (self, self.player2))
        while self.running:

            self.screenWidth = pygame.display.get_window_size()[0]
            self.screenHeight = pygame.display.get_window_size()[1]

            if not self.playing:
                pygame.quit()
                break

            if self.player2:
                self.player2_y = self.screenHeight - 45
            self.player1_y = self.screenHeight - 90
            ui.aircraft_1(self,)
            # 当没有飞机时，退出
            times = bind.watch(self, times)
            # 每次循环停止0.015秒，25FPS/s,用于减轻CPU压力
            time.sleep(1/self.fps)
            times += 1
            # 事件识别
            for event in pygame.event.get():
                # 退出监测
                if event.type == pygame.QUIT:
                    self.running = False
                # 监测是否键盘事件发生
                if event.type == pygame.KEYDOWN:
                    bind.keyEvent(self, event)
            update.update(self)


if __name__ == "__main__":
    from entrance import entrance
    from init import init
    self = init.init(programme())
    output = entrance.entrance(self)
    try:
        programme.main(self, output[0], output[1])
    except SyntaxError:
        print(SyntaxError)
    else:
        print("Game Finished")
