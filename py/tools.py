import os
import json
import time


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

        def __init__(self, filePath) -> None:
            self.dictionary = json.loads(tools.file.readFile(filePath, 0, 100))

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

        def writeFile(name: str, strings: str = "") -> None:
            '''
            @ name: The Name of the file\n
            @ strings: The string you want to write\n
            This fuction is used to write a file.
            '''
            # open the file you want to write in.
            with open(name, mode='a+') as file:
                # write in
                file.write(strings)

        def config(settingName: str, filePath: str = './data/setting.json') -> str:
            '''
            @ settingName: The setting you want to look up\n
            This fuc is used to read and return a json object.
            '''
            dictionary = json.loads(tools.file.readFile(filePath, 0, 100))
            return dictionary[settingName]

        def write(settingName: str, self, input) -> dict:

            self.dictionary[settingName] = input

        def delete(filePath: str) -> bool:
            '''
            @ fileName: The file you want to delete\n
            This fuction deletes the file you want to delete
            '''
            try:
                os.remove(filePath)
                return True
            except:
                return False

        def writeInJson(input: json):
            '''
            @ input: The json you want to write in
            This fuction is used to save the configs
            '''
            with open(f"./save/{int(time.time())}.json", mode="a+")as f:
                writeinStr = ''
                for m in str(input):
                    if m == "'":
                        m = "\""
                    writeinStr += m
                f.write(writeinStr)
