#!/usr/bin/env python
import midi
from PIL import Image
from math import floor, sqrt, sin
import os, sys

def __usage ():
    print('Usage: index.py [option]')
    print('Available option: -TO_PNG, -TO_MIDI')
    sys.exit()

if len(sys.argv) <= 1:
    __usage()
    
if sys.argv[1] == '-TO_PNG':
    for filename in os.listdir('music'):
        if filename.endswith('.mid'):
            pattern = midi.read_midifile('music/%s' % filename)
    
            notes = []
    
            for a in pattern:
                for b in a:
                    if "Note" in str(b):
                        notes.append(b)
    
            size = int(floor(sqrt(len(notes))))
    
            im = Image.new("RGB", (size, size), "white")
    
            for i in range(size):
                for j in range(size):
                    note = notes[i * size + j]
                    im.putpixel((i, j), (int(abs(sin(note.tick)) * 255), int(abs(sin(note.data[0])) * 255), int(abs(sin(note.data[1])) * 255)))
    
            im.save('images/%s' % filename.replace('.mid', '.png'), 'PNG')
elif sys.argv[1] == '-TO_MIDI':
##
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
else:
    __usage()
