print("Append")
countries = ["Canada", "China", "Japan", "Russia", "Turkey", "South Africa"]

# To append text to existing file, we use open(). 1st parameter is the path of the location of the file and
# 2nd parameter('a') indicates that this is an append action.
# 'with' keyword here is very important as it closes file which we have opened as soon as we move out of with block
# the method of writing and appending to a file is same with the only difference being the 2nd parameter of the
# open function. Writing as 'w' whereas append has 'a'
# If the file with same name exist at same location then it will be over written with the new one.
with open('FileIO_Write_Sample.txt', 'a') as appendFile:
    for country in countries:
        print(country, file=appendFile)

# reading appended file
with open('FileIO_Write_Sample.txt', 'r') as readFile:
    country = readFile.readlines()
    for name in country:
        print(name.strip('\n'))
