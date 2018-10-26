

def REVP(n,s):
        '''input : seqName, n and DNA seq string, s 
        will locate restriction sites of seq size 4-14 in a given seq
        restriction site is defined as a reverse palindrome
        reverse complement is identical to forward read
        output is position and length of each restriction site found'''
        '''input : seqName, n and DNA seq string, s 
        will locate restriction sites of seq size 4-14 in a given seq
        restriction site is defined as a reverse palindrome
        reverse complement is identical to forward read
        output is position and length of each restriction site found'''

        seqLength=len(s)
        palindromeList=list()
        forward=s
        for i in range (4,13):
                for nucStretch in range(0,seqLength-i+1):
                        forwardRead=forward[nucStretch:nucStretch+i]
                        
                        if forwardRead== REVC(forwardRead):

                                palindromeList.append([nucStretch+1,i])

        for item in palindromeList:
                print(*item)
        
def fileOpen(f):
        '''input is an opened file,
        will read each file and separate ROSALIND seqs
        output is sequence name, sequence'''
        seq=''
        seqName=''
       
        for eachLine in f:
                if eachLine.startswith('>'):
                      
                                
                        seqName=eachLine[1:14].rstrip()
                        seq=''
                        continue
                seq+=eachLine
                
        seq=seq.rstrip()

        return(seqName,seq)
                
                        

                                              
def REVC(s):
        '''input is DNA string
        outputs string NA reverse complement of input'''
        
        s=s[::-1]
        reverse=''
        for item in s:
                item=item.upper()

                if item == 'A':
                        reverse+='T'
                if item == 'C':
                        reverse+='G'
                if item == 'G':
                        reverse+='C'
                if item == 'T':
                        reverse+='A'
        return(reverse)

f=open('rosalind_revp.txt','r')
n,t=fileOpen(f)
REVP(n,t)
