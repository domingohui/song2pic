from PIL import Image
import midi
from math import asin
import os

IMAGE_DIR = 'images'
for filename in os.listdir (IMAGE_DIR):
    if filename.endswith('.png'):

        print ('Openning %s' % filename)

        image = Image.open(os.path.join(IMAGE_DIR, filename))
        # Get pixel data
        data = image.getdata()

        # Instantitate pattern and track from midi
        pattern = midi.Pattern()
        track = midi.Track()
        pattern.append(track)

        for pixel in data:
            # (0,0) = upper left
            note = midi.NoteOnEvent ( tick = pixel[0], data = [pixel[1], pixel[2]] )
            track.append(note)
        eot = midi.EndOfTrackEvent(tick=1)
        track.append(eot)
        print (pattern)
        midi.write_midifile('midi_output/%s' % filename.replace('.png', '.mid'), pattern)
