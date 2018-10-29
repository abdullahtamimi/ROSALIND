#generate list of all sequences
#compare two seqs against eachother
#when comparing, look at subseq of first seq, and see
#subseq is half the size
#if secondseq starts with or ends with subseq
#if it doesn't, shorten the length of the subseq by 25%
#if it does, increase the length by 25% and see if it is still in it

#if it isnt in it after shortening the length, its not in it, move to next sequence to compare substrings in
#if it is and still is after lengthing, continue to lengthen until it doesnt match anymore, then titrate down by 1 or by 12.5%

#for subseqs found, add to dictionary, with key being prefix seq, and value being suffix seq


def ORF(s):
        
        '''Input: DNA String, s of length at most 1 kbp in FASTA format.,
        Output: Every distinct candidate protein string that can be translated
        from ORFs of s. Strings can be returned in any order.'''

        codonDict={'UUU':'F','CUU':'L','AUU':'I','GUU':'V',
                   'UUC':'F','CUC':'L','AUC':'I','GUC':'V',
                   'UUA':'L','CUA':'L','AUA':'I','GUA':'V',
                   'UUG':'L','CUG':'L','AUG':'M','GUG':'V',
                   'UCU':'S','CCU':'P','ACU':'T','GCU':'A',
                   'UCC':'S','CCC':'P','ACC':'T','GCC':'A',
                   'UCA':'S','CCA':'P','ACA':'T','GCA':'A',
                   'UCG':'S','CCG':'P','ACG':'T','GCG':'A',
                   'UAU':'Y','CAU':'H','AAU':'N','GAU':'D',
                   'UAC':'Y','CAC':'H','AAC':'N','GAC':'D',
                   'UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E',
                   'UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E',
                   'UGU':'C','CGU':'R','AGU':'S','GGU':'G',
                   'UGC':'C','CGC':'R','AGC':'S','GGC':'G',
                   'UGA':'Stop','CGA':'R','AGA':'R','GGA':'G',
                   'UGG':'W','CGG':'R','AGG':'R','GGG':'G'}
        s=RNA(s)
        
        protSet=set()
        seqLength=len(s)
        stopCodons = {'UAA', 'UAG', 'UGA'}
        startCodons={'AUG'}
                
        protSeq=''
        startFound=False

        for triplet in range(0,seqLength-2,3):
                        
                codon=s[triplet:triplet+3]
                        
                if codon in startCodons:
                        startFound=True

                if startFound and codon not in stopCodons:
                        protSeq+=codonDict[codon]

                if codon in stopCodons and startFound:
                        protSet.add(protSeq)
                        protSeq=''
                        startFound=False
                                
                                                           
        return protSet


def SPLC(s):
        
        '''Input: a collection of s DNA strings and intron substrings
        removes intron subseqs, translates to protein seq
        Output: a protein string'''

        firstItem=False
        for item in s:
                
                if not firstItem:
                        mainSeq=item
                        firstItem=True
                        continue
                if firstItem:
                        intronPos=mainSeq.find(item)
                        intronLength=len(item)
                        mainSeq=mainSeq[0:intronPos]+mainSeq[intronPos+intronLength:]
        return(mainSeq)
        
def RNA(s):
        '''input: DNA String
        output: RNA version of DNA string'''
        rnaTranslate=''
       
        for item in s:
                item=item.upper()

                if item == 'A':
                        rnaTranslate+=item
                if item == 'C':
                        rnaTranslate+=item
                if item == 'G':
                        rnaTranslate+=item
                if item == 'T':
                        rnaTranslate+='U'
        return(rnaTranslate)       

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

        f=open('rosalind_splc.txt','r')
        seqList=fileOpen(f)
        x=SPLC(seqList)
        print(ORF(x))
 

        f.close()


if __name__=='__main__':
        main()
        


        
        

        
