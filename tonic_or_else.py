from pychord import Chord
import pprint

bass_chord = Chord("C")
appendixes = ["", "m", "maj7", "7", "m7", "sus4", "sus2", "aug", "dim", "dim7", "m7b5"]

tonic_list = []

for i in range(12):
    tmp_tonic_list = []
    for appendix in appendixes:
        current_chord = bass_chord.chord + appendix
        print(current_chord)
        print(Chord(current_chord).components())

        if (
            "F" in Chord(current_chord).components()
            and "B" in Chord(current_chord).components()
        ):
            print("Dominant")
        elif (
            "F" in Chord(current_chord).components()
            and "Ab" in Chord(current_chord).components()
        ):
            print("Subdominant-Minor")
        elif "F" in Chord(current_chord).components():
            print("Subdominant")

        else:
            print("Tonic")
            tmp_tonic_list.append(current_chord)

        print("===================================")
    tonic_list.append(tmp_tonic_list)
    bass_chord.transpose(1)

print("Tonic List")
pprint.pp(tonic_list)
