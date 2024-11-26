# OS_Paging
Python program that implements the FIFO, LRU, and optimal page replacement algorithms 

A new method has been created for each replacement algorithm (FIFO, LRU, OPT)

Each method is called on a reference string with the hard-coded size of 16.

The user is required to enter the size/length of main memory ("page size") when running the code. The expected running terminal command is "python paging.py [number of page frames]"

Once running, the code will generate a reference string of random numbers from a method called generateRefStr(sizeOfRef). The three replacement algorithms will then run and a print of the number of faults resultiing from each algorithm will be shown. 

An extra method called checkReps(number, array) is used as a helping method to find repeated elements in main memory. 
