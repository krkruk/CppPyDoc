'''
Created on Jul 29, 2015

@author: krzysztof
'''
import unittest
import SaveAsCSV as sacsv
import DocEngine

class TestSaveFileToCSV(unittest.TestCase):


    def setUp(self):
        self.inp1 = {"source": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/combined.cpp",
                      "dest": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/inp1.csv",
                      "recursive": False}
        self.inp2 = {"source": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV",
                      "dest": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/inp2.csv",
                      "recursive": False}
        self.inp3 = {"source": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV",
                      "dest": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/inp2.csv",
                      "recursive": True}
        
        self.comp1 = "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/combined.csv"
        self.comp2 = "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/comp2.csv"
        self.comp3 = "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/combined.csv"

    def _loadData(self, filePath):
        pass
    
    def tearDown(self):
        pass


    def test_inp1_singleFile_Save(self):
        save = sacsv.SaveAsCSV(self.inp1["dest"])
        data = []
        with open(self.comp1, 'r') as f:
            for line in f:
                data.append(line.rstrip().split(';'))
        save.save(data)
        
        with open(self.comp1, "r") as f:
            compFile = f.readlines()
            compFile.pop(0)
        with open(self.inp1["dest"], 'r') as f:
            genFile = f.readlines()            
            genFile.pop(0)
        self.assertEqual(compFile, genFile, "gen:Comp {} != {}".format(genFile, compFile))               
        
    
    def test_inp2_dirInput_Save(self):
        save = sacsv.SaveAsCSV(self.inp2["dest"])
        data = []
        with open(self.comp2, 'r') as f:
            for line in f:
                data.append(line.rstrip().split(';'))
        save.save(data)
        
        with open(self.comp2, "r") as f:
            compFile = f.readlines()
            compFile.pop(0)
        with open(self.inp2["dest"], 'r') as f:
            genFile = f.readlines()   
            genFile.pop(0)         
        self.assertEqual(compFile, genFile, "gen:Comp {} != {}".format(genFile, compFile))    
    
    def test_inp3_dirInput_Save(self):
        save = sacsv.SaveAsCSV(self.inp3["dest"])
        data = []
        with open(self.comp3, 'r') as f:
            for line in f:
                data.append(line.rstrip().split(';'))
        save.save(data)

        with open(self.comp3, "r") as f:
            compFile = f.readlines()
            compFile.pop(0)
        with open(self.inp3["dest"], 'r') as f:
            genFile = f.readlines()      
            genFile.pop(0)      
        self.assertEqual(compFile, genFile, "gen:Comp {} != {}".format(genFile, compFile))    

class TestSaveFileToCSVEngine(unittest.TestCase):
    def setUp(self):
        self.inp1 = {"source": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/combined.cpp",
                      "dest": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/inp1.csv",
                      "recursive": False}
        self.inp2 = {"source": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV",
                      "dest": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/inp2.csv",
                      "recursive": False}
        self.inp3 = {"source": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV",
                      "dest": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/inp2.csv",
                      "recursive": True}
        
        self.comp1 = "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/combined.csv"
        self.comp2 = "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/comp2.csv"
        self.comp3 = "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/combined.csv"
#     (self, parseEngineList, source, dest, *cmd):

    def test_inp1_singleFile_NotRecursive(self):
        de = DocEngine.DocEngine(self.inp1["source"])
        save = sacsv.SaveAsCSVEngine([de], [self.inp1["source"]], self.inp1["dest"], self.inp1["recursive"])
        save.save()
        
        with open(self.comp1, "r") as f:
            compFile = f.readlines()
            compFile.pop(0)
        with open(self.inp1["dest"], 'r') as f:
            genFile = f.readlines()            

        self.assertEqual(compFile, genFile, "gen:Comp {} != {}".format(genFile, compFile))  
        
    def test_inp2_dirInput_NotRecursive(self):
        de = DocEngine.DocEngine(self.inp2["source"])
        save = sacsv.SaveAsCSVEngine([de], [self.inp2["source"]], self.inp2["dest"], self.inp2["recursive"])
        save.save()
        
        with open(self.comp2, "r") as f:
            compFile = f.readlines()
            compFile.pop(0)
        with open(self.inp2["dest"], 'r') as f:
            genFile = f.readlines()            

        self.assertEqual(compFile, genFile, "gen:Comp {} != {}".format(genFile, compFile))       
           
    def test_inp3_dirInput_Recursive(self):
        de = DocEngine.DocEngine(self.inp3["source"])
        save = sacsv.SaveAsCSVEngine([de], [self.inp3["source"]], self.inp3["dest"], self.inp3["recursive"])
        save.save()
        
        with open(self.comp3, "r") as f:
            compFile = f.readlines()
            compFile.pop(0)
        with open(self.inp3["dest"], 'r') as f:
            genFile = f.readlines()            

        self.assertEqual(compFile, genFile, "gen:Comp {} != {}".format(genFile, compFile))  
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()