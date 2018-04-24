import json

f = open('./survivor.json', 'r', encoding="utf-8_sig")
survivors = json.load(f)

class Survivor:
    def charaData(self, name):
        data = {
            "name": name,
            "perks": survivors[name]
        }

        return data
