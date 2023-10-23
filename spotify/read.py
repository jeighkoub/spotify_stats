#from local json files, print only the master_metadata_album_artist_name and master_metadata_track_name
#print to .txt file

import json
import datetime
from datetime import datetime

#todo read from dir no hardcode
files = ["Streaming_History_Audio_2018-2020_0.json", "Streaming_History_Audio_2020_1.json", "Streaming_History_Audio_2020-2021_2.json",
         "Streaming_History_Audio_2021-2022_3.json", "Streaming_History_Audio_2022-2023_4.json", "Streaming_History_Audio_2023_5.json"]

with open("out.txt", 'w') as out:
    for file in files:
        print(file)
        with open(file, 'r') as f:
            data = json.load(f)
            #f.close()
        for element in data:
            if type(element["master_metadata_album_artist_name"]) is str:
                out.write(element['master_metadata_album_artist_name'])
            else:
                out.write("Unknown Artist")
            out.write(" - ")
            if type(element["master_metadata_track_name"]) is str:
                out.write(element['master_metadata_track_name'])
            else:
                out.write("Unknown Track")
            out.write(" - ")
            if type(element["ts"]) is str:
                out.write(datetime.strptime(element['ts'], "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y %I:%M:%S %p"))
            else:
                out.write("Unknown Date")
                print(element["ts"])





            out.write('\n')
#out.close()
print("done")