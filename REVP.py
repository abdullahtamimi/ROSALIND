

def REVP(n,s):
        '''input : seqName, n and DNA seq string, s 
        will locate restriction sites of seq size 4-14 in a given seq
        restriction site is defined as a reverse palindrome
        reverse complement is identical to forward read
        output is position and length of each restriction site found'''
        
        seqLength=len(s)
        palindromeSet=set()
        palindromeList=[]      
       
        for nucStretch in range(0,seqLength+1):
                for endSite in range(nucStretch+4,nucStretch+13):
                                
                        forwardRead=s[nucStretch:endSite]
                        reverseRead=REVC(forwardRead)
                            
                        if len(forwardRead)>=4 and len(reverseRead)>=4:
                                    
                                if forwardRead in reverseRead:
                                        palindromeSet.add(str(nucStretch+1)+'%'+str(len(forwardRead)))


        for item in palindromeSet:
                item=item.split('%')
                palindromeList.append([int(item[0]),int(item[1])])
                                      
                
        for item in sorted(palindromeList):
                print(*item,sep='\t')

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
