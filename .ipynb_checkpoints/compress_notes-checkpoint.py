notesList = [
    ['E2', 82.41, 40], 
    ['F2', 87.31, 41], 
    ['F#2/Gb2', 92.5, 42], 
    ['G2', 98, 43], 
    ['G#2/Ab2', 103.83, 44], 
    ['A2', 110, 45], 
    ['A#2/Bb2', 116.54, 46], 
    ['B2', 123.47, 47], 
    ['C3', 130.81, 48], 
    ['C#3/Db3', 138.59, 49], 
    ['D3', 146.83, 50], 
    ['D#3/Eb3', 155.56, 51], 
    ['E3', 164.81, 52], 
    ['F3', 174.61, 53], 
    ['F#3/Gb3', 185, 54], 
    ['G3', 196, 55], 
    ['G#3/Ab3', 207.65, 56], 
    ['A3', 220, 57], 
    ['A#3/Bb3', 233.08, 58], 
    ['B3', 246.94, 59], 
    ['C4', 261.63, 60], 
    ['C#4/Db4', 277.18, 61], 
    ['D4', 293.66, 62], 
    ['D#4/Eb4', 311.13, 63], 
    ['E4', 329.63, 64], 
    ['F4', 349.23, 65], 
    ['F#4/Gb4', 369.99, 66], 
    ['G4', 392, 67], 
    ['G#4/Ab4', 415.3, 68], 
    ['A4', 440, 69], 
    ['A#4/Bb4', 466.16, 70], 
    ['B4', 493.88, 71], 
    ['C5', 523.25, 72], 
    ['C#5/Db5', 554.37, 73], 
    ['D5', 587.33, 74], 
    ['D#5/Eb5', 622.25, 75], 
    ['E5', 659.25, 76]
]

def compress_notes(notes):
    dur_list = []
    prev_note = notes[0][0]
    count = 0
    for note in notes:
        if note[0] == prev_note:
            count += 1

        else:
            dur_list.append(count)
            count = 0
            prev_note = note[0]
    dur_list.append(count)

    avg_dur = int(sum(dur_list)/len(dur_list))
    print(avg_dur)

    start = 0
    end = avg_dur
    result = []
    aux = None
    prev_aux = None
    while end < len(notes):
        freq_map = {}
        for i in range(start, end):
            if not freq_map.get(notes[i][0]):
                freq_map[notes[i][0]] = 1   

            else:
                freq_map[notes[i][0]] += 1

        most_freq = 0
        for key in list(freq_map.keys()):
            if freq_map[key] > most_freq:
                aux = key

        if aux != prev_aux:
            result.append(aux)    
            prev_aux = aux    

        start += 3
        end += 3

    final_result = []
    for i in result:
        for note in notesList:
            if i == note[0]:
                final_result.append(note)
                break

    return final_result
