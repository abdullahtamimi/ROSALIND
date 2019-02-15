

def fileOpen(file):

    '''input: an opened file containing an alphabet, and a positive digit
    output: a list containing each symbol of the alphabet, and the positive digit n'''

    firstPass=True
    alphList=list()
    
    for eachLine in file:

        if firstPass:
            for letter in eachLine:
                if letter is not ' ':
                    alphList.append(letter)
            firstPass=False
            
        if not firstPass:
           n=eachLine.strip()
        
    alphList.pop()
    n=int(n)

    return alphList, n



def LEXV(aList,n):

    '''input:a list containing an ordered alphabet, an integer n which corresponds
    with the maximum length of a string
    output: all strings of length at most n formed from the given alphabet, ordered
        lexicographically'''

    corrN=n-1
    posCount=0
    numLet=len(aList)-1
    lastWord=[numLet]*n
    curWord=[-1]*n
    testWord=''
    outFile=open('lexv_out.txt','w')

    while curWord != lastWord:

        for pos in curWord:
            
            if posCount == corrN and curWord[posCount] <= numLet:

                curWord[posCount]+=1
                
                testWord=makeWord(aList,curWord)
                outFile.write(testWord+'\n')

                if curWord[posCount] == numLet:
                    
                    if curWord == lastWord:
                        break

                    curWord[posCount]=-1
                    posCount-=1

            if posCount!= corrN and curWord[posCount] < numLet:
                
                curWord[posCount]+=1
                
                testWord = makeWord(aList,curWord)
                        
                outFile.write(testWord+'\n')
                testWord=''
                    
                posCount+=1

            if posCount!= corrN and curWord[posCount] == numLet:
                curWord[posCount]=-1
                posCount-=1


    outFile.close()



def makeWord(aList,curWord):

    '''input:a list with indices relating to the alphabet list, the alphabet list
    output: a word constructed from alphabet list with given indices'''

    outWord=''

    for item in curWord:
        
        if item != -1:
            outWord += aList[item]

    return outWord
            


def main():

    f=open('rosalind_lexv.txt','r')

    x,n=fileOpen(f)
    LEXV(x,n)

    f.close()


if __name__ == '__main__':
    main()
    
