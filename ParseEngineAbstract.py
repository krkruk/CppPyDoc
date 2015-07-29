'''
Created on Jul 29, 2015

@author: krzysztof
'''

class ParseEngineAbstract(object):
    '''
    classdocs
    '''
    def __init__(self):
        self._dataLines = ""
        self._ext = ""
        pass
    
    def parse(self, noDescFoundMsg = ""):
        """Return generator object which constains list
        of elements"""
        pass
    
    def loadFile(self, fileName):
        """Load file
        fileName - standard file name
        ext - extension e.g cpp, h. No commas etc."""
        if fileName.find('.' + self._ext) > -1:
            with open(fileName, "r") as f:
                self._dataLines = f.readlines()
        else:
            self._dataLines = []

class NoDocTextFoundException(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str(self):
        print("EXCEPTION: {}".format(self.value))