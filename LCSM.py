
def LCSM(k):
        
        '''Input: A collection of k DNA strengths of length at most 1kbp each
        in FASTA format.,
        Output: The longest common substring of the collection'''
        firstSeq=False
        baseSet=set()

        for eachSeq in k:
                if not firstSeq:
                        baseSet=subSetGen(eachSeq)
                        firstSeq=True

                if firstSeq:
                        compSet=subSetGen(eachSeq)
                        baseSet=baseSet.intersection(compSet)
        return(baseSet)
                        
                        



def subSetGen(seq):
        
        '''Input: A collection of k DNA strengths of length at most 1kbp each
        in FASTA format.,
        Output: The longest common substring of the collection'''

        subSeqSet=set()
        seqLength=len(seq)
        
        for nucA in range(0,seqLength):
                
                for nucB in range(0,seqLength):
                        
                        subSeq=seq[nucA:nucB]

                        if subSeq is not '':

                                subSeqSet.add(subSeq)
                        
                        
        return subSeqSet


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

        f=open('rosalind_lcsm.txt','r')
        
        seqList=fileOpen(f)

        subSeqs=LCSM(seqList)

        print(max(subSeqs,key=len))

        f.close()


if __name__=='__main__':
        main()
        


        
        

        
