import sys
import argparse
import os.path as op

class InputSourceError(Exception):
    def __init__(self, value):
        self.text = value
        
    def __str__(self):
        print("INPUT SOURCE ERROR: ".format(self.text))
        print("No file or directory incorrect")

class UserInputParse(object):
    '''
    Parse user input. The class enables passing commands via command line.
    '''
    def __init__(self, dataInput = sys.argv[1:]):
        '''
        dataInput - list with commands in Unix-like pattern. By default
        it is sys.argv[1:]
        '''
        self.input = dataInput
        self.parser = argparse.ArgumentParser(
            description="""CppPyDoc is a tool that creates documentation
            based on C++ comments included in *.cpp files""")
        
    def getCmd(self):
        """Return [source], destination, *cmds"""
        
        self.parser.add_argument(
            "-s", "--source", nargs='+', required=True, type=str, help="Source file(s) or directory")
        self.parser.add_argument(
            "-d", "--destination", nargs=1, required=True, type=str, help="Save parsed data in a file")
        self.parser.add_argument(
            "-r", "--recursive", required=False, 
            action="store_true", default=False, help="Parse all files in all children directories. It starts at source.")
        
        args = self.parser.parse_args(self.input)
        if not op.isdir(args.source[0]):
            for sourceFile in args.source:
                if not op.isfile(sourceFile):
                    raise InputSourceError(sourceFile)
        
        return args.source, args.destination[0], args.recursive
