import json

with open("lipu_nimi_noun.json", "r") as json_lipu:
    nimi_mute_noun = json.load(json_lipu)
with open("lipu_nimi_verb.json", "r") as json_lipu:
    nimi_mute_verb = json.load(json_lipu)
with open("lipu_nimi_mod.json", "r") as json_lipu:
    nimi_mute_mod = json.load(json_lipu)

while True:
    nimi_jo = input("Enter Toki Pona to translate(Done to end):")
    if nimi_jo == "Done":
        break
    nimi_jo = nimi_jo.split()
    if "la" in nimi_jo:
        mode = "Conditional_Phrase"
    else:
        mode = "Subject_Phrase"
    head = 1
    for nimi in nimi_jo:
        if nimi == "li":
            mode = "Prepositional_Phrase"
            head = 1
            continue
        elif nimi == "e":
            mode = "Object_Phrase"
            head = 1
            continue
        elif nimi == "la":
            mode = "Subject_Phrase"
            head = 1
            continue
        
        if mode == "Prepositional_Phrase" and head == 1: #verb
            if nimi not in nimi_mute_verb:
                print("[NULL]")
                head += 1
                continue
            print(nimi_mute_verb[nimi], end=" ")
            #print(mode, end=" ")
        elif head == 1: #noun
            if nimi not in nimi_mute_noun:
                print("[NULL]")
                head += 1
                continue
            print(nimi_mute_noun[nimi], end=" ")
            #print(mode, end=" ")
        else:
            if nimi not in nimi_mute_mod:
                print("[NULL]")
                head += 1
                continue
            print(nimi_mute_mod[nimi], end=" ")
            #print(mode, end=" ")
        head += 1
        if nimi == "sina" or nimi == "mi":
            mode = "Prepositional_Phrase"
            head = 1
        
    print()