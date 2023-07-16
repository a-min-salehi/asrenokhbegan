import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('music.xml')
root = tree.getroot()

want = input("Enter the name of singer:").title()

# Extract and display album details
for album in root.findall('album'):
    title = album.find('title').text
    artist = album.find('artist').text
    genre = album.find('genre').text
    year = album.find('year').text

    if artist == want:
        print(f"Album: {title}")
        print(f"Artist: {artist}")
        print(f"Genre: {genre}")
        print(f"Year: {year}")
        tracks = [track.text for track in album.findall('tracks/track')]
        print("Tracks:")
        for track in tracks:
            print(track)
    
        print()
