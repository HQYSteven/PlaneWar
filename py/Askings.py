
import tkinter


class ask(object):
    def Yes(window, self):
        self.reply = "yes"
        quit()

    def No(window, self):
        self.reply = "no"
        quit()

    def SaveOrNot(self,s):
        '''
        This fuc Ask You if you want to Save the game
        '''
        window = tkinter.Tk()
        tkinter.Label(window, text="Do You Want To Save This Game?").grid(
            column=0, row=1)
        tkinter.Button(window, text="Yes!", command=lambda: ask.Yes(
            window, self)).grid(column=0, row=2)
        tkinter.Button(window, text="No Thanks!", command=lambda: ask.No(
            window, self)).grid(column=2, row=2)
        tkinter.mainloop()
