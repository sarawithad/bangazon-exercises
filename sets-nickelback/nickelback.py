# Instructions

# Define a set that contains tuples. Each tuple should contain two strings:
# The name of an artist
# A song by that artist
# Make sure that some of the songs are from the band Nickelback. You can see a list of their greatest hits on Amazon.

songs = {
    ("Karen Elson", "Distant Shore"), 
    ("Grateful Dead", "Sugar Magnolia"),
    ("Nickelback", "Photograph"),
    ("Ryan Adams", "Rosebud"),
    ("Nickelback", "How You Remind Me")
}
# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

good_songs = [artist for artist in songs if artist[0] != "Nickelback"]
print(good_songs)

