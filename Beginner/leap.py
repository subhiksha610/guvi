subi=int(input(" "))
if subi%4==0 and subi%100!=0:
    print("yes")
elif subi%100==0:
    print("no")
elif subi%400==0:
    print("yes")
else:
    print("no")
