from pychord import Chord

bass_chord = Chord("C")
appendixes = ["", "m", "maj7", "7", "m7", "sus4", "sus2", "aug", "dim", "dim7", "m7b5"]

tonic_list = []
subdominant_list = []
subdominant_minor_list = []
dominant_list = []

for i in range(12):
    for appendix in appendixes:
        curent_chord = bass_chord.chord + appendix
        print(curent_chord)
        print(Chord(curent_chord).components())

        if (
            "F" in Chord(curent_chord).components()
            and "B" in Chord(curent_chord).components()
        ):
            print("Dominant")
            dominant_list.append(curent_chord)
        elif "F" in Chord(curent_chord).components():
            print("Subdominant")
            subdominant_list.append(curent_chord)
        elif "Ab" in Chord(curent_chord).components():
            print("Subdominant-Minor")
            subdominant_minor_list.append(curent_chord)
        else:
            print("Tonic")
            tonic_list.append(curent_chord)

        print("===================================")

    bass_chord.transpose(1)

print("Tonic List")
print(tonic_list)
print("Subdominant List")
print(subdominant_list)
print("Subdominant Minor List")
print(subdominant_minor_list)
print("Dominant List")
print(dominant_list)
