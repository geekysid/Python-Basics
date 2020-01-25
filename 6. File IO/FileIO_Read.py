print("readLine()")
print("==========")
# To read an file, we use open(). 1st parameter is the path of the location of the file and 2nd parameter indicates
# that this is a read only action.
# 'with' keyword here is very important as it closes file which we have opened as soon as we move out of with block
with open('FileIO_Read_Sample.txt', 'r') as readFile:
    line = readFile.readline()      # readline() reads and returns one line at a time as a Strings
    while line:
        print(line.strip('\n'))
        line = readFile.readline()  # on next call of readline() it reads and return next line
print("=*" * 20)

print()

print("readLines()")
print("==========")
# readLines() returns all the lines in the form of list
with open('FileIO_Read_Sample.txt', 'r') as readFile:
    lines = readFile.readlines()
    print(lines)
    for line in lines:
        print(line.strip('\n'))

print("=*" * 20)

print()

print("read()")
print("==========")
# read() returns entire text in file as a string
with open('FileIO_Read_Sample.txt', 'r') as readFile:
    text = readFile.read()
    print(text)

print()
