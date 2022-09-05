import sys
def main():
    inp=sys.stdin.readline()
    inp=inp.split(" ")
    inp=int(inp[0])+ int(inp[1])
    sys.stdout.write(str(inp))


if __name__== "__main__":
    main()