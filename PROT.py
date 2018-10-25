
def PROT(s):
        
        '''Input: An RNA string s corresponding to a
        strand of mRNA (of length at most 10 kbp).
        Output: The protein string encoded by s.'''

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
        s=str(s)
        seqLength=len(s)
        aaSeq=''

        for i in range(0,seqLength-2,3):
                codon=s[i:i+3]
                aaSeq+=codonDict[codon]
                if codonDict[codon] == 'Stop':
                        print(aaSeq.rstrip('Stop'))

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

f=open('rosalind_prot.txt','r')
s=fileOpen(f)
PROT(s)
