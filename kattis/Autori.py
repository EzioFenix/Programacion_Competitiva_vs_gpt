#	0.04 s
import sys

def main():
    inp=sys.stdin.readline()
    #separate=inp.split("-")
    total=inp[0]
    for i in range(len(inp)):
        if inp[i]=="-":
            total+=inp[i+1]
    sys.stdout.write(total)


if __name__=="__main__":
    main()