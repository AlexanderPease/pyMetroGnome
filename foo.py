from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note
import os
from pprint import pprint
from random import randint
import pygame # Mixer
from pygame_player import play_music, init_player

#PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

def tutorial():
    notes1 = NoteSeq("D4 F#8 A Bb4")
    midi = Midi(1, tempo=60)
    midi.seq_notes(notes1, track=0)
    midi.write("demo.mid")

def foo():
    notes = NoteSeq("C4 D4")
    pprint(notes.verbose) #Value (1-12), Octave (default=5) and Duration
    
    note1 = Note("C4")
    pprint('Note1 verbose = ' + note1.verbose) #<NoteSeq: [<Note: 0, 5, 0.25>, <Note: 2, 5, 0.25>]>
    pprint('Note1 name = ' + note1.name)
    note1.midi_number
    note1.midi_dur

    note_blank = Note()
    pprint('Note_blank = ' + note_blank.verbose) #<Note: 0, 5, 0.25> (pitch, octave, duration)

    note = Note(2, 4, 1, 100) #Value, Octave, Duration, Volume
    pprint('Programmatic note = ' + note.verbose) #<Note: 1, 4, 1>
    pprint('Programmatic note name = ' + note.name)

    #notes = NoteSeq("D4 F#8 A Bb4")
    #note.harmonize(notes)

    scale = NoteSeq('G4')
    scale2 = NoteSeq('A4')
    scale += scale2
    pprint('Scale: ' + scale.verbose)

    Dmajor = [2,4,6,7,9,11,13,14]
    foolist = []
    for degree in Dmajor:
        foolist.append(Note(degree, 5, .25, 100))
    pprint(foolist)
    fooSeq = NoteSeq(foolist)
    pprint('List of notes in NoteSeq: ' + fooSeq.verbose) #[<Note: 3, 5, 1>, <Note: 4, 5, 1>, etc.]
    
    midi = Midi(1, tempo=60)
    midi.seq_notes(fooSeq, track=0)
    midi.write("foo.mid")
    
    seq2 = NoteSeq("C4 D8 E8 C4 D8 E8 C4 D8 E8")
    midi2 = Midi(1, tempo=60)
    midi2.seq_notes(seq2, track=0)
    midi2.write("foo1.mid")
    
    chord1 = NoteSeq("C E G")
    chord2 = NoteSeq("D F A")
    chord3 = NoteSeq("E G B")
    chord4 = NoteSeq("F A C")
    seqlist = [chord1, chord2, chord3, chord4]
    pprint(seqlist)
    midi3 = Midi(1, tempo=60)
    midi3.seq_chords(seqlist, track=0)
    midi3.write('foochord.mid')
    
#Script
foo()

# Pygame script
# pick a midi music file you have ...
# (if not in working folder use full path)
music_file = "foochord.mid"
init_player()
#play_music(music_file)
"""freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024    # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)
# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)
try:
    play_music(music_file)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit"""

#test = input("What is the note? ") #input python code
#pprint("Note is " + test)

pprint(PROJECT_ROOT)
