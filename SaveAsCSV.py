from inspect import isgenerator
import os.path as op
import Tools
import glob

#args.source, args.destination[0], args.recursive

class SaveAsCSV(object):
    '''
    Save a list as a csv file separated with semicolons
    '''

    def __init__(self, dest):
        self.dest = dest
    
    def save(self, parsedDataList):
        """Save a list as a csv file separated with semicolons"""
        with open(self.dest, 'w') as f:
            for line in parsedDataList:
                f.write(';'.join(line) + '\n')
                
                
class SaveAsCSVEngine(object):
    """Parse files and save them to a single csv file."""
    def __init__(self, parseEngineList, source, dest, *cmd):
        """Constructor
        parseEngineList - requires a list with parsing engines based on ParseEngineAbstract
        source - file or directory (full path)
        destination - csv file to be created (full path)
        *cmd - list of additional parameters; The most important is recursion (if cmd[0] = True)
        """
        self.dest = dest
        self.cmd = cmd
        self.recursive = cmd[0][0]
        self.data = []
        
        if(isgenerator(parseEngineList) 
           or isinstance(parseEngineList, (list, tuple))):
            self.engines = parseEngineList
        else:
            raise TypeError("Must pass parsing engines list")
            
        if op.isfile(source[0]):
            self.source = source
        else:
            self.source = []
            if self.recursive:
                for file in Tools.getFilesRecursively(source[0]):
                    self.source.append(file)
            else:
                l = len(source[0]) - 1
                if source[0][l] == '/':
                    ext = "*.*"
                else:
                    ext = "/*.*"
                self.source = glob.glob(source[0] + ext)

        self.source = sorted(self.source)

    def _loadData(self):
        for engine in self.engines:
            for source in self.source:
                engine.loadFile(source)
                for ns, name, doc in engine.parse():
                    self.data.append([ns, name, doc])
        
    def save(self):
        """Parse files and save the data to a csv file"""
        self._loadData()
        save = SaveAsCSV(self.dest)
        save.save(self.data)

