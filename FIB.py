


def FIB(n,k):
        
        '''input : n=num months, k = rabbit pairs
        output: number of rabbit pairs (baby and mature)
        present after k months of breeding, given
        we start with 1 pair, and that rabbits
        reach sexual maturity after one month of life, and they breed
        every month'''

        if n==1:
                return 1
        if n==2:
                return 1
        else:
                return FIB(n-2,k)*k+FIB(n-1,k)
       
                




print(FIB(90,1))
       
