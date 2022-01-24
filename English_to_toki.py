import json

def find_key(input_dict, value):
    return next((k for k, v in input_dict.items() if v == value), None)

with open("lipu_nimi.json", "r") as json_lipu:
        nimi_mute = json.load(json_lipu)

while True:
    nimi_jo = input("Enter Toki Pona to translate(Done to end):")
    if nimi_jo == "Done":
        break
    nimi_jo = nimi_jo.split()
    if "la" in nimi_jo:
        mode = "Conditional_Phrase"
    else:
        mode = "Subject_Phrase"
    for nimi in nimi_jo:
        if nimi == "li":
            mode = "Prepositional_Phrase"
            continue
        elif nimi == "e":
            mode = "Object_Phrase"
            continue
        elif nimi == "la":
            mode = "Subject_Phrase"
            continue

        if nimi not in nimi_mute:
            print("[NULL]")
            continue
        print(nimi_mute[nimi], end=" ")
        print(mode, end=" ")

        if nimi == "sina" or nimi == "mi":
            mode = "Prepositional_Phrase"
        
    print()