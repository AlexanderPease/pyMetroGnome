import pygame_player as player
from pyknon.music import Note, Rest, NoteSeq #rename NoteSeq to Chord?
from pyknon.genmidi import Midi
from random import randint, choice
from pprint import pprint
import constants

# Writes array of Notes or NoteSeqs to a midi file
# Works by turning any Notes into a NoteSeq then calling write_midi_chord()
def write_midi(arg_notes, file_name='temp.mid', tempo=60):
    # Rebuild the list. This changes all Note objects to NoteSeq objects 
    write_notes = []
    for note in arg_notes:
        if isinstance(note, Note):
            next_entry = NoteSeq([note])
        elif isinstance(note, NoteSeq):
            next_entry = note
        else:
            print 'write_midi: Attempting to write non-Note or NoteSeq object to midi'
            raise 
        write_notes.append(next_entry)

    midi = Midi(1, tempo)
    midi.seq_chords(write_notes, track=0)
    midi.write(file_name) 

# Checks for var == answer
def correct_boolean_response(var, answer=True):
    truelist = ['True', 'T', 't', 'Yes', 'Y', 'yes', 'y']
    if var == True or var == 1 or var in truelist:
        var = True
    else:
        var = False
    return var == answer

# Returns a random Note object from integers in List note_list, 
# excluding integers in List exception_list
def random_note(note_list=None, exception_list=None):
    # If no note list, assume all notes
    if not note_list:
        note_list = list(range(0, 12, 1)) # default to all notes

    # Remove exception notes
    if exception_list and exception_list != note_list:
        for note in exception_list:
            note_list.remove(note)
    
    # Pick random note
    max_index = len(note_list) 
    rand = randint(0,max_index-1)
    return Note(rand, 5, 1, 100) # whole note, default octave and volume

# Returns a random chord (list of notes) but NOT a NoteSeq object
# If unspecified, hardcoded other_notes to min,max of 1,6
def random_chord(note_list=None, exception_list=None, other_notes=None): #FIX TO NOTESEQ?
    if not other_notes and not other_notes == 0:
        max_num = 6
        min_num = 1
        other_notes = randint(min_num,max_num-1)
    chord = [ ]
    for i in range(0,other_notes):
        other_note = random_note(note_list, exception_list)
        chord.append(other_note)
    return chord


# Executable ear training tests
#########################################################
# Plays a single pitch in note_list and asks you to name it
def test_single_pitch(note_list=None):
    note = random_note(note_list)
    notes = NoteSeq([note])
    write_midi_notes(notes)
    player.play_music()

    response = input("What is the note? ")
    if response == note.name:
        print("Correct!")
    else:
        print("The note was " + note.name)

# Plays a single pitch in note_list, then plays a chord
# that may or may not contain the tone. The pitch appears
# 50% of the time. 
def test_single_pitch_in_chord(note_list=None, other_notes=1):
    # Play initial note
    note = random_note(note_list)
    notes = NoteSeq([note])
    write_midi_notes(notes)
    player.play_music()
   
    # Pick other notes
    chord = random_chord(note_list, exception_list=[note.value])
    '''chord = [ ]
    for i in range(0,other_notes):
        other_note = random_note(note_list, exception_list=[note.value])
        chord.append(other_note)
    '''

    # True or False? To include original note
    boolean = choice([True, False])
    if boolean:
        chord.append(note)
    else:
        chord.append(random_note(note_list, exception_list=[note.value])) 


    # Play chord
    chord_seq = NoteSeq(chord)
    write_midi_chord(chord_seq) # make this Note and NoteSeq methods
    player.play_music()
    response = raw_input("Was the note in the chord? ")
    if correct_boolean_response(response, boolean):
        print "Correct!"
    else:
        print "Wrong!"
    print "The first note was " + note.name
    print "The chord was " + ", ".join(map(str, chord))

# Plays a single note "repeat" times
# Arg pitch is the number of the desired pitch
def pitch_meditation(pitch=None, repeat=100): 
    if pitch:
        note = Note(pitch, 5, 1, 100)
    else:
        note = random_note()
    notes = [note]
    while repeat:
        notes.append(note)
        repeat = repeat - 1
    write_midi(notes)
    print "The note is " + note.name
    player.play_music()


# Alternates between a single pitch and a chord containing that pitch
def pitch_in_random_chords(pitch=None, repeat=100):
    if pitch:
        note = Note(pitch, 5, 1, 100)
    else:
        note = random_note()
    print "The note is " + note.name
    while repeat: 
        notes = [note]
        if repeat % 2:
            notes = notes + random_chord()
            write_midi_chord(NoteSeq(notes))
        else:
            write_midi_notes(notes) 
        repeat = repeat - 1
        player.play_music()


# Execute
player.init_player()

test_notes = [Note(0,5,1,100), NoteSeq(random_chord())]
# test_single_pitch_in_chord(other_notes=4)
# pitch_meditation(pitch=9)
# pitch_in_random_chords(pitch=9, repeat=50)
# test_multiple_pitches(note_list=[] 
write_midi(test_notes)
player.play_music()
