
def MRNA(s):
        
        '''Input:  A protein string of length at most 1000 aa.
        
        Output: The total number of different RNA strings from
        which the protein could have been translated, modulo 1,000,000'''

      

        revDict={'M':1,'L':6,'S':6,'A':4,'P':4,'T':4,'F':2,'I':3,'V':4,
                'Y':2,'H':2,'N':2,'D':2,'Q':2,'K':2,'E':2,'R':6,'G':4,
                'C':2,'W':1}

        totalNum=3
                
        for AA in s:
                totalNum*=revDict[AA]
                
        print(totalNum%1000000)
                


protString=''
f=open('rosalind_mrna.txt','r')

for eachLine in f:
        protString+=eachLine
        
protString=protString.rstrip()

MRNA(protString)

f.close()
