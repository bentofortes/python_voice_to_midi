from midiutil import MIDIFile

def write_file(notes, beat, tempo):
    track = 0
    channel = 0
    time = 0
    volume = 100

    duration = beat
    tempo = tempo

    midi = MIDIFile(1)
    midi.addTempo(track, time, tempo)

    for i in range(len(notes)):
        midi.addNote(track, channel, notes[i][2], time + i * beat, beat, volume)

    with open("output.mid", "wb") as file:
        midi.writeFile(file)