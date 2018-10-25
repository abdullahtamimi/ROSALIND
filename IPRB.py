
def IPRB(k,m,n):
        
        '''Three positive integers k, m, and n, representing
        a population containing k+m+n organisms: k individuals
        are homozygous dominant for a factor, m are heterozygous,
        and n are homozygous recessive.
        Output: The probability that two randomly selected mating
        organisms will produce an individual possessing a dominant allele
        (and thus displaying the dominant phenotype). Assume that any two organisms
        can mate'''

        k=float(k)
        m=float(m)
        n=float(n)
        totalOrgs=k+m+n

        p=[k*(k-1),k*m,k*n,
          m*k,m*(m-1)*0.75,m*n*0.5,
          n*k,n*m*0.5,n*(n-1)*0]

        prob=(sum(p)/totalOrgs)/(totalOrgs-1)

        return prob

k=20
m=18
n=21

print(round(IPRB(k,m,n),5))
