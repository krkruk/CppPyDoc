'''
Created on Jul 29, 2015

@author: krzysztof
'''
import unittest
import UserInputParse as uip


class Test(unittest.TestCase):


    def setUp(self):
        self.inp1 = ["-s", "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/combined.cpp",
                     "-d", "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/inp1.csv"]
        self.inp2 = ["--source=/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV",
                     "--destination=/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/inp2.csv"]
        self.inp3 = ["--recursive",
                     "--source=/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV",
                     "--destination=/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/inp3.csv"]
        
        self.comp1 = {"source": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/combined.cpp",
                      "dest": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/inp1.csv",
                      "recursive": False}
        self.comp2 = {"source": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV",
                      "dest": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/inp2.csv",
                      "recursive": False}
        self.comp3 = {"source": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV",
                      "dest": "/home/krzysztof/Programming/Eclipse/Python/CppPyDoc/tests/testFiles/toCSV/inp3.csv",
                      "recursive": True}


    def tearDown(self):
        pass


    def test_inp1_fileAsInput(self):
        data = uip.UserInputParse(self.inp1)
        source, dest, *cmd = data.getCmd()
        self.assertEqual(source, [self.comp1["source"]], "source:Comp: {} != {}".format(source,  self.comp1["source"]))
        self.assertEqual(dest, self.comp1["dest"], "dest:Comp {} != {}".format(dest,  self.comp1["dest"]))
        self.assertEqual(cmd[0], self.comp1["recursive"], "cmd[0]:Comp: {} != {}".format(cmd[0],  self.comp1["recursive"]))
    
    def test_inp2_dirAsInput(self):
        data = uip.UserInputParse(self.inp2)
        source, dest, *cmd = data.getCmd()
        self.assertEqual(source, [self.comp2["source"]], "source:Comp: {} != {}".format(source,  self.comp2["source"]))
        self.assertEqual(dest, self.comp2["dest"], "dest:Comp {} != {}".format(dest,  self.comp2["dest"]))
        self.assertEqual(cmd[0], self.comp2["recursive"], "cmd[0]:Comp: {} != {}".format(cmd[0],  self.comp2["recursive"]))
    
    def test_inp3_dirAsInput_Recursive(self):
        data = uip.UserInputParse(self.inp3)
        source, dest, *cmd = data.getCmd()
        self.assertEqual(source, [self.comp3["source"]], "source:Comp: {} != {}".format(source,  self.comp3["source"]))
        self.assertEqual(dest, self.comp3["dest"], "dest:Comp: {} != {}".format(dest,  self.comp3["dest"]))
        self.assertEqual(cmd[0], self.comp3["recursive"], "cmd[0]:Comp: {} != {}".format(cmd[0],  self.comp3["recursive"]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()