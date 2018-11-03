


def FIBD(n,m):
        
        '''input : n=num months, m = rabbit lifespan
        output: number of rabbit pairs (baby and mature)
        present after n months of breeding, given
        we start with 1 pair, and that rabbits
        reach sexual maturity after one month of life, and they breed
        every month, make 1 baby'''

        rabAge=[0]*m
        rabAge[0]=1

        for i in range(n-1):

                newRab=sum(rabAge[1:])

                rabAge= [newRab]+rabAge[0:m-1]

        return(sum(rabAge))
       
                

print(FIBD(80,19))
       
