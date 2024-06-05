num=int(input("Enter the fibonacci sequence lenght to be generated:"))
firstTerm=0
secondTerm=1
print("The Fibonacci series with",num,"term is:")
print(firstTerm,secondTerm,end=" ")
for i in range(2,num):
    curTerm=firstTerm+secondTerm
    print(curTerm,end=" ")
    firstTerm=secondTerm
    secondTerm=curTerm
print()    
