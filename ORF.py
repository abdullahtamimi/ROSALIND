

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
        
        protSet=set()
        seqLength=len(s)
        stopCodons = {'UAA', 'UAG', 'UGA'}
        startCodons={'AUG'}

        for readingFrame in range(3):
                
                protSeq=''
                startFound=False

                for triplet in range(readingFrame,seqLength-2,3):
                        
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


def seqPasser(s):
        
        '''input: DNA sequence
        will generate forward mRNA strand and reverse mRNA strand,
        pass them to ORF function and store found protein seqs in a list.
        Outputs a set all protein seqs found'''
        
        revS=REVC(s)
        s=RNA(s)
        
        revS=RNA(revS)
        seqList=[s,revS]
        seqSet=set()
        for item in seqList:

                x=ORF(item)
                
                for aaSeq in x:
                        if aaSeq is '':
                                pass
                        else:
                                seqSet.add(aaSeq)
        return seqSet

def multipleStart(seq,secProtSet):
        
        '''input is a amino acid sequence, and a set for data storage
        whill check for multiple methionine residues, and identify all
        ORF substrings in an aa chain
        output is a set containing all ORF substrings'''
        
        if len(seq)>1:
                
                newSeq=seq[1:]
                findStart=newSeq.find('M')
                
                if findStart is not -1 or None:


                        secProt=newSeq[newSeq.find('M'):]
                        
                        if secProt is not -1 or None:
                                secProtSet.add(secProt)
                                nextProt=secProt[1:]

                        if nextProt.find('M') is not -1 or None:
                                multipleStart(secProt,secProtSet)
                        else:
                                return secProtSet
                        return secProtSet

       
                                              
def REVC(s):
        '''input is a DNA string
        output is the reverse complement of that string'''
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

        return(seq)

def RNA(s):
        '''input is DNA string
        output is RNA translation of that string'''
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

def main():
        
        f=open('rosalind_orf.txt','r')

        s=fileOpen(f)

        proteinSet=seqPasser(s)

        secondSet=set()
        secProtSet=set()

        for seq in proteinSet:
                secondSet.add(seq)
                subSeqSet=multipleStart(seq,secProtSet)

                if subSeqSet is not None:
                        for subSeq in subSeqSet:
                
                                secondSet.add(subSeq)

        for item in secondSet:
                print(item)


        f.close()

if __name__=='__main__':
        main()
