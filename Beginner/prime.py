subi = int(input(" "))  
if (subi > 1):  
   for i in range(2,subi):  
       if (subi % i) == 0:  
           print("no")  
           break  
   else:  
       print("yes")  
         
else:  
   print("no")
