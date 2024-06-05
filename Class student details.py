class Student:
    def __init__(self,name,usn):
        self.name=name
        self.usn=usn
        self.marks=[]
        self.total_marks=0
        self.percentage=0.0
    def getMarks(self):
        for i in range(3):
            mark=float(input(f"Enter marks for subject{i+1}:"))
            self.marks.append(mark)
            self.total_marks+=mark
        self.percentage=self.total_marks/3
    def display(self):
        print("----Scorecard----")
        print("Name:",self.name)
        print("USN:",self.usn)
        print("Marks:",self.marks)
        print("Total Marks:",self.total_marks)
        print("Percetage:",self.percentage)
name=input("Enter Student name:")
usn=input("Enter student USN:")
student=Student(name,usn)
student.getMarks()
student.display()
