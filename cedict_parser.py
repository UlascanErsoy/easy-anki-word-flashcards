# Script to parse cedict into a dictionary
import json

TONE_MARK = {
    "a": ("ā","á","ǎ","à","a"),
    "o": ("ō","ó","ǒ","ò","o"),
    "e": ("ē","é","ě","è","e"),
    "i": ("ī","í","ǐ","ì","i"),
    "u": ("ū","ú","ǔ","ù","u"),
    "v": ("ǖ","ǘ","ǚ","ǜ","ü")
  }

def replace_tone_marks(pins):
    new_pins = []

    for pin in pins:
        if not pin or not pin[-1].isnumeric():
            new_pins.append(pin)
            continue
        tone = int(pin[-1])-1
        
        for ch in pin[:-1]:
            if ch in TONE_MARK:
                new_pins.append(
                        pin[:-1]\
                                .replace(ch, TONE_MARK[ch][tone])
                                )
                break

    return new_pins

if __name__ == "__main__":
    
    with open("cedict.txt","r") as f:
        entries = f.read().split("\n")[40:-1]

    
    print(f"{len(entries)} entries found!")
    
    results = {}
    for entry in entries:

        character = entry[:entry.find(" ")]
        pinyin = entry[entry.find("[")+1:entry.find("]")].split(" ")
        if not character in results:
            results[character] = replace_tone_marks(pinyin)


    open("cedict.js","w").write("const HANZI = " + json.dumps(results))

    results2 = {}
    with open("pinyin.txt","r") as f:
        for idx, entry in enumerate(f.read().split("\n")):
            sections = entry.split(" ")
            character = sections[0]
            pinyin = replace_tone_marks(sections[1:2])

            if pinyin:
                if character == "怼":
                    print(pinyin)
                results2[character] = pinyin[0]


            
    open("pinyin.js","w").write("const HANZI2 = " + json.dumps(results2))
    
        
