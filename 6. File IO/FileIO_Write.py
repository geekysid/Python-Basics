print("WRITE")
countries = ["India", "USA", "England", "Germany", "Spain", "France", "Australia"]

# To read an file, we use open(). 1st parameter is the path of the location of the file and 2nd parameter indicates
# that this is a write only action.
# 'with' keyword here is very important as it closes file which we have opened as soon as we move out of with block
# If the file with same name exist at same location then it will be over written with the new one.
with open('FileIO_Write_Sample.txt', 'w') as writeFile:
    for country in countries:
        print(country, file=writeFile)  # print functions has 2 parameters. 1st parameter is the content which is added
        # to the file and 2nd parameter is the name of the file to which the content is to be written file is the
        # name of the file to which the content is to be written

# trying to read the file which we have just written and printing its content on console.
countries = []
with open('FileIO_Write_Sample.txt', 'r') as readFile:  # reading file
    line = readFile.readlines()     # fetching all content of file as a list of each line of file

    for country in line:    # executing through the list
        countries.append(country.strip('\n'))

print(countries)
for country in countries:
    print(country)

print()
print("=*" * 40)
print()

# It is important to realize that no matter what we add to the file, list, tuple, dictionary etc, it is always
# written as a string and whenever we fetch the data, we always gets string.
# Python has a function eval() which we can apply on teh content fetched from file and returns the best matched data
# type as we will see below.

# Tuple which will be added to file
scorpions = "Love At First Sting", "Scorpions", 1984, (
    (1, "Bad Apples"), (2, "November Rain"), (3, "Right Next Door to Hell"), (4, "Bad Obsession"))
with open('FileIO_Write_Sample2.txt', 'w') as music:    # opening file in which tuple will be added
    print(scorpions, file=music)    # tuple added to the file
with open('FileIO_Write_Sample2.txt', 'r') as music:    # opening file to fetch tuple
    tracks = music.readline()   # tuple fetched as string
    scorpions = eval(tracks)    # using eval() function to convert string into tuple.

print(scorpions)    # printing tuple to console.
album, singer, year, tracks = scorpions
print(album)
print(singer)
print(year)
print(tracks)
