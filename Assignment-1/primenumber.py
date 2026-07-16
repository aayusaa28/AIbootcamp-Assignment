x=int(input("Enter a number:\n"))
c=0
if(x==0):
    print("zero")
for i in range (1,x+1):
   if(x%i==0):
       c+=1
    
if(c==2):
    print(f"{x}number is prime")
else:
    print("number is composite")