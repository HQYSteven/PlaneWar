import os
import tkinter
import json
import shutil
from tkinter import colorchooser
from tkinter import filedialog
'''
This is the main file of the theme editor
'''


class editor():
    '''
    This fuc is the main programme
    '''
    def readFile(name: str, startRow: int = 0, endRow: int = 1) -> str:
        '''
        @ name: The Name of the file\n
        @ startRow: The row you want to start\n
        @ endRow: The row you want to stop\n
        This fuction is used to read a file.
        '''
        result = ''
        # open the file user want to read.
        with open(name, mode='r') as file:
            fileList = []
            fileList = file.readlines()
            if endRow > len(fileList):
                endRow = len(fileList)
            for index in range(0, endRow):
                if index >= startRow:
                    result += fileList[index]
                    continue
        return result

    def __init__(self) -> None:
        '''
        The fuc used to init the programme
        '''
        settings = json.loads(editor.readFile(
            "./data/setting.json", 0, 100))
        themePath = settings["themePath"]
        self.uiSettings = json.loads(editor.readFile(
            f"{themePath}/ui.json", 0, 100))
        settings = json.loads(editor.readFile(
            "./data/setting.json", 0, 100))
        sourcePath = settings["themePath"]
        self.sourceSettings = json.loads(editor.readFile(
            f"{sourcePath}/sources.json", 0, 100))

    def color_callback() -> str:
        '''
        This fuction returns a color value
        '''
        colorValue = colorchooser.askcolor(title="Choose color")[1]
        return colorValue if colorValue != None else [0, 0, 0]

    def fontSize_Callback(self):
        self.sourceSettings['fontSize'] = self.ent.get()

    def callback(self, settingName) -> None:
        ''''
        The Call back of button_playerWig
        '''
        if settingName in self.uiSettings:
            self.uiSettings[settingName] = editor.color_callback()
        if settingName in self.sourceSettings:
            if settingName != 'fontSize':
                self.sourceSettings[settingName] = filedialog.askopenfile()
            else:
                window = tkinter.Tk()
                window.title = 'FontSize'
                self.ent = tkinter.Entry(window, relief="flat")
                self.ent.pack(fill="x")
                tkinter.Button(window, relief="flat", text="OK",
                               command=lambda: editor.fontSize_Callback(self)).pack(fill="x")
                tkinter.mainloop()

    def saveAs(self):
        """
        This fuc is used to store the configs 
        """
        os.makedirs(self.themeName)
        shutil.copytree("./"+self.themeName, './themes')
        with open("ui.json", mode='a+') as ui:
            uiJSon = json.dumps(self.uiSettings)
            ui.write(uiJSon)
        with open("sources.json") as sources:
            sourceJson = json.dumps(self.sourceSettings)
            sources.write(sourceJson)
        shutil.copyfile("ui.json",f"./themes/{self.themeName}")
        shutil.copyfile("sources.json",f"./themes/{self.themeName}")
        for path in self.sourceSettings:
            shutil.copyfile(path,f"./themes/{self.themeName}")
        quit()
    def set_themeName(self):
        self.themeName = self.entry.get()

    def main(self):
        '''
        main Programme
        '''

        self.themeName = "New Theme"
        window = tkinter.Tk()
        window.title("Theme Editor")
        tkinter.Label(window, text="--=Plane War Theme Editor=--",
                      height=3,).pack(fill='x')
        listFrame = tkinter.Frame()
        listBox = tkinter.Listbox(listFrame, relief="flat", height=18, width=100, foreground="#aaaaaa",
                                  highlightcolor="#0A59f7", highlightbackground="#f1f3f5", selectbackground="#0A59f7", selectforeground="#ffffff")
        for key in self.uiSettings:
            listBox.insert("end", key,)
        for key in self.sourceSettings:
            listBox.insert("end", key,)
        listBox.pack(fill='both')
        tkinter.Button(listFrame, text='Change', relief='flat', highlightcolor="#0A59F7",
                       command=lambda: editor.callback(self, listBox.get("active"))).pack(fill="x")
        tkinter.Button(listFrame, text='Output Into File', relief='flat',
                       command=lambda: editor.saveAs(self)).pack(fill="x")
        tkinter.Label(window, text="Theme Name?").pack()
        self.entry = tkinter.Entry(window, bg="#ffffff").pack()
        tkinter.Button(window, relief="flat", border=0, text="").pack()
        listFrame.pack(fill='x')
        tkinter.mainloop()


if __name__ == "__main__":
    self = editor()
    editor.main(self)
