from collections import defaultdict

# Dictionary to keep track of songs played in a row
songs_in_a_row = defaultdict(int)

# Dictionary to keep track of artists for each song
artist_for_song = defaultdict(str)

# Minimum consecutive plays to consider
min_consecutive_plays = 5

# Read the file
with open('out.txt', 'r') as file:
    previous_song = None
    consecutive_count = 0
    current_artist = None

    for line in file:
        parts = line.strip().split(' - ')
        if len(parts) == 3:
            artist, song, timestamp = parts
            if song == previous_song:
                consecutive_count += 1
            else:
                consecutive_count = 1
            songs_in_a_row[song] = max(songs_in_a_row[song], consecutive_count)
            artist_for_song[song] = artist  # Track the artist for the song
            previous_song = song

# Find songs played at least min_consecutive_plays times in a row
songs_played_at_least_5_times = [song for song, count in songs_in_a_row.items() if count >= min_consecutive_plays]

# Sort songs by the number of times played in a row (from most to least)
sorted_songs = sorted(songs_played_at_least_5_times, key=lambda song: songs_in_a_row[song], reverse=True)

# Write the output to a file named "row.txt" with artist information
with open('row.txt', 'w') as output_file:
    for song in sorted_songs:
        output_file.write(f"{song} by {artist_for_song[song]}: {songs_in_a_row[song]} times in a row\n")




#top artist and tracks


# Dictionary to keep track of the total times each song was played
song_play_counts = defaultdict(int)
# Dictionary to keep track of the total times each artist was played
artist_play_counts = defaultdict(int)

# Read the file
with open('out.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(' - ')
        if len(parts) == 3:
            artist, song, timestamp = parts
            song_play_counts[song] += 1
            artist_play_counts[artist] += 1

# Sort songs by play count (from most to least)
sorted_tracks = sorted(song_play_counts, key=lambda song: song_play_counts[song], reverse=True)

# Write the top tracks to "top_tracks.txt"
with open('top_tracks.txt', 'w') as tracks_file:
    for song in sorted_tracks:
        tracks_file.write(f"{song} by {artist_for_song[song]}: {song_play_counts[song]} times played\n")

# Sort artists by the total number of plays
sorted_artists = sorted(artist_play_counts, key=lambda artist: artist_play_counts[artist], reverse=True)

# Write the top artists to "top_artists.txt"
with open('top_artists.txt', 'w') as artists_file:
    for artist in sorted_artists:
        artists_file.write(f"{artist}: {artist_play_counts[artist]} total plays\n")






import json

# List of file names
files = [
    "Streaming_History_Audio_2018-2020_0.json",
    "Streaming_History_Audio_2020_1.json",
    "Streaming_History_Audio_2020-2021_2.json",
    "Streaming_History_Audio_2021-2022_3.json",
    "Streaming_History_Audio_2022-2023_4.json",
    "Streaming_History_Audio_2023_5.json"
]

# Output file name
output_file = "history.json"

# Create an empty list to store all the JSON data
all_data = []

# Iterate through the list of files and read their contents
for file_name in files:
    with open(file_name, "r") as file:
        data = json.load(file)
        all_data.extend(data)

# Write all the data to the output file
with open(output_file, "w") as outfile:
    json.dump(all_data, outfile, indent=4)

print(f"Combined data from {len(files)} files into {output_file}")



#weighted by listening time top artists and tracks


# Input file containing history data
input_file = "history.json"

# Output files for top tracks and top artists
output_tracks_file = "top_tracks_weighted.txt"
output_artists_file = "top_artists_weighted.txt"

# Load data from the input JSON file
with open(input_file, "r") as file:
    data = json.load(file)

# Dictionary to store total listening time for each track
track_listening_time = defaultdict(int)

# Dictionary to store total listening time for each artist
artist_listening_time = defaultdict(int)

# Calculate total listening time for tracks and artists
for entry in data:
    track_name = entry["master_metadata_track_name"]
    artist_name = entry["master_metadata_album_artist_name"]
    listening_time = entry["ms_played"]  # Listening time in milliseconds
    track_listening_time[track_name] += listening_time
    artist_listening_time[artist_name] += listening_time

# Sort tracks and artists by listening time (from most to least)
sorted_tracks = sorted(track_listening_time, key=lambda track: track_listening_time[track], reverse=True)
sorted_artists = sorted(artist_listening_time, key=lambda artist: artist_listening_time[artist], reverse=True)

# Write top tracks to the output file
with open(output_tracks_file, "w") as tracks_file:
    for track in sorted_tracks:
        tracks_file.write(f"{track}: {track_listening_time[track]} ms listened\n")

# Write top artists to the output file
with open(output_artists_file, "w") as artists_file:
    for artist in sorted_artists:
        artists_file.write(f"{artist}: {artist_listening_time[artist]} ms listened\n")

print(f"Top tracks based on listening time written to {output_tracks_file}")
print(f"Top artists based on listening time written to {output_artists_file}")












