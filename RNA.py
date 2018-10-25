


def RNA(s):
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
        print(rnaTranslate)
       # return(aCount,cCount,gCount, tCount)





def main():
        RNA(s)


if __name__== '__main__':
        main()
