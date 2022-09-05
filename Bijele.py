from posixpath import split
import sys
def main():
    inp=sys.stdin.readline()
    inp=inp.split(" ")
    piezas=(1,1,2,2,2,8)
    resultado:list[int]=[]

    for i in range(len(piezas)):
        resultado.append(str(piezas[i]-int(inp[i])))

    sys.stdout.write(" ".join(resultado))

if __name__=="__main__":
    main()