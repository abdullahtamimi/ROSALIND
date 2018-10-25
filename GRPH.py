
def GRPH(s,k):
        '''opens a file containing fastA style ROSALIND headers and sequences
        parses through all, adds sequences to a dict with seq name as key, seq as val
        looks at first/last k-mer and finds overlap sequences
        outputs these overlaps together, in the right direction'''
        
        firstPass=False
        seqDict=dict()
        seq=''
        grphSet=set()
        
        for eachLine in f:
                if eachLine.startswith('>'):
                        if firstPass:
                                seqDict[seqHeader]=seq
                        seq=''
                        seqHeader=eachLine[1:14]
                        seqDict[seqHeader]=''
                        firstPass=True
                        continue
                seq+=eachLine
        seqDict[seqHeader]=seq

        for keyA in seqDict:
                seqA=seqDict[keyA].rstrip()
                seqALen=len(seqA)
                seqAStart=seqA[0:k]
                seqAEnd=seqA[seqALen-k:seqALen]

                for keyB in seqDict:
                        if keyA != keyB:
                                seqB=seqDict[keyB].rstrip()
                                seqBLen=len(seqB)
                                seqBStart=seqB[0:k]
                                seqBEnd=seqB[seqBLen-k:seqBLen]
                                if seqAStart in seqBEnd :
                                        grphSet.add(keyB+'%'+keyA)
                                if seqBStart in seqAEnd:
                                        grphSet.add(keyA+'%'+keyB)

        for item in grphSet:
                item=item.split('%')
                print(*item)
                                


f=open('rosalind_grph.txt','r')
GRPH(f,3)
