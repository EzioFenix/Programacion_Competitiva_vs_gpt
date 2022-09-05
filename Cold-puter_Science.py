import sys
def main():
    num=int(sys.stdin.readline())
    inp=sys.stdin.readline()
    inp=inp.split()
    res=0
    for i in range(num):
        res+=int(inp[i]<"0")

    sys.stdout.write(str(res))

if __name__=="__main__":
    main()