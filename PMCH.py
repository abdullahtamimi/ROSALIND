def PMCH(k):
        
        '''Input: An RNA sequence, k, having the same # of occurences of 'A'
        as 'U' and the same # of occurences of 'C' as 'G'.
        
        Output: The total possible number of 'perfect matching' of basepair edges
                in the bonding graph of s'''

        seqLen=len(k)
        
        aCount=0

        for nuc in k:
                if nuc is 'A':
                        aCount+=1

        cCount=int((seqLen-aCount*2)/2)

        return(factorial(cCount)*factorial(aCount))

def factorial(n):

        '''input: an integer, n
        output: factorial of that integer'''

        nFact=1

        for i in range(1,n+1):
                nFact*=i
                
        return nFact
                        

def fileOpen(f):
        
         '''input is an opened file,
        will read each file and separate ROSALIND seqs
        output is sequence name, sequence'''
         
         seq=''
         seqName=''
         
         for eachLine in f:
                 if eachLine.startswith('>'):

                         seqName=eachLine[1:14].rstrip()
                         continue
                        
                 seq+=eachLine

         seq=seq.strip()        

         return(seq)


def main():

        f=open('rosalind_pmch.txt','r')
        
        seq=fileOpen(f)
        
        print(PMCH(seq))

        
       
                
        f.close()


if __name__=='__main__':
        main()
        
