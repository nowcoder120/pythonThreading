"""
This class will allow for threads to handle reading the input files and
locking so that only one thread at a time writes to the output file
"""
import threading
import sys
 
class FileReader(threading.Thread):
      
    # create a class instance lock for our threads
    ourLock = threading.Lock()
    ourWriteFile = './output/outFile.txt'
                                                                    
    # this method is automatically called on a class instantiation
    def __init__(self, inputFile, threadName):
        # "self.variableName" creates instance variables, these can be referenced
        # inside of this object using "self.blah"
        #
        # _variableName is used to "declare" something that should be
        # treated as private though python doesn't enforce it
        self._myInputFile = inputFile
        self._myThreadName = threadName

        # make sure to call super class __init__()
        super(FileReader, self).__init__()
    
    # overwrite run method to implement threading
    def run(self):
        myFile = open(self._myInputFile, 'r')
        try:
            for myLine in myFile:
                self.ourLock.acquire()
                print(self._myThreadName + " is writing to file now")
                outFile = open(self.ourWriteFile, 'a+')
                outFile.write(myLine)
                outFile.close()
                self.ourLock.release()
        except IOError:
            print("An IO Error occurred while trying to write out to the file.")
            self.ourLock.release()
        except:
            print("An unexpected error occurred :", sys.exc_info()[0])
            self.ourLock.release()
