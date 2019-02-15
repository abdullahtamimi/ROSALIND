
def CORR(seqList,seqDict):

    '''input: list of DNA sequences, dictionary with seqs as key,
    and frequency as value
        output: a seq in the list of DNA sequences that contains
        a single nucleotide error matched along a corrected read
        also in the list of DNA seqs'''

            
    for seq in seqDict:
        
        revComp=REVC(seq)
        
        if seqDict[seq] == 0 and not seqDict[revComp] and seq in seqList:
            
            for nextSeq in seqDict:
                hamDist=0

                if seqDict[nextSeq] > 0 :
                    for nucA,nucB in zip(seq,nextSeq):
                        if nucA!= nucB:
                            hamDist+=1

                    if hamDist == 1:
                        print(seq+'->'+nextSeq)

                else:
                    continue

def seqFreq(seqList):

    '''input: a list of DNA sequences
       output: dictionary with sequences + rev complement
       and frequency of occurence of each'''
    
    seqDict=dict()

    for eachSeq in seqList:

        revComp=REVC(eachSeq)
                
        if eachSeq not in seqDict:
            
            seqDict[eachSeq]=0
            
            if revComp not in seqDict:
                seqDict[revComp]=0
                
            else:
                seqDict[revComp]+=1
                
        else:
            
            seqDict[eachSeq]+=1

            if revComp in seqDict:
                seqDict[revComp]+=1
            else:
                seqDict[revComp]=0
                
    return seqDict
    


def REVC(s):
    '''input: a DNA string
    output: reverse complement DNA string'''
    
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
                
    return reverse
    
def fileOpen(file):

    '''input: opened file containing seqs in FASTA format
    output: dictionary of seqs + rev seqs'''

    seq=''
    seqList=list()

    for eachLine in file:

        if eachLine.startswith('>'):
            seq=''
            continue
        
        seq=eachLine.strip()
        seqList.append(seq)

    return seqList



def main():
    
    f=open('rosalind_corr.txt','r')
    x=fileOpen(f)
    seqDict=seqFreq(x)

    CORR(x,seqDict)
    f.close()


if __name__== '__main__':
    main()
