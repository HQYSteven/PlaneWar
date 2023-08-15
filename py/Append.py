import random
'''
 * You may think you know what the following code does.
 * But you don't. Trust me.
 * Fiddle with it, and you'll spend many a sleepless
 * night cursing the moment you thought you'd be clever
 * enough to "optimize" the code below.
 * Now close this file and go play with something else.
 *
 * 你可能会认为你读得懂以下的代码。但是你不会懂的，相信我吧。
 * 要是你尝试玩弄这段代码的话，你将会在无尽的通宵中不断地咒骂自己为什么会认为自己聪明到可以优化这段代码。
 * 现在请关闭这个文件去玩点别的吧。
 *
'''



class Append(object):
    '''
    This class contains methods used to append\n
    enemies,medicines,stones,strings.
    '''

    def appendMedicine(self,) -> None:
        '''
        This fuction appends medicines that can cure players
        '''
        self.medicineX.append(random.randint(0, 480))
        self.medicineY.append(0)
        self.medicineAmount -= 1

    def appendEnemy(self,) -> None:
        '''
        This fuction appends enemies
        '''
        coordinate = random.randint(0, 480)
        self.enemy_x_list.append(coordinate)
        self.enemy_y_list.append(0)
        self.otherAttack_x.append(coordinate+13)
        self.otherAttack_y.append(10)
        self.enemyLifeList.append(100)
        self.planeAmount -= 1

    def appendAttack(self, player=0) -> None:
        '''
        This fuction appends strings that can hurt players
        '''
        
        self.attackStringX.append(self.playerxList[player]+13)
        self.attackStringY.append(self.screenHeight - 100)
        

#################################################################
