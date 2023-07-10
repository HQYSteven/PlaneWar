import json
from typing import Any
class tools(object):
    '''
    This is a tools class that contains some tools
    Like file modules
    '''
    class file(object):
        '''
        This class is used to process I/O options
        created in 2023
        '''
        def __init__(self,filePath) -> None:
            self.dict = json.loads(tools.file.readFile(filePath,0,100))
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
        def writeFile(name: str, strings: str = "")->None:
            '''
            @ name: The Name of the file\n
            @ strings: The string you want to write\n
            This fuction is used to write a file.
            '''
            # open the file you want to write in.
            with open(name,mode = 'a+') as file:
                # write in 
                file.write(strings)
        def config(settingName):
            '''
            @ settingName: The setting you want to look up\n
            This fuc is used to read and return a json object.
            '''
            dictionary = json.loads(tools.file.readFile('setting.json',0,100))
            return dictionary[settingName]