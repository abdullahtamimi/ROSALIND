
def LEXF(s,n):

        '''input:A collection of at most 10 symbols defining an ordered alphabet
        and a positive integer n

        output: all strings of length n that can be formed from the alphabet
                ordered lexicographically'''

        s=oneWord(s)
        rolls=len(s)
        lessRolls=rolls-1
        maxSpin=[lessRolls]*n
        spots=[0]*n
        firstWord=''
    
        for item in spots:
            firstWord+=s[item]
            
        print(firstWord)    
            
        while not (spots)==maxSpin:
            for pos in range(0,rolls+1):
                if pos==rolls:

                    for dig in range(0,n):
                        if spots[dig] <(lessRolls):
                            spots[dig]+=1
                            break
                
                        if spots[dig]==lessRolls:
                            spots[dig]=0
                            continue
                    
                if spots==maxSpin:
                    break
        
            sIndex=spots[::-1]
            lexString=''
        
            for index in sIndex:
                lexString+=s[index]
        
            print(lexString) 
            
            
def oneWord(s):
        '''input: a string
        output: string with removed spaces'''
    
        joinedString=''

        for letter in s:

            if letter is not ' ':
                joinedString+=letter
        return joinedString.strip()


def main():
        s='ABCDE'
        n=4
        LEXF(s,n)
        
if __name__=='__main__':
        main()
