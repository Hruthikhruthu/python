class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,other):
        real=self.real+other.real
        imaginary=self.imaginary+other.imaginary
        return Complex(real,imaginary)
def read_complex_numbers(n):
    complex_numbers=[]
    for i in range(n):
        print(f"Enter complex number{i+1}:")
        real=float(input("Real part:"))
        imaginary=float(input("Imaginary part:"))
        complex_numbers.append(Complex(real,imaginary))
    return complex_numbers
def compute_sum(complex_numbers):
   result=Complex(0,0)
   for num in complex_numbers:
       result+=num
   return result
n=int(input("Enter the number of complexnumbers(N):"))
numbers=read_complex_numbers(n)
sum_of_numbers=compute_sum(numbers)
print(f"The sum of the complex number is:{sum_of_numbers.real}+{sum_of_numbers.imaginary}i")





    
            
