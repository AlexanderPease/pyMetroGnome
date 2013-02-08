from pygame_player import init_player, play_music
from pyknon.music import Note, Rest, NoteSeq
from pyknon.genmidi import Midi
from random import randint, choice
from pprint import pprint
import constants

# Writes notes into a midi file 
def write_midi_notes(notes, file_name='temp.mid', tempo=60):
    midi = Midi(1, tempo=60)
    midi.seq_notes(notes, track=0)
    midi.write(file_name)

# Writes a list of NoteSeq "notes" as a series of chords
def write_midi_chord(notes, file_name='temp.mid', tempo=60):
    midi = Midi(1, tempo=60)
    midi.seq_chords([notes], track=0) 
    midi.write(file_name)   

# Checks for var == answer
def correct_response(var, answer=True):
    truelist = ['True', 'T', 'Yes', 'Y', 'yes', 'y']
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


#########################################################
# Executable ear training tests
#########################################################
# Plays a single pitch in note_list and asks you to name it
def test_single_pitch(note_list=None):
    note = random_note(note_list)
    notes = NoteSeq([note])
    write_midi_notes(notes)
    init_player()
    play_music()

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
    init_player()
    play_music()

    # True or False?
    boolean = choice([True, False])
    if not boolean:
        note = random_note(note_list, exception_list=[note.value]) 
   
    # Pick other notes
    chord = [note]
    for i in range(0,other_notes):
        other_note = random_note(note_list, exception_list=[note.value])
        chord.append(other_note)

    # Play chord
    chord_seq = NoteSeq(chord)
    write_midi_chord(chord_seq) # make this Note and NoteSeq methods
    play_music()
    response = raw_input("Was the note in the chord? ")
    if correct_response(response, boolean):
        if other_notes == 1:
            pprint("Correct! The first note was " + note.name)
        else:
            pass #debug
    else:
        pprint("Sorry! The first note was " + note.name)


#Execute
test_single_pitch_in_chord()


