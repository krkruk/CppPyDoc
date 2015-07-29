'''
Created on Jul 29, 2015

@author: krzysztof
'''
import os
import fnmatch

def getFilesRecursively(startPath, extension="*"):
    """
    Get a generator object to return the list of files.
    startPath - start point where recursion begin
    extension - extension that files are to be found
    """
    if not os.path.isdir(startPath):
        raise StopIteration
    for dirpath, _, filenames in os.walk(startPath):
        for filename in fnmatch.filter(filenames, extension):
            yield os.path.join(dirpath, filename)