import tkinter
import os


class restorer():
    def __init__(master, dirPath: str) -> None:
        '''
        @ master: The master class
        @ dirPath: The dir you want to switch to\n 
        This fuc init the restorer class
        '''
        master.fileList = os.listdir(dirPath)
        master.mode = "restore"

    def get(master, index: int) -> str:
        return master.fileList[index]

    def okCallback(self) -> None:
        '''
        This fuc is used to deal with the ok ebent
        '''
        self.fileIndex = self.entry.get()

    def getFileList(dir: str) -> str:
        """
        @ dir:The dir you want to know about\n 
        This fuction get all the files in ```dir``` and returns them in a string
        """
        txt = ''
        index = 0
        for m in os.listdir("./save"):
            index += 1
            txt += f"{index}:{m}\n"
        return txt
    def askChapter(self)->bool:
        '''
        This fuc is used to ask if the player want to start a new game or restore the backups
        '''
        master = tkinter.Tk()
        window = tkinter.Frame(master, bg="#f1f3f5")
        tkinter.Label(window, text="Which Chapter do you want?",
                      bg="#f1f3f5").grid(column=1, row=1)
        txt = restorer.getFileList("./chapter")
        tkinter.Label(window, text=txt, bg="#f1f3f5").grid(column=1, row=2)
        self.entry = tkinter.Entry(window, bg="#ffffff")
        self.entry.grid(column=1, row=3)
        okButton = tkinter.Button(window, text="OK", relief='flat',
                                  command=lambda: restorer.okCallback(self), bg="#ffffff")
        editButton = tkinter.Button(window, text='Edit', relief='flat')
        editButton.grid(column=2, row=4)
        okButton.grid(column=1, row=4)
        window.grid(column=1, row=1)
        tkinter.mainloop()
        try:
            return int(self.fileIndex)
        except:
            return None

    def askRestores(self) -> bool:
        '''
        This fuc is used to ask if the player want to start a new game or restore the backups
        '''
        master = tkinter.Tk()
        window = tkinter.Frame(master, bg="#f1f3f5")
        tkinter.Label(window, text="Do You Want To Restore The Backups?(End this window after you have end entering)",
                      bg="#f1f3f5").grid(column=1, row=1)
        txt = restorer.getFileList("./save")
        tkinter.Label(window, text=txt, bg="#f1f3f5").grid(column=1, row=2)
        self.entry = tkinter.Entry(window, bg="#ffffff")
        self.entry.grid(column=1, row=3)
        okButton = tkinter.Button(window, text="OK", relief='flat',
                                  command=lambda: restorer.okCallback(self), bg="#ffffff")
        okButton.grid(column=1, row=4)
        window.grid(column=1, row=1)
        tkinter.mainloop()
        try:
            return int(self.fileIndex)
        except:
            return None
