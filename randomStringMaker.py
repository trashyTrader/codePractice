import random

# this program takes a file and returns a string that has 10 random lines from the file
# concatenated together with no duplicates

def randomHastagString(fileName):
    
    f = open(fileName, 'r')
    fList = []
    
    #populates a list with contents from file
    for x in f:
        fList.append(x[:-1])
        
    #must use newlines to separate words in file     
    #creates a list with each word as an index
    
    #creates a list 10 indexes long that has a smaller range than the word indexes
    randList = random.sample(range(len(fList) - 1), 10)
    final = ''
    
    #creates final string by going through random list 
    for x in randList:
        final += fList[x] + ' '
    
    return final

print(randomHastagString('hashtags.txt'))
