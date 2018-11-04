import math

def PROB(s,a):

    '''input: A DNA string s of at most 100bp and an array A containing up to
    20 numbers between 0 and 1
       output: an array B having the same length as A, in which B[k]
       represents the common log of the probability that a random string
       constructed with the GC content found in A[k] will match s exactly'''

    seqLen=len(s)
    gcCount=s.count('G') + s.count('C')
    
    atCount=seqLen-gcCount
    b=[]
    
    for prob in a:
        
        gcProb=((float(prob))/2)**(gcCount)
        atProb=((1-float(prob))/2)**(atCount)
        probLog=math.log10(gcProb*atProb)
        b.append(round(probLog,3))

    return b
        
            
    



def fileOpen(f):

    '''input: an opened file
    output: a DNA string s and a string array A'''

    seq=''

    firstPass=False
    
    for eachLine in f:

        if not firstPass:
            seq=eachLine.strip()
            firstPass=True
            continue

        if firstPass:
            A=eachLine.split(' ')

    return seq, A


def main():

    f=open('rosalind_prob.txt','r')
    s,a=fileOpen(f)
    b=PROB(s,a)

    print(*b)    
    f.close()

if __name__=='__main__':
    main()

        
