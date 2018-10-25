
def GC(s):
        '''opens a file containing fastA style ROSALIND headers and sequences
        parses through all, calculates GC content and prints sequence name
        and GC Percentage for highest one'''
        
        firstPass=False
        highestGC=0
        heaviestSeq=''
        percentGC=0
        gcDict=dict()
        for eachLine in s:
                
                if eachLine.startswith('>'):
                        
                        if firstPass:
                                percentGc=gcCount/seqLength*100
                                if percentGc>highestGC:
                                        highestGC=percentGc
                                        heaviestSeq=seqName
                                        print(heaviestSeq,'\n',percentGc)
                        gcCount=0
                        seqLength=0
                        seqName=eachLine[1:14]
                        gcDict[seqName]=''
                        firstPass=True
                        continue
                      
                for nuc in eachLine:
                        if nuc in {'A','G','C','T'}:
                                seqLength+=1
                        if nuc in {'G','C'}:
                                gcCount+=1

        percentGc=gcCount/seqLength*100
        if percentGc>highestGC:
                highestGC=percentGc
                heaviestSeq=seqName
                print(heaviestSeq,'\n',percentGc)

f=open('rosalind_gc.txt','r')
GC(f)
