import os

with os.scandir('/path/to/direcory') as entries:
    for entry in entries:
        print (entry.name)