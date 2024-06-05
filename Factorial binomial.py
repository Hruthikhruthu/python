num=int(input("Enter the value of num:"))
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
n=int(input("Enter the value of N:"))
r=int(input("Enter the value of R(R cannot be negative or greater than N):"))
bc=fact(n)/(fact(r)*fact(n-r))
print("The binomial coefficient is",bc)
result=fact(num)
print("Factorial of ",num,"is",result)
