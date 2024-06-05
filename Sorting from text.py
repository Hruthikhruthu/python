import os.path
import sys
fname=input("Enter the file name whose contents are to be sorted:")#samplefile.unsorted.txtalsoprovided
if not os.path.isfile(fname):
    print("File",fname,"dosent exists")
    sys.exit(0)
infile=open(fname,"r")
myList=infile.readlines()
#print(mylist)
#Remove trailing\n characters
lineList=[]
for line in myList:
    lineList.append(line.strip())
lineList.sort()
outfile=open("sorted.txt","w")
for line in lineList:
    outfile.write(line+"\n")
infile.close()#close the input file
outfile.close()#close the outfile
if os.path.isfile("sorted.txt"):
    print("\nFile containing sorted content sorted.txt created successfully")
    print("sorted.txt contains",len(lineList),"lines")
    print("contents of sorted.txt")
    print("===========================")
    rdFile=open("sorted.txt","r")
    for line in rdFile:
        print(line,end="")
    
