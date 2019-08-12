def subi(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*subi(base,exp-1))
base=int(input(" "))
exp=int(input(" "))
print(subi(base,exp))
