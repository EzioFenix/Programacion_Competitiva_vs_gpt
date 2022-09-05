import sys
def main():
    inp:int=int(sys.stdin.readline()) #Number of input
    especial:bool= inp<100
    residuo=99-(inp % 100)
    if residuo<=50 or especial:
        inp+=residuo
        sys.stdout.write(str(inp))
    else:
        sys.stdout.write(str(inp-(inp%100)-1))


if __name__=="__main__":
    main()