
file=open('test.txt')
# read all contents of files
#read n number of characters by passing parameter
#print(file.read(5))
#read  one single line from file

#print(file.readline())

line = file.readlines()
while line!="":
     print(line)
     line=file.readline()

#file.close()

# print line by line from using redLine mathod



