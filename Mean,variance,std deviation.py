import statistics
a=list()
number=int(input("enter the number of elements you want:"))
print("enter the number in array:")
for i in range(int(number)):
    n=input("number:")
    a.append(int(n))
print("given n number:")
print(a)
m=statistics.mean(a)
v=statistics.variance(a)
st=statistics.stdev(a)
print("Mean=",m)
print("Variance=",v)
print("Standard deviation=",st)
