import re
from ParseEngineAbstract import *
        
class DocFuncBody(object):
    """Find and parse documentation string in the file."""
    def __init__(self):
        self.getDocScope = """
                            \/\*                                     #find "/*"
                            ([\w\s\t\,\.\&\*\:\"\'                        #paramteres
                            \=\<\>\!\(\)\<\>\?\[\]
                            \+\-\/\@\#\$\%\^\|]*)
                            \*\/                                     #closing "*/"
                           """
        self.getDocInline = """
                            \/\/                                    #find "//"
                            ([\s\w\*\;\'\"\.\,\?                    #comment content
                            \!\@\#\$\%\^\&\(\)\=\_\-]*)
                            """
        self.reGetDocScope = re.compile(self.getDocScope, re.X)
        self.reGetDocInline = re.compile(self.getDocInline, re.X)
        
    def getComment(self, bodyContent):
        """Find and return documentation string found in bodyContent."""
        bodyContent = str(bodyContent)
        dScope = self.reGetDocScope.search(bodyContent)
        dInline = self.reGetDocInline.search(bodyContent)

        if dScope or dInline:
            docData = ""
            if(dScope):
                try:
                    docData = dScope.group(1)
                    docBeg = dScope.start(1)
                    if( docData[docBeg] == bodyContent[docBeg]  #if comment is found but it is not
                        and bodyContent[docBeg].isalnum() ):     #at the begining then no comment at all
                        return "EMPTY"              
                    
                except:
                    return "EMPTY"
            else:   #parse inline documentation
                try:
                    docSet = []
                    docEnd = dInline.end(1)
                    docEndPrev = dInline.start(1)
                    docBeg = dInline.start(1)   #first group starts always at 3 pos
                                                #but it is needed to add two additional chars                 

                    docBegPrev = docBeg + 2     #magic
                    try:
                        while docEndPrev < docEnd:      #find another // comments
                            docSet.append(dInline.group(1))
                            dInline = self.reGetDocInline.search(bodyContent[docEnd:])
                            docEndPrev, docEnd = docEnd, dInline.end(1) + docEnd
                            if docBegPrev != dInline.start(1):
                                break;
                    except:
                        pass

                    docData = " ".join(docSet)
                    if( docData[docBeg] == bodyContent[docBeg]  #if comment is found but it is not placed
                        and bodyContent[docBeg].isalnum() ):     #at the begining then no comment at all
                        return "EMPTY"

                except: return "EMPTY"
                  
            docData = docData.replace(" *", "", docData.count(" *"))
            docData = docData.replace("--", "", docData.count("--"))
            docData = docData.replace("\\n", "", docData.count(""))
            docData = re.sub(r"\s+", ' ', docData)              
            docData = docData.lstrip().rstrip()
            return docData
        else:
            raise NoDocTextFoundException("DOC COMMENT NOT FOUND IN: {}".format(bodyContent))
    
class DocFuncName(object):
    """Parsing declaration of the function."""
    def __init__(self):
        self.rePatternNs = """
                            \s\&{0,2}\*?                   #find a start of the ns 
                            ([\w\_\:]*)                    #namespace
                            (\:\:)                         #final ::
                           """
        
        self.reGetNs = re.compile(self.rePatternNs, re.X)
        
    def getNamespace(self, data):
        """Find a namespace in data input. The function returns
        a string with the namespace. If no namespace found, the
        function returns "::" as a default."""
        nsMatch = self.reGetNs.search(data)       
        if nsMatch:
            return nsMatch.group(1)
        else:
            return "::"
    
    def getName(self, data):
        """Find name of the function in data input. The getName
        returns declaration of the method withoud any namespace included."""
        nsMatch = self.reGetNs.search(data)       
        if nsMatch:
            data = data.replace(nsMatch.group(0), " ")
            return data
        else:
            return data
        pass

