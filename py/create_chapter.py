import tkinter
import json
from tkinter import ttk
from tools import tools


class chapter():
    def __init__(self) -> None:
        '''
        The init fuc
        '''
        self.dic = json.loads(tools.file.readFile(
            "./chapters/template.json", 0, 6))

    def create(self, name: str) -> None:
        '''
        This file is used to create the config file
        '''
        with open(f"./chapters/{name}.json", mode="a+") as file:
            file.write("")

    def add(self) -> None:
        '''
        This fuc is used to add a choice in the listbox
        '''
        self.listbox.insert("end", "New Elements")

    def config(self, index: int) -> None:
        '''
        The config Fuction 
        '''
        choice = self.combe.get()
        amount = int(self.sBox.get())
        if choice == '敌机':
            self.listbox.delete(index)
            self.listbox.insert(index, f"敌机*{amount}")
            for i in range(amount):
                self.dic["aircraftList"].append(1)
        if choice == "陨石":
            self.listbox.delete(index)
            self.listbox.insert(index, f"陨石*{amount}")
            for i in range(amount):
                self.dic["stoneList"].append(1)
        if choice == '射击':
            self.listbox.delete(index)
            self.listbox.insert(index, f"射击*{amount}")
            for i in range(amount):
                self.dic["stringList"].append(1)
        if choice == '医疗包':
            self.listbox.delete(index)
            self.listbox.insert(index, f"医疗包*{amount}")
            for i in range(amount):
                self.dic["medicineList"].append(1)
        if choice == "间隔":
            self.listbox.delete(index)
            self.listbox.insert(index, f"间隔*{amount}")
            for i in range(amount):
                self.dic["stringList"].append(0)
                self.dic["stoneList"].append(0)
                self.dic["aircraftList"].append(0)
                self.dic["medicineList"].append(0)

    def save(self) -> None:
        '''
        This fuc is used to save all the changes
        '''
        import time
        t = time.time()
        chapter.create(self, t)
        with open(f"{t}.json", mode='a+') as file:
            file.write(json.dumps(self.dic))

    def configBox(self, index: int) -> None:
        '''
        This fuc creates a window and asks you what you want to add to 
        '''
        newWindow = tkinter.Tk()
        newWindow.title = "Edit"
        tkinter.Label(
            newWindow, text="What Do You Want To Add And The Amount?").pack(fill="x")
        self.combe = ttk.Combobox(newWindow, values=("敌机", "陨石", "射击","医疗包", "间隔"))
        self.combe.pack(fill="x")
        self.sBox = tkinter.Spinbox(newWindow, relief="flat", from_=1, to=5)
        self.sBox.pack(fill="x")
        okbutton = tkinter.Button(
            newWindow, relief="flat", text="OK", command=lambda: chapter.config(self, index))
        okbutton.pack(fill="y")
        tkinter.mainloop()

    def ChangeBox(self) -> None:
        try:
            num = 0
            for num in range(self.listbox.size()):
                if self.listbox.select_includes(num):
                    break
            chapter.configBox(self, num)
        except:
            return -1

    def main(self) -> None:
        '''
        The main fuction
        '''
        self.screen = tkinter.Tk()
        self.screen.title("Chapter Editor")
        tkinter.Label(self.screen, text="关卡编辑器").pack()
        bar = tkinter.Scrollbar(self.screen, relief="flat")
        bar.pack(side="right", fill="y")
        self.listbox = tkinter.Listbox(
            self.screen, relief="flat", yscrollcommand=bar.set)
        self.listbox.pack(fill="y")
        bar.config(command=self.listbox.yview)
        button0 = tkinter.Button(
            self.screen, text="添加", relief="flat", command=lambda: chapter.add(self))
        button0.pack(fill="both")
        button1 = tkinter.Button(
            self.screen, text="更改", relief="flat", command=lambda: chapter.ChangeBox(self))
        button1.pack(fill="both")
        button2 = tkinter.Button(self.screen, text="导入", relief="flat")
        button2.pack(fill="both")
        button3 = tkinter.Button(
            self.screen, relief="flat", text="保存", command=lambda: chapter.save(self))
        button3.pack(fill="both")
        tkinter.mainloop()


if __name__ == "__main__":
    self = chapter()
    chapter.main(self)
