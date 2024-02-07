import os
import json
import zipfile

class DynamicFile:
    def __init__(self, path, fname, ftype) -> None:
        self.path = path
        self.name = fname
        self.type = ftype
    
    def __repr__(self) -> str:
        return f"DynamicFile({self.path})"
    
    def __str__(self) -> str:
        return self.path
    
    def __eq__(self, __value: object) -> bool:
        return self.name == __value
    
    def as_json(self):
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            return False
    
    def save(self, data, str_type = False):
        if self.type == 'json' and not str_type:
            json.dump(data, open(self.path, "w"), indent=4)
        else:
            with open(self.path, "w") as f:
                f.write(data)
        

def build_profile(as_string = True) -> str | dict:
    with zipfile.ZipFile("TalesOfAndrogyny.jar", 'r') as zip_ref:
        raw = zip_ref.read("script/encounters.json")
        data = json.loads(raw)

    profile = {
        "achievements": set(),
        "enemyKnowledge": set(),
        "events": set(),
        "cgSeen": set(),
        "animatedCgSeen": set(),
        "outfitUnlocked": set(),
    }

    for scenario, scenes in data.items():
        profile["events"].add(scenario)

        for scene in scenes:
            profile["cgSeen"].add(scene.get('foreground', ''))
            profile["animatedCgSeen"].add(scene.get('animatedForeground', ''))
            for mutation in scene.get('mutations', []):
                save_type = mutation.get('profileSaveType')
                if save_type:
                    value = mutation['value']['value']
                    match save_type:
                        case "ACHIEVEMENT":
                            profile["achievements"].add(value)
                        case "KNOWLEDGE":
                            profile["enemyKnowledge"].add(value)
                        case "OUTFIT_UNLOCKED":
                            profile["outfitUnlocked"].add(value)
                        case _:
                            print(f"Unknown profile save type: {save_type}")

    profile = {key: {text: 1 for text in values if text != ''} for key, values in profile.items() if key != ''}
    
    profile['saveVersion'] = 1

    if as_string:
        return json.dumps(profile, indent=2).replace('"', '').replace(',', '')
    else:
        return profile
    
def init_data():
    TOA_DATA_PATH = os.path.join(os.getenv("APPDATA"), "TalesOfAndrogyny")
    if not (data := os.path.exists(TOA_DATA_PATH)) or not(game := os.path.isfile("TalesOfAndrogyny.jar")):
        return (data, game)
    
    files = {}
    for file in os.listdir(TOA_DATA_PATH):
        if (ftype := file.split(".")[-1]) not in files:
            files[ftype] = []
        files[ftype].append(DynamicFile(os.path.join(TOA_DATA_PATH, file), file, ftype))

    return files

# if __name__ == "__main__":
    # data = json.load(open("encounters.json", "r"))
    # build_profile(data)
    # data = init_data()  
    # for file in data["json"]:
    #     if file == "profile.json":
    #         print(file.as_json())
    
