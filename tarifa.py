import sys
def main():
    #inp=[10,3,4,6,2]
    gastados:int=0
    mb:int=int(sys.stdin.readline())
    meses:int=int(sys.stdin.readline())
    for i in range(meses):
        gastados+= int(sys.stdin.readline())

    restantes=mb*(meses+1)- gastados
    sys.stdout.write(str(restantes))


if __name__=="__main__":
    main()