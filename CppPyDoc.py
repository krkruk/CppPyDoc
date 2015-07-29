'''
Created on Jul 29, 2015

@author: krzysztof
'''
import DocEngine
import SaveAsCSV
import UserInputParse
if __name__ == '__main__':
    parse = UserInputParse.UserInputParse()
    source, dest, *cmd = parse.getCmd()
    
    de = DocEngine.DocEngine(source[0])
    saveCSV = SaveAsCSV.SaveAsCSVEngine([de], source, dest, cmd)
    saveCSV.save()