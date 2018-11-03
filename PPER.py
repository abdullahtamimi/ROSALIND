
def PPER(n,k):
        
        '''Input: positive integers n,k
        
        Output: total number of partial permutations P(n,k)
        mod 1,000,000.'''

        permSum=1

        for i in range(n-k+1,n+1):
                permSum*=i
                
        return(permSum%1000000)




def main():
        
        n=99
        k=10
        print(PPER(n,k))

if __name__=='__main__':
        main()
