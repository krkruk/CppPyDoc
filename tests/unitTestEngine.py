'''
Created on Jul 19, 2015

@author: krzysztof
'''
import unittest
import DocEngine
import csv


def loadFile(filename):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            data.append(line.rstrip())
    return data

class LoadData(object):
    
    def __init__(self):
        self.testData = {}
        self.addTestFile("TEST1", ("testFiles/test1.cpp",  "testFiles/test1.csv"))
        self.addTestFile("TEST2", ("testFiles/test2.cpp",  "testFiles/test2.csv"))
        self.addTestFile("TEST3", ("testFiles/test3.cpp",  "testFiles/test3.csv"))
        self.addTestFile("TEST4", ("testFiles/test4.cpp",  "testFiles/test4.csv"))
        self.addTestFile("TEST5", ("testFiles/test5.cpp",  "testFiles/test5.csv"))
        self.addTestFile("COMBINED", ("testFiles/combined.cpp",  "testFiles/combined.csv"))
        
        self.csvData = {}
        for k,v in self.testData.items():
            self.csvData[k] = self.__openTestDataInputFile(v[1])
        pass
    
    def addTestFile(self, dictEntry, tupleCPP_CSV):
        self.testData[dictEntry] = tupleCPP_CSV
        
    def getTestData(self, dictEntry):
        """Return a tuple with cpp and csv accordingly;
        Return cpp directory and loaded csv data"""
        return (self.testData[dictEntry][0], self.csvData[dictEntry])
    
    def getCSVDir(self, dictEntry):
        return self.testData[dictEntry][0]
    
    def getCppDir(self, dictEntry):
        return self.testData[dictEntry][1]
    
    def __openTestDataInputFile(self, fileName):
            with open(fileName, "r") as f:
                csvFileData = []
                for row in f:
                    csvFileData.append(row.rstrip())
                csvFileData.pop(0)
                return csvFileData
            
    def __popFirstElement(self, data):
        data.pop(0)
        return data
        

class Test_MultipleFilesCSV(unittest.TestCase):
    """Test1: test basic parsing of the data
    without any fancy input"""
      
    def setUp(self):
        #unittest.TestCase.setUp(self)
        self.data = LoadData()
        csv.register_dialect("semicolon", delimiter = ';')
          
    def tearDown(self):
        #unittest.TestCase.tearDown(self)
        pass
      
    def __loadAndTest(self, sourceDataDir, inputData):
        """inputData - loaded list with string to test
        sourceDataDir - proper directory to the cpp test file"""
        engine = DocEngine.DocEngine(sourceDataDir)
        parsedElems = engine.parse()
        inData = csv.reader(inputData, dialect = "semicolon")
        for entry, comp in zip(inData, parsedElems):
            self.assertEqual(entry[0], entry[0], "{} != {}".format(entry[0], comp[0]))
            self.assertEqual(entry[1], entry[1], "{} != {}".format(entry[1], comp[1]))
            self.assertEqual(entry[2], entry[2], "{} != {}".format(entry[2], comp[2]))
  
    def test_parse_basic_content_without_namespace_and_specifierTEST1(self):
        cppData, csvData = self.data.getTestData("TEST1")
        self.__loadAndTest(cppData, csvData)
          
    def test_parse_basic_content_without_namespace_and_specifierTEST2(self):
        cppData, csvData = self.data.getTestData("TEST2")
        self.__loadAndTest(cppData, csvData)
          
    def test_parse_basic_content_without_namespace_and_specifierTEST3(self):
        cppData, csvData = self.data.getTestData("TEST3")
        self.__loadAndTest(cppData, csvData)
          
    def test_parse_basic_content_with_namespace_and_specifierTEST4(self):
        cppData, csvData = self.data.getTestData("TEST4")
        self.__loadAndTest(cppData, csvData)
          
    def test_parse_basic_content_with_namespace_and_specifier_fancy_formatTEST5(self):
        cppData, csvData = self.data.getTestData("TEST5")
        self.__loadAndTest(cppData, csvData)
          
    def test_parse_basic_content_combinedAllTogether(self):
        cppData, csvData = self.data.getTestData("COMBINED")
        self.__loadAndTest(cppData, csvData)
            
