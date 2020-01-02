print("TUPLES")
print("Tuples can be defined with or without brackets.")

print()

tupleWithBracket = ("a", "b", "c")
tupleWithOutBracket = "a", "b", "c"
print(f"tupleWithOutBracket == tupleWithBracket: {tupleWithOutBracket == tupleWithBracket}")

print()

print(f"tupleWithBracket[0]: {tupleWithBracket[0]}")
print("Using for loop with tuples")
for item in tupleWithBracket:
    print(item)

print()

print("Tuples are like Lists but are IMMUTABLE")
print("We cant change any element in tuple. Doing 'tupleWithBracket[0] = d' will result in error")
# tupleWithBracket[0] = 'd'
print("We can however point tuple variable to new tuples as below")
tupleWithBracket = tupleWithBracket[0], 'd', tupleWithBracket[2]
print(f"tupleWithBracket = tupleWithBracket[0], \"d\", tupleWithBracket[2]: {tupleWithBracket}")

print()

print("Like lists, Tuples can also have different data types as its elements.")
tuples2 = "a", "b", "c", 4, 6, 10.4, True
print("Tuple with different data type {}". format(tuples2))

print()

metallica = "Metallica", "Nothing Else Matters", 1991
nirvana = "Nevermind", "Come As You Are", 1991
gunNRoses = "Use Your Illusion I", "November Rain", 1991
eagle = "Live @ Summit", "Hotel California", 1976

print("Metallica: {}".format(metallica))
print("In {}, Metallica released an album named {}, with {} song".format(metallica[2], metallica[0], metallica[1]))

print()

print("As we know we can assign multiple variable at same time, so we will assigns different elements of tuple to "
      "different variable at same time using:\n\"variable1, variable2, variable3, ..., variableN = tupleVariable\"\n"
      "where N is total number of element in tuple")
album, song, year = metallica
print("When using this element \"album, song, year = metallica\", we get")
print(f"album: {album}, song: {song}, year: {year}")
print("However it is important to note that number of varibles should be exactly equal to number of elements that "
      "tuple has else we will get an error")

print()

print("Similar to list, tuples can also be nested. We can have a list in tuple and also a tuples in tuple")
print("TUPLE IN TUPLE")
scorpions = "Love At First Sting", "Scorpions", 1984, (
    (1, "Bad Apples"), (2, "November Rain"), (3, "Right Next Door to Hell"), (4, "Bad Obsession")
)
album, artist, year, tracks = scorpions
print(f"album: {album}\nartist: {artist}\nyear: {year}\ntracks: {tracks}")
track1, track2, track3, track4 = tracks
print(f"Album: {album}\nArtist: {artist}\nYear: {year}")
for track in tracks:
    print("\tSong # {} is {}".format(track[0], track[1]))
print("Other way of printing tuple in for loop")
for song in tracks:
    track, title = song
    print("\tSong # {} is {}".format(track, title))

print()
print("TUPLE IN TUPLE")
alphabets = ("a", "b", "c", "d", ("d", "e", "f"), ["g", "h", "i"])
print("alphabets tuple before appending to list{}".format(alphabets))
alphabets[5].append("j")
print("alphabets tuple after appending to list{}".format(alphabets))
