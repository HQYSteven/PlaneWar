from tools import tools


class save(object):
    '''
    A class used to save all the modules together.
    '''
    def save(master):
        '''
        @ self,master: The class you want to save
        A fuc used to save all the modules togrther
        '''

        self = tools.file("./data/template.json")
        save.save_planeAmount(self, master,)
        save.save_players(self, master,)
        save.save_attackStrings(self, master,)
        save.save_enemy(self, master,)
        save.save_medicine(self, master,)
        save.save_bullet(self, master,)
        save.saveStone(self, master,)
        tools.file.writeInJson(str(self.dictionary))

    def save_medicine(self, master,):
        '''
        @ self,master: The class you want to save 
        A fuc used to save \n
         * medicine Amount\n
         * medicine lists\n
         * the length of every step you went. 
        '''
        tools.file.write("stringMov", self, master.stringMov)
        tools.file.write("medicineAmount", self, master.medicineAmount)
        tools.file.write("medicineX", self, master.medicineX)
        tools.file.write("medicineY", self, master.medicineY)

    def save_attackStrings(self, master,):
        '''
        @ self,master: The class you want to save 
        A fuc used to save \n
         * players' attack strings' Amount\n
         * players' attack strings' lists\n
         * the color of players' attack strings'. 
        '''
        tools.file.write("attackStringX", self, master.attackStringX)
        tools.file.write("attackStringY", self, master.attackStringY)

    def save_bullet(self, master,):
        '''
        @ self,master: The class you want to save 
        A fuc used to save \n
         * players' bullets' Amount\n
         * players' bullets' lists\n
         * the color of players' bullet'. \n
         * The color of every wapon modes\n
         * The hurt of every kind of wapons\n
         * The speed of the bullets
        '''
        tools.file.write("player1_bullet", self, master.player1_bullet)
        tools.file.write("player2_bullet", self, master.player2_bullet)
        tools.file.write("stringMov", self, master.stringMov)

    def save_enemy(self, master,):
        '''
        @ self,master: The class you want to save 
        A fuc used to save \n
         * enemies' Amount\n
         * enemies' bullets' lists\n
         * enemies' list. \n
         * enemies' lives\n
        '''
        tools.file.write("otherAttack_x", self, master.otherAttack_x)
        tools.file.write("otherAttack_y", self, master.otherAttack_y)
        tools.file.write("enemy_x_list", self, master.enemy_x_list)
        tools.file.write("enemy_y_list", self, master.enemy_y_list)
        tools.file.write("enemyLifeList", self, master.enemyLifeList)

    def save_planeAmount(self, master,):
        '''
        @ self,master: The class you want to save 
        A fuc used to save\n
         * players' wigs' color\n
         * players' plane's body's color\n
         * players are moving or not\n
         * The amount of the players
         * The speed of the players
        '''
        tools.file.write("planeAmount", self, master.planeAmount)

    def saveStone(self, master,):
        '''
        @ self,master: The class you want to save 
        A fuc used to save\n
         * stone x\n
         * stone y\n
        '''
        tools.file.write("stoneXList", self, master.stoneXList)
        tools.file.write("stoneYList", self, master.stoneYList)

    def save_players(self, master,):
        '''
        @ self,master: The class you want to save 
        A fuc used to save\n
         * The color of the fire\n
         * The players' life\n
         * The players' x\n
         * The players' y\n
         * The fuel of the players\n
         * The list of the strings that players has sent out\n
         * The score of the players
        '''
        tools.file.write("player1_life", self, master.player1_life)
        tools.file.write("player2_life", self, master.player2_life)
        tools.file.write("player1_bullet", self, master.player1_bullet)
        tools.file.write("player2_bullet", self, master.player2_bullet)
        tools.file.write("score", self, master.score)
        tools.file.write("attackXList", self, master.attackXList)
        tools.file.write("attackYList", self, master.attackYList)
        tools.file.write("player2_x", self, master.player2_x)
        tools.file.write("player1_x", self, master.player1_x)


if __name__ == "__main__":
    from init import init

    class test():
        def __inti__():
            pass
    self = test()
    init.init(self)
    save.save(self)