class Test_FuncBody(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        with open("testFiles/funcBody.cpp", 'r', encoding="utf-8") as f:
            self.funcBody = []
            for line in f:
                self.funcBody.append(line.rstrip())
        try:
            self.csvFile = open("testFiles/combined.csv", "r")
        except Exception as e:
            print("EXCEPTION {}".format(e))
            self.fail(e)
            
        self.csvData = csv.reader(self.csvFile, delimiter=';')
        self.docData = []
        for line in self.csvData:
            self.docData.append(line[2])
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        if not self.csvFile.closed:
            self.csvFile.close()            
                
    def test_funcBody_extractDoc(self):
        fb = DocEngine.DocFuncBody()
        self.docData.pop(0) #discard first element
        for testData, parsedData in zip(self.docData, self.funcBody):
            self.assertEqual(testData, fb.getComment(parsedData))
            

class Test_FuncName(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        with open("testFiles/funcName.cpp") as f:
            self.funcName = []
            for line in f:
                self.funcName.append(line.rstrip())
        try:
            self.csvFile = open("testFiles/combined.csv", "r")
        except Exception as e:
            print("EXCEPTION {}".format(e))
            self.fail(e)
            
        self.csvData = csv.reader(self.csvFile, delimiter=';')
        self.docData = []
        for line in self.csvData:
            self.docData.append([line[0], line[1]])
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        if not self.csvFile.closed:
            self.csvFile.close()            
                
    def test_funcName_extractName(self):
        fn = DocEngine.DocFuncName()
        self.docData.pop(0) #discard first element
        for testData, data in zip(self.docData, self.funcName):
            testName = testData[1]
            compName = fn.getName(data)
            self.assertEqual(testName, compName, "DATA: {} != {}".format(testName, compName))
            
    def test_funcName_extractNamespace(self):
        fn = DocEngine.DocFuncName()
        self.docData.pop(0) #discard first element
        for testData, data in zip(self.docData, self.funcName):
            testNs = testData[0]
            compNs = fn.getNamespace(data)
            self.assertEqual(testNs, compNs, "DATA: {} != {}".format(testNs, compNs))
            
class Test_SplitFunctionContent(unittest.TestCase):
    def setUp(self):
        self.combined = loadFile("testFiles/combined.cpp")
        self.funcName = loadFile("testFiles/funcName.cpp")
        self.funcBody = loadFile("testFiles/funcBody.cpp")
        self.funcTEST1 = loadFile("testFiles/test1.cpp")
        self.funcNameTEST1 = loadFile("testFiles/funcNameTEST1.cpp")
        self.funcBodyTEST1 = loadFile("testFiles/funcBodyTEST1.cpp")
        
    def test_splittingCombined(self):
        lineIter = iter(self.combined)
        de = DocEngine.DocEngine("testFiles/combined.cpp")
        data =  de.splitFunction(lineIter)
        for fN, fB, toCheck in zip(self.funcName, self.funcBody, data):
            self.assertEqual(fN, toCheck[0], "{} IS NOT {}".format(fN, toCheck[0]))
            self.assertEqual(fB, toCheck[1], "{} IS NOT {}".format(fB, toCheck[1]))
    
    def test_splittingTEST1(self):
        lineIter = iter(self.funcTEST1)
        de = DocEngine.DocEngine("testFiles/test1.cpp")
        data = de.splitFunction(lineIter)
        for fN, fB, toCheck in zip(self.funcNameTEST1, self.funcBodyTEST1, data):
            self.assertEqual(fN, toCheck[0], "{} IS NOT {}".format(fN, toCheck[0]))
            self.assertEqual(fB, toCheck[1], "{} IS NOT {}".format(fB, toCheck[1]))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    