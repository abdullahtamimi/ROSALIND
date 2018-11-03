


def TRAN(s,t):
        
        '''Input: two DNA strings of equal length.

         a transition is defined as purine to purine or pyrimidine to
         pyrimidine
         a transversion is purine to pyrimidine or vice versa
        
        Output: the transition transversion ratio'''

        purine={'A','G'}
        pyrimidine={'C','T'}
        transition=0
        transversion=0
        
        for nucA,nucB in zip(s,t):

                if nucA is not nucB:
                        if nucA in purine and nucB in purine:
                                transition+=1
                        if nucA in purine and nucB in pyrimidine:
                                transversion+=1
                        if nucA in pyrimidine and nucB in pyrimidine:
                                transition+=1
                        if nucA in pyrimidine and nucB in purine:
                                transversion+=1
                                
        return(transition/transversion)
                                
        



                        

def fileOpen(f):
        
         '''input is an opened file,
        will read each file and separate ROSALIND seqs
        output is sequence name, sequence'''
         
         seq=''
         seqName=''
         seqList=list()
         firstPass=False
         
         for eachLine in f:
                 if eachLine.startswith('>'):

                         if firstPass:
                                 seq=seq.strip()
                                 seqList.append(seq)
                         
                         seqName=eachLine[1:14].rstrip()
                         seq=''
                         firstPass=True
                         continue
                        
                 seq=seq.rstrip()
                 seq+=eachLine

         seq=seq.strip()        
         seqList.append(seq)
         return(seqList)


def main():

        f=open('rosalind_tran.txt','r')
        
        seqList=fileOpen(f)
        s=seqList[0]
        t=seqList[1]

        print(round(TRAN(s,t),11))
        

                
        f.close()


if __name__=='__main__':
        main()
        
