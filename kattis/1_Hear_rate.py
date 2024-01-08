import sys

def calculate(b,p):
    bpmMax= (60 * (b+1))/p
    bpmMin= (60 * (b-1))/p
    mid=(bpmMax-bpmMin)/2 +bpmMin

    return (bpmMin,mid,bpmMax)

def main():
    cases=int(sys.stdin.readline().strip())

    for i in range(cases):
        b,p=sys.stdin.readline().strip().split()
        min,mid,max=calculate(int(b),float(p))
        print(f"{min:.4f} {mid:.4f} {max:.4f}\n")


if __name__=="__main__":
    main()