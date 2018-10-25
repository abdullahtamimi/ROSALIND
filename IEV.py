
def IEV(i):
        
        '''Input:Six nonnegative integers, each of which does not exceed 20,000.
        The integers correspond to the number of couples in a population possessing
        each genotype pairing for a given factor. In order, the six given integers
        represent the number of couples having the following genotypes:

        AA-AA
        AA-Aa
        AA-aa
        Aa-Aa
        Aa-aa
        aa-aa
        
        Output: The expected number of offspring displaying the dominant phenotype
        in the next generation, under the assumption that every couple has exactly
        two offspring.'''
        
        i=i.rstrip()
        intList=i.split(' ')
        domSum=0
        

        p=[1,1,1,0.75,0.5,0]

        for i in range(0,6):
                domSum+=int(intList[i])*2*p[i]
        print(domSum)
                
                



i='16163 17550 18132 18199 19742 19347'
IEV(i)
