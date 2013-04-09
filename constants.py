PITCH_C = 0
PITCH_Csharp = 1
PITCH_Dflat = 1
PITCH_D = 2
PITCH_Dsharp = 3
PITCH_Eflat = 3
PITCH_E = 4
PITCH_F = 5
PITCH_Fsharp = 6
PITCH_Gflat = 6
PITCH_G = 7
PITCH_Gsharp = 8
PITCH_Aflat = 8
PITCH_A = 9
PITCH_Asharp = 10 
PITCH_Bflat = 10
PITCH_B = 11

# Integer changes to an existing pitch
U = 0
m2 = 1
M2 = 2
m3 = 3
M3 = 4
P4 = 5
Aug4 = 6
dim5 = 6
tri = 6
P5 = 7
m6 = 8
M6 = 9
m7 = 10
dom = 10
M7 = 11
Oct = 12

MAJOR_SCALE = [1, 3, 5, 6, 8, 10, 12]
NATURAL_MINOR_SCALE = [1, 3, 4, 6, 8, 9, 11]

# Chords from a single pitch
MAJOR_TRIAD = [U, M3, P5]
MINOR_TRIAD = [U, m3, P5]
DIMINISHED = [U, m3, dim5]
MAJOR_SEVENTH = [U, M3, P5, M7]
MINOR_SEVENTH = [U, m3, P5, M7]
DOMINANT_SEVENTH = [U, M3, P5, m7]
HALF_DIMINISHED = [U, m3, dim5, m7]
FULLY_DIMINISHED = [U, m3, dim5, m7-1]
DIMINISHED_SEVENTH = FULLY_DIMINISHED

# Rhythmic constants
QUARTER = 0.25
HALF = 2 * QUARTER
WHOLE = 4 * QUARTER
EIGHTH = QUARTER / 2
SIXTEENTH = QUARTER / 4


