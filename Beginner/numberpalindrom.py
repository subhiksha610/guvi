subi=int(input(" "))
t=subi
reverse=0
while(subi>0):
    num=subi%10
    reverse=reverse*10+num
    subi=subi//10
if(t==reverse):
    print("yes")
else:
    print("no")
