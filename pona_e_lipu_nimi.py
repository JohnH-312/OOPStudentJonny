import json

word = {"noun": None, "verb": None, "mod": None, "interjection": None}

try:
    with open("lipu_nimi.json", "r+") as json_lipu:
        nimi_mute = json.load(json_lipu)
except:
    nimi_mute = {}

while True:
    ilo_lawa = input("New(N), Update(U), Remove(R) or Done(D): ")
    if ilo_lawa == "N":
        while True:
            nimi = input("Enter word in Toki Pona: ")
            if nimi in nimi_mute:
                print("That word is already in the Dictionary, try another")
                continue
            sona = input("Enter English Translation: ")
            nimi_mute[nimi] = sona
            break
    elif ilo_lawa == "U":
        while True:
            nimi = input("Enter word in Toki Pona: ")
            if nimi not in nimi_mute:
                print("That word is not in the dictionary, try another")
                continue
            sona = input("Enter English Translation: ")
            nimi_mute.update({nimi: sona})
            break
    elif ilo_lawa == "R":
        nimi = input("Enter word in Toki Pona: ")
        try:
            del nimi_mute[nimi]
        except:
            print("That word was already not in the dictionary")

    elif ilo_lawa == "D":
        break
    else:
        print("Bad Input, Plz enter N, U, R or D!")
        continue

#print to file
with open("lipu_nimi.json", "w+") as json_lipu:
    json.dump(nimi_mute, json_lipu)