class DocEngine(ParseEngineAbstract):
    """Parsing engine for a single file. The object init requires
    file name to the file. In order to parse a file a parse method
    must be called."""
    def __init__(self, fileName, ext = "cpp"):
        self._ext = ext
        self.loadFile(fileName)
        self._rePatternFunction = """
                    (const|constexpr|static|friend
                    \[\[noreturn\]\]|virtual|inline
                    |override|final)*                            #return specifier e.g. const
                    [\w\d\_\:\&\*\<\>]*                          #data type
                    \s
                    [\w\_\:\&\*]*                                #namespace
                    [\w]*                                        #function name
                    \s? \(                                       #optional space; paranthesis
                    [\w\s\t\,\.\&\*\:\"\'                        #paramteres
                    \=\<\>\!\(\)\<\>\?\[\]
                    \+\-\/\@\#\$\%\^\|]*          
                    
                    
                            #if the definition is multiline, must check ) bracket
                            #in the text line
                    \s*\)?                                       #optional space; paranthesis
                    \s*[\-\>]{0,2}                               #encapsulation operator

                    """
    
        self._regEngineFunctionName = re.compile(self._rePatternFunction, re.VERBOSE)

    def __exit__(self):
        pass
    
    def __countBrackets(self, textLine, openBracket = '(', closeBracket = ')'):
        """Get number of individual brackets
        textLine - string
        openBracket, closeBracket - characters that should be seeked, 
        opening and closing one accordingly""" 
        opening = textLine.count(openBracket)
        closing = textLine.count(closeBracket)
        return (opening, closing)
    
    def __updateBracketCounter(self, textLine, currentOpen="0",
                                currentClose="0", openBracket = '(', closeBracket = ')'):
        opening, closing = self.__countBrackets(textLine, openBracket, closeBracket)
        currentOpen += opening
        currentClose += closing
        return currentOpen, currentClose
    
    
    def splitFunction(self, lineIter):
        """Split the function into two parts consisting of the
        function declaration and its namespace (further called funcName)
        and the function body. The algorithm counts parenthesis and braces
        in order to split the file properly. The function returns a
        generator object consisting of a tuple: funcName and funcBody.        
        lineIter: data file iterator"""
        for row in lineIter:
            openPCount, closePCount = 0, 0
            openBCount, closeBCount = 0, 0
            funcContent = []
            funcMatch = self._regEngineFunctionName.match(row)
            if funcMatch:
                funcContent.append(row.lstrip().rstrip())
                openPCount, closePCount = self.__countBrackets(row)
                openBCount, closeBCount = self.__countBrackets(row, '{', '}')
                
                while (openPCount > closePCount):                    
                    nextRow = next(lineIter)
                    funcContent.append(nextRow.lstrip().rstrip())
                    openPCount, closePCount = self.__updateBracketCounter(nextRow, openPCount, closePCount)
                    openBCount, closeBCount = self.__updateBracketCounter(nextRow, openBCount, closeBCount, '{', '}')
                
                #check the variant if: func(){;
                while openBCount == 0:      #read all before '{' and append to the funcName
                    nextRow = next(lineIter)
                    buf = funcContent.pop().rstrip()
                    funcContent.append(buf)
                    funcContent.append(nextRow.lstrip().rstrip())
                    openBCount, closeBCount = self.__updateBracketCounter(nextRow, openBCount, closeBCount, '{', '}')
                    
                funcName = " ".join(funcContent)
                index = funcName.rfind("{")
                funcBodyLine = ""
                if index >= 0:
                    funcBodyLine = '{' + funcName[index+1:]
                    funcName = funcName[:index].rstrip()
                funcContent.clear()
                
                while (openBCount > closeBCount
                       or openBCount == 0):
                    nextRow = next(lineIter)
                    nextRow = nextRow + '\\n' if nextRow.find("//") >= 0 else nextRow
                    funcContent.append(nextRow.lstrip().rstrip())
                    openBCount, closeBCount = self.__updateBracketCounter(nextRow, openBCount, closeBCount, '{', '}')
                    
                funcBody = funcBodyLine + " ".join(funcContent)    
                funcContent.clear()
                yield funcName, funcBody
        
    def parse(self, noDescFoundMsg = ""): 
        """Parse the entire file at given fileName. The function
        returns the generator object consisting of 
        Namespace, Function name, Documentation.
        noDescFoundMsg: string in case when no doc string found"""
        lineIter = iter(self._dataLines)
        data = self.splitFunction(lineIter)
        fb = DocFuncBody()
        fn = DocFuncName()
        for line in data:
            try:
                docData = fb.getComment(line[1])
            except NoDocTextFoundException:
                docData = noDescFoundMsg
            docNs = fn.getNamespace(line[0])
            docName = fn.getName(line[0])
            #retData.append(docNs + ';' + docName + ';' + docData)
            yield docNs, docName, docData
