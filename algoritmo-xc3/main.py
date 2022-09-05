def main():
    inp=decBin(117)
    inp=xc3(inp)

    


def decBin(dec:int)->str:
    return bin(10)[2:]

def mas3(bi:str)->str:
    return bin(int(bi,2) + 0b11)[2:] # 0b1000=> 1000

def xc3(bi:str)->str:
    bi=[*bi] # separar por letras
    resultado=[0]
    nib0=resultado[0:4] # 0-3 Acuerdate que el 5 no se incluye
    nib1=resultado[4:8] # 4-7
    nib2=resultado[8:10]# 8-9

    f=0
    # calculamos por cada bit
    for i in range(len(bi),0,-1):
        bit=bi[f]
        f+=1
        print(bit)
        resultado[i]=bit

        if (nib0)>"1001":
            nib0=mas3(nib0)
        if (nib1)>"1001":
            nib1=mas3(nib1)
        if (nib2)>"1001":
            nib2=mas3(nib2)

    print(resultado)

main()