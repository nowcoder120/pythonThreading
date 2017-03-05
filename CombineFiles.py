"""
This class will attempt to use threads to read in files and
locks to safely write them out to a single file
"""
 
from os import listdir
from os.path import isfile, join
from FileReader import FileReader
import threading
  
# constant for input directory
INPUT_DIR = './inputs/'
   
# name for thread logging
THREAD_BASE_NAME = "Thread_"
    
# grab the list of input files
files = [f for f in listdir(INPUT_DIR) if isfile(join(INPUT_DIR, f))]
     
      
threadNumber = 1;
# loop over files and spawn threads to handle the merging
for f in files:
    # create thread
    threadName = THREAD_BASE_NAME + str(threadNumber)
    fileReaderThread = FileReader(INPUT_DIR + f, threadName)
    threadNumber += 1
    
    # kick off thread
    fileReaderThread.start()
