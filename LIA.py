from sympy import binomial

def LIA(k,n):
        
        '''Input: Two positive integers k (k≤7) and N (N≤2k). In this problem,
        we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom
        has two children in the 1st generation, each of whom has two children, and
        so on. Each organism always mates with an organism having genotype Aa Bb.

        Output: The probability that at least N Aa Bb organisms will belong to the k-th
        generation of Tom's family tree (don't count the Aa Bb mates at each level).
        Assume that Mendel's second law holds for the factors.'''
        
        genNum=int(k)
        numOrg=int(n)
        totalOrg=2**k

        probHetero=0.25

        return binomial(totalOrg,numOrg)*(probHetero**numOrg)*((1-probHetero)**(totalOrg-numOrg))

def probLoop(k,num):
        
        '''input: k is number of gens, n is number of hetero offspring to find probability for
        finds probability for heterozygous offspring for at
        least number of n.
        essentially loops the LIA function to account for everything between
        n and 2**k'''

        return 1-(sum([LIA(k,n) for n in range(num)]))
        

        
        
                


k=5
num=7
print(round(probLoop(k,num),3))
