import urllib
from urllib.request import Request, urlopen

def MPRT(seqList):
        '''input is a Uniprot ID
        if fasta AA sequence for protein has NGlycosylation motif
        output:output its given access ID followed by a list of locations
        in the protein string where the motif can be found'''

        for seqName in seqList:
                data = urllib.request.urlopen("http://www.uniprot.org/uniprot/" + seqName + '.fasta').read()
                data=data.split()
                aaSeq=getAA(data)
                indexSum=0
                motifFound=False
                motifList=[]
                for amino in aaSeq:
                        indexSum+=1
                        if 'N' is amino:
                                motifFound=checkMotif(aaSeq,indexSum)

                        if motifFound:
                                motifList.append(indexSum)
                                motifFound=False
                if motifList:                
                        print(seqName,'\n',*motifList)
                             
                                                
                                
def checkMotif(aaSeq,index):
        '''input: aa seq and index where N is found
        will look at subsequent residues and see if motif exists
        outputs: true if motif exists, false otherwise'''
        
        phenyl={'P'}
        polar={'S','T'}
        subSeq=aaSeq[index-1:index+3]

        if subSeq[1] not in phenyl and subSeq[2] in polar and subSeq[3] not in phenyl:

                return True
        else:
                return False
                
                

def getAA(webData):
        '''input: urllib web data from uniprot fasta page for protein seq name
        output: amino acid sequence from that page'''
        
        startPrinting=False
        aaSeq=''

        for line in webData:
                if b'SV=' in line:
                        startPrinting=True
                        continue
                if startPrinting:
                                
                                aaSeq+=str(line,encoding='utf-8')
                                
                if b'>sp' in line and startPrinting:
                        startPrinting=False
                        break
        return aaSeq.rstrip()

def fileOpen(f):
        
         '''input is an opened file,
        will read each file and separate ROSALIND seqs
        output is sequence name, sequence'''
         
         seq=''
         seqName=''
         seqList=list()
         firstPass=False
         
         for eachLine in f:
                 seqName=eachLine.rstrip()
                 seqList.append(seqName)
                 
         return(seqList)

def main():

        f=open('rosalind_mprt.txt','r')
        seqList=fileOpen(f)
        MPRT(seqList)

        x=MPRT(seqList)
 

        f.close()


if __name__=='__main__':
        main()
        


        
        

        
