#Gina Fornasari
#FRNGIN001

#Relevant imports
import random
import sys

#a function used to generate the random Reference string
def generateRefStr(size):
    refStr = ""
    for i in range(size):
        #generating a random number between one and nine (inclusive)
        num = random.randint(0,9)
        refStr +=str(num)
    
    return refStr

#function that checks for a repeated number taking a number and a list
def checkReps(number, array):
    for i in range(len(array)):
        if(number==array[i]):
            return True
    return False

#First in first out algorithm
def FIFO(pgsize, refstr):
    hits = 0
    faults = 0
    mainMem = []
    counter = 0

    #running until main memory is full
    while (len(mainMem)<pgsize):
        if(counter>len(refstr)-1):
            break

        #if a number is repeated, do not add to main memory as it is already there, this is a hit
        repeat = checkReps(refstr[counter], mainMem)
        if (repeat==False):
            mainMem.append(refstr[counter])
            counter+=1
            faults+=1
        else:
            counter+=1
            hits+=1

    #memory now full - time to replace or hit
    currentIndexInRef = counter
    replaceIndex = 0

    #continuously run through the numbers in the reference string
    while(currentIndexInRef<=(len(refstr)-1)):
        currentNum=refstr[currentIndexInRef]
        #check if the current number is already present
        found=checkReps(currentNum,mainMem)

        if (found):
            hits+=1

        else:
            #not in memory currently, need to do a replacement
            mainMem[replaceIndex]=currentNum
            replaceIndex+=1
            faults+=1
        
        if(replaceIndex>=pgsize):
            replaceIndex=0
        
        currentIndexInRef+=1

    return faults
    #print("HITS:" + str(hits))
    #print("MISSES:" + str(faults))

#Least recently used algorithm
def LRU(pgSize,refStr):
    hits = 0
    faults = 0
    mainMem = []
    counter=0

#initially filling memory
    while(len(mainMem)<pgSize):
        if(counter>len(refStr)-1):
            break

        repeat= checkReps(refStr[counter],mainMem)
        if(repeat==False):
            mainMem.append(refStr[counter])
            faults+=1
        else:
            hits+=1

        counter+=1



    #memory now full: lets get down to business (replacement or hit)

    currentIndexofRef = counter

    #iterating though the elements of the reference string
    while(currentIndexofRef<=(len(refStr)-1)):
        currentNum = refStr[currentIndexofRef]
        found = checkReps(currentNum, mainMem)

        if (found):
            #in memory, hit
            hits+=1
        else: 
            #not currently in memory, need to replace
            faults+=1
            move=0

            #initially assuming the element to replace 
            num2replace=refStr[currentIndexofRef-pgSize]

            #checking to see if the chosen element has been hit recently
            for i in range(pgSize):
                currN = refStr[currentIndexofRef-i-1]
                start = currentIndexofRef-int(pgSize)-i
                end = currentIndexofRef-i-1
                currStr = refStr[start:end]
                repped = checkReps(currN,currStr)
                if(repped):
                    #if the element has been repeated, there was a recent hit and this element has not been in memory the longest
                    #move to the next element accross
                    move+=1
            
            num2replace=refStr[int(currentIndexofRef-pgSize-move)]

            #replacing the element
            for k in range(len(mainMem)):
                if(num2replace==mainMem[k]):
                    mainMem[k]=currentNum
                    break
        currentIndexofRef+=1
    
    #print("HITS:" + str(hits))
    #print("MISSES:" + str(faults))
    return faults

#optimal algorithm
def OPT(size, refStr):
    hits = 0
    faults=0
    mainMem = []
    counter = 0

    #initially filling memory
    while(len(mainMem)<size):
        #if we have iterated through all the elements, break from the loop
        if(counter>len(refStr)-1):
            break
     
        repeat = checkReps(refStr[counter], mainMem)
        if(repeat==False):
            mainMem.append(refStr[counter])
            faults+=1
        else:
            hits+=1
        
        counter+=1

    #memory now full - time to replace or hit

    currentIndexInRef = counter
    #string holding the remaining elements
    usingStr = refStr[currentIndexInRef:]

    #loop that runs until all remaining elements have been seen
    while(len(usingStr)>0):
        found=False
        indexOfElements = []

        found = checkReps(usingStr[0], mainMem)

        if (found):
            hits+=1

        else:
            faults+=1
            for i in range(size):
                try:
                    #looking for the next occurance of the elements in memory
                    ind = usingStr.index(mainMem[i])
                except ValueError:
                    #if there is no other occurance of the element
                    ind = -1
                
                indexOfElements.append(ind)

            highest = 0
            indOfHighest=0

            for j in range(len(indexOfElements)):
                #finding the index of the element that will be used again last
                if(indexOfElements[j]==-1):
                    #any element that is not repeated is swapped out first
                    #if non of the remaining elements have repetitions, the first one is replaced
                    highest = -1
                    indOfHighest = j
                    break
                else:
                    if(int(indexOfElements[j])>highest):
                        highest=indexOfElements[j]
                        indOfHighest=j

            #replacing the element used last
            mainMem[indOfHighest] = usingStr[0]
        
        
        currentIndexInRef+=1
        #moving the remaining elements up by one
        usingStr = refStr[currentIndexInRef:]
    

    #print("HITS: "+ str(hits))
    #print("MISSES: "+ str(faults))
    return faults


def main():
    #size of the reference string
    sizeOfRef=16
    #size of the memory page, between 1 and 7, imputted by the user
    sizeOfPg = int(sys.argv[1]) 

    #generating a random string of elements with the chosen size
    refStr = generateRefStr(sizeOfRef)
    print("The Reference String generated: "+refStr)

    print("FIFO: " + str(FIFO(sizeOfPg,refStr))+ " page faults.")
    print("LRU: " + str( LRU(sizeOfPg,refStr))+ " page faults.")
    print("OPT: "+ str(OPT(sizeOfPg,refStr))+ " page faults.")
    
if __name__=="__main__":
    if len(sys.argv)!=2:
        print ("Usage: python paging.py [number of page frames]")
    else:
        main()
