from itertools import permutations
def PERM(n):
        '''input : an integer,n
        outputs total number of permutations of length n,
        as wekk as a list of all such permutations'''
        numWord=''
        numList=list(range(1,n+1))

        for num in numList:
                numWord+=str(num)
        factorial(n)
        permList=permutations(numWord)

        for item in permList:
                print(*item)
        #look at it as shuffling indices in a list
        
        
       

def factorial(n):
        totalNum=1
        if n>1:
                for num in range(2,n+1):
                        totalNum*=num
        print(totalNum)

n=6
PERM(n)


