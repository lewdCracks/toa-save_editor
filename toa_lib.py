import json, os, copy

from tkinter import *

import json, logging, tkinter.messagebox, os

LOG_FILENAME = "save_editor_errors.log"
logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)

class BackEnd(object):
    def __init__(self):
        """ Custom backend class for save_editor_V6, some useful functions made easier to use """
        self.dev = "@lew"
        self.new = False
        print('Loaded Backend.')
    
    def load_data(self, path): # load json data
        """ Load json file from path """
        try:
            data = json.load(open(path))
            return data
        except Exception as error:
            self.log_error(error)
    
    def save_data(self, data, path): # save json data
        """ Save dict to json file path """
        try:
            json.dump(data, open(path, "w+"), indent=4)
        except Exception as error:
            self.log_error(error)

    def ask_user(self, head, message): # tkinter box ask for boolean answer
        """ Ask the user a question using tkinter.messagebox, returns True or False"""
        self.root = Tk()
        self.root.withdraw()
        self.c = tkinter.messagebox.askquestion(head, message)
        if self.c == 'yes':
            return True
        else:
            return False
        self.root.destroy()
    
    def show_user(self, head, message): # tkinter box show user info
        """ Show user info using tkinter.messagebox: void """
        self.root = Tk()
        self.root.withdraw()
        self.c = tkinter.messagebox.showinfo(head, message)
        self.root.destroy()    

    def log_error(self, error): # log error to LOG_FILENAME path
        """ Displays tkinter.messagebox error, shows discord dev name set with self.dev, records to LOG_FILENAME """
        self.root = Tk()
        self.root.withdraw()
        logging.exception({error})
        tkinter.messagebox.showerror('Woops!', f"You ran into an error please report to {self.dev} on discord if the error was fatal.\n\n{error}\n\nFull error log is available in logs folder.")
        self.root.destroy()

util = BackEnd()

class LoaderError(Exception):
    pass

class EditorError(Exception):
    pass

class Loader():
    def __init__(self, path='.toa-data'): # add image system to save, so user can see latest save update
        self.base_path = path

        self.save_paths = {}
        self.saves = {}
        self.debug = True

        self.load_paths(path)
    
    def pd(self, val): # print data if self.debug
        if self.debug == True:
            print('[debug]',val)
    
    def load_paths(self, path):
        for file in os.listdir(path):
            if file.endswith('.json'):
                self.save_paths[file.replace('.json', '')] = os.path.join(self.base_path, file)
                self.pd(f"Acknowledged {file}")
            else:
                self.pd(f"Ignored {file}")
    
    def get_raw_data(self, save_name):
        res = self.save_paths.get(save_name, False)
        if res and os.path.isfile(res):
            return json.load(open(res))
        else:
            raise LoaderError(f"Tried to get save '{save_name}.json' returned '{res}', the file either no longer exists or was not loaded properly.")
    
    def save_is_empty(self, save_name):
        data = self.get_raw_data(save_name)  
        if not data.get('playerStart', False):
            return True, data
        else:
            return False, data
    
    def build_save_data(self, save_name):
        res,data = self.save_is_empty(save_name)
        self.saves[save_name] = {}
        self.saves[save_name]['empty'] = res # if empty, its an unused save meaning the player hasn't saved anything to it yet.
        self.saves[save_name]['data'] = data
        self.pd(f"built {save_name}.json")
    
    def build_all_save_data(self):
        for sname in self.save_paths:
            self.build_save_data(sname)
    
    def get_save(self, save_name):
        res = self.saves.get(save_name, False)
        if res:
            self.pd(f"loaded {save_name}.json")
            return res['data'], save_name
        else:
            raise LoaderError(f"Tried to get '{save_name}'.json however the save data was never built.")

# add error handling and proper case clauses
class Dumper():
    def __init__(self, loader_save_paths) -> None:
        self.reverts = {}
        self.save_paths = loader_save_paths
    
    def dump(self, save_name, original_data, dump_data):
        self.reverts[save_name] = original_data
        json.dump(dump_data, open( self.save_paths[save_name], 'w+'), indent=3)
    
    def revert(self, save_name):
        json.dump(self.reverts[save_name], open( self.save_paths[save_name], 'w+'), indent=3)

class BaseEditor():
    def __init__(self, save_data, save_name):
        self.original_save_data = copy.deepcopy(save_data)
        self.save_data = save_data
        self.save_name = save_name
        self.player_data = self.save_data['player']

        self.purity_tiers = ['CHASTE', 'PURE', 'COQUETTISH', 'FLIRTY', 'KINKY', 'LOOSE', 'EASY', 'TRASHY', 'SLUTTY', 'COMPLETE_SLUT']
        self.dignity_tiers = ['HAUGHTY', 'PROUD', 'DIGNIFIED', 'HUMBLE', 'EMBARRASSED', 'SHAMED', 'HUMILIATED', 'DISGRACED', 'DEPRAVED', 'NONE', 'FULL']
        self.femininity_enums = ['MASCULINE', 'UNMASCULINE', 'ANDROGYNOUS', 'EFFEMINATE', 'GIRLY', 'FEMININE', 'BITCH', 'MALE', 'FEMALE']
        self.breast_enums = ['FLAT', 'LITTLE', 'HANDFUL', 'FUN']
        self.pronoun_enums = ['MALE', 'FEMALE', 'SECOND_PERSON']
        self.booty_enums = ['Bubble', 'Round', 'Fat']
        self.lip_enums = ['Thin', 'Pouty', 'Full', 'Beestung']
        self.races = ['Lowlander', 'Highlander', 'Mountainman', 'Elfblood', 'Orcblood']
        self.hair_colors = ['Black', 'Brown', 'Red', 'Blonde', 'Pink', 'Mix']
        self.eye_colors = ['Blue', 'Teal', 'Pink', 'Golden']
        self.jobs = ['WARRIOR', 'PALADIN', 'THIEF', 'RANGER', 'MAGE', 'ENCHANTRESS', 'BITCH', 'MARE', 'BUNNY', 'QUEEN', 'PROSTITUTE', 'SCHOOLGIRL', 'LEWD_SCHOOLGIRL']
        self.contexts = ['ENCOUNTER', 'WORLD_MAP', 'BATTLE', 'LEVEL', 'TOWN', 'CAMP', 'BROTHEL', 'GAME_OVER']

    @property
    def file(self):
        return self.save_name, self.original_save_data, self.save_data
    
    def merge_lists(self, list1, list2):
        return list(set(list1+list2))

    def merge_data(self, data1, data2):
        return data2.update(data1)

    def replace_data(self, key, data):
        res = self.player_data.get(key, False)
        if res and (type(res) == type(data)):
            self.player_data[key] = data
        else:
            raise EditorError(f"Data could not be replaced: key_found = {bool(res)}, if True data types may not have matched.")
    
    def get_mode(self, editable=False):
        mode = self.original_save_data.get('mode', False)
        if editable:
            if mode == 'STORY':
                return False, mode
        return True, mode

    def node_set(self, node):
        self.save_data['nodeCode'] = int(node)

    def entry_set(self, entry, val, convert_to):
        self.player_data[entry] = convert_to(val)
    
    def entry_get(self, entry_key, convert_to):
        entry = self.player_data.get(entry_key, 1001.1001)
        if entry != 1001.1001:
            return convert_to(entry)
        else:
            print(f"[debug] entry for key : '{entry_key}' does not exist, returning acceptable variable")
            return convert_to(-1)
 
    def pronoun_set(self, enum): # add 'you,he,she' label selection
        enum = str(enum).upper()
        if enum in self.pronoun_enums:
            self.player_data['pronouns'] = enum
            if enum == 'SECOND_PERSON':
                self.player_data['secondPerson'] = True
            else:
                self.player_data['secondPerson'] = False
        else:
            raise EditorError(f"Could not find '{enum}' in pronoun enums list.")

    def purity_set(self, tier, val=100):
        if tier == 'DNE': return
            
        tier = str(tier).upper()
        if tier in self.purity_tiers:
            self.player_data['purity']['tier'] = tier
            self.player_data['purity']['purity'] = int(val)
        else:
            raise EditorError(f"Could not find '{tier}' in purity tier list.")
    
    def purity_get(self):
        return self.player_data.get('purity', {'tier':'DNE'}).get('tier', 'DNE')

    def dignity_set(self, tier, val=100):
        if tier == 'DNE': return

        tier = str(tier).upper()
        if tier in self.dignity_tiers:
            self.player_data['dignity']['tier'] = tier
            self.player_data['dignity']['dignity'] = int(val)
        else:
            raise EditorError(f"Could not find '{tier}' in dignity tier list.")

    def dignity_get(self):
        return self.player_data.get('dignity', {'tier':'DNE'}).get('tier', 'DNE')

    def breast_set(self, enum):
        if enum == 'DNE': return

        breast = str(enum).upper()
        if breast in self.breast_enums:
            self.player_data['breast'] = breast
        else:
            raise EditorError(f"Could not find '{breast}' in breast enums list.")
    
    def breast_get(self):
        return self.player_data.get('breast', 'DNE')
    
    def race_set(self, race):
        if race == 'DNE': return

        race = str(race).lower().capitalize()
        if race in self.races:
            self.player_data['race'] = race
        else:
            raise EditorError(f"Could not find '{race}' in races list.")
    
    def race_get(self):
        return self.player_data.get('race', 'DNE')

    def job_set(self, job):
        if job == 'DNE': return

        job = str(job).upper()
        if job in self.jobs:
            self.player_data['jobClass'] = job
        else:
            raise EditorError(f"Could not find '{job}' in jobs list.")
    
    def job_get(self):
        return self.player_data.get('jobClass', 'DNE')
    
    def hair_set(self, color):
        if color == 'DNE': return

        color = str(color).lower().capitalize()
        if color in self.hair_colors:
            self.player_data['hairColor'] = color
        else:
            raise EditorError(f"Could not find '{color}' in hair colors list.")

    def hair_get(self):
        return self.player_data.get('hairColor', 'DNE')

    def eye_set(self, color):
        if color == 'DNE': return

        color = str(color).lower().capitalize()
        if color in self.eye_colors:
            self.player_data['eyeColor'] = color
        else:
            raise EditorError(f"Could not find '{color}' in eye colors list.")
    
    def eye_get(self):
        return self.player_data.get('eyeColor', 'DNE')

    def lip_set(self, enum):
        if enum == 'DNE': return

        enum = str(enum).lower().capitalize()
        if enum in self.lip_enums:
            self.player_data['lipFullness'] = enum
        else:
            raise EditorError(f"Could not find '{enum}' in lip enums list.")
    
    def lip_get(self):
        return self.player_data.get('lipFullness', 'DNE')

    def booty_set(self, enum):
        if enum == 'DNE': return

        enum = str(enum).lower().capitalize()
        if enum in self.booty_enums:
            self.player_data['bootyliciousness'] = enum
        else:
            raise EditorError(f"Could not find '{enum}' in booty enums list.")
    
    def booty_get(self):
        return self.player_data.get('bootyliciousness')

    def femininity_set(self, enum):
        if enum == 'DNE': return

        enum = str(enum).upper()
        if enum in self.femininity_enums:
            self.player_data['femininity'] = enum
        else:
            raise EditorError(f"Could not find '{enum}' in lip femininity enums list.")
    
    def femininity_get(self):
        return self.player_data.get('femininity')

    
class AdvancedEditor(BaseEditor):
    def __init__(self, save_data, save_name):
        super().__init__(save_data, save_name)

        self._data = False

        self.encounter_codes = [
            'WERESLUT', 'WERESLUT_QUICKSHOT', 'WERESLUT_FRIENDLY', 'WERESLUT_EXCITED', 'HARPY', 'HARPY_DIVEBOMBER', 'HARPY_SWARM', 'HARPY_BREEDING', 'SLIME', 'BRIGAND', 
            'BRIGAND_THIEF', 'BRIGAND_HORNY', 'BRIGAND_COTTAGE', 'CULTIST', 'DRYAD', 'CENTAUR', 'GOBLIN', 'GOBLIN_MALE', 'GADGETEER', 'ORC', 
            'ADVENTURER', 'OGRE', 'BEASTMISTRESS', 'BEASTMISTRESS_HUNTER', 'SPIDER', 'ELF', 'GOLEM', 'GHOST', 'GHOST_MANOR', 'BUNNY', 
            'ANGEL', 'NAGA', 'NAGA_PLAYFUL', 'NAGA_CAVE_IN', 'MOUTH_FIEND', 'MERMAID', 'WARLOCK', 'WASP', 'WASP_NUPTIAL_AREA', 'DOPPELGANGER', 
            'VAMPIRE', 'MINOTAURESS', 'GIANTESS_FUTA', 'DULLAHAN', 'MERRYBELLE', 'QUETZAL', 'HEALING_POND', 'FIRE_ELEMENTAL', 'ETTIN', 'ETTIN_SLEEPING', 
            'JESTER', 'DARK_KNIGHT', 'DARK_KNIGHT_2', 'OGRE_WANDERER', 'GOBLIN_HORDE', 'CATGIRL'
        ]
        self.quest_codes = [
            'ORC', 'CRIER', 'QUETZAL', 'INNKEEP', 'TRUDY', 'CENTAUR', 'GOBLIN', 'GOBLIN_AMBUSH', 'OGRE', 'SPIDER', 'BROTHEL', 'ELF', 'DULLAHAN', 'DEBT', 'GADGETEER',
            'MADAME', 'WITCH', 'MOUTH_FIEND', 'MERMAID', 'TRAINER', 'MERI', 'HUMAN_TOWN', 'MONSTER_TOWN', 'OUTPOST_TOWN', 'WARLOCK', 'GIANTESS', 'HEALING_POND',
            'HARPY_ANATOMY', 'WEREWOLF_ANATOMY', 'GIANT_ANATOMY', 'CENTAUR_ANATOMY', 'CAT_ANATOMY', 'HARPY_INTELLIGENCE', 'WEREWOLF_SCENT',
            'SPIDER_ARENA', 'WEREWOLF_SEEN', 'WEREWOLF_ORIGIN', 'WASP', 'CHURCH', 'DULLAHAN_SEEN', 'GHOST_SEEN', 'CURSED_ARMOR', 'VAMPIRE_SEEN',
            'CULTIST', 'CENTAUR_ELLA', 'CENTAUR_JACK', 'CENTAUR_NAME', 'GIANTESS_HOARD', 'BROTHEL_MADAME_REQUEST', 'BROTHEL_OPEN', 'LUPA_SPY',
            'LUPA_INTERROGATE', 'BROTHEL_SCHOOLGIRL', 'CENTAUR_BOW', 'SPERM_BANK', 'MILKSHAKE', 'ANGEL', 'STORY', 'VIRGIN_FUTA', 'BROTHEL_WEREWOLF_ORAL',
            'DARK_KNIGHT_TAVERN', 'STORY_DARK_KNIGHT_TAVERN', 'BROTHEL_MADAME_ASS_EATING', 'INNKEEP_SUCK', 'GOBLIN_FLUSHED', 'SALON', 'STORY_FORT',
            'BRIGAND_CANT', 'WARLOCK_COMPANION', 'GADGETEER_TEST', 'IMPOTENT', 'VISITED_GLORYHOLE', 'SERVICED_GLORYHOLE', 'LUPA_MET'
        ]

        self.map_ids = ['DEFAULT', 'SECOND', 'THIRD', 'FOURTH']
    
    @property
    def data_exists(self):
        if not self._data:
            return False
        else:
            return True
    
    @property
    def data_info(self):
        return self.data.get('version_info', "data_info : False")
    
    @property
    def data(self):
        if self.data_exists:
            return self._data
    
    def _version_check(self):
        if self.data_info.get('data_version', -1) != 4:
            util.show_user("Error!", "data.json is out of date, please download the latest version.")
            quit(-1)
    
    def _g_val(self, v_list, query, upper=True):
        """ internal function used to generically validate that a query exists in a given list """
        if upper and (query.upper() in v_list):
            return True
        elif query in v_list:
            return True
        else:
            return False
    
    def update_quest_flags(self, new_flags):
        self.player_data = self.merge_data(self.player_data['questFlags'], new_flags)
    
    def get_location(self, location_key):
        if self.data_exists:
            return self.data.get['locations'].get(location_key, False)
        else:
            print('[debug] unable to get locations as no external data has been loaded...')
            return False
    
    def load_external_data(self, d_path):
        try:
            self._data = json.load(open(d_path, 'r'))
            print('[debug] loaded data.json')
        except Exception as error:
            util.log_error(error)
            raise error
    
    def map_id_set(self, map_id):
        if self._g_val(self.map_ids, map_id):
            self.save_data['mapId'] = map_id.upper()
        else:
            print(f'[debug] unable to set map_id : {map_id}/{map_id.upper()}')
    
    def context_set(self, context_code):
        if self._g_val(self.contexts, context_code):
            self.save_data['context'] = context_code.upper()
    
    def encounter_code_set(self, encounter_code):
        if self._g_val(self.encounter_codes, encounter_code):
            self.save_data['encounterCode'] = encounter_code.upper()
    
    def location_set(self, location_key):
        data=self.get_location(location_key)
        if data:
            self.map_id_set(data['mapId'])
            self.node_set(data['node'])
            self.context_set(data['context'])
            self.encounter_code_set(data['encounterCode'])
            self.update_quest_flags(data['questFlags'])
        else:
            print(f'[debug] location does not exist : {location_key}')


if __name__ == '__main__':
    loader = Loader(r"C:\Users\junkj\Documents\code\other\g\beep\Tales of Androgyny Win64\.toa-data")
    loader.build_all_save_data()
    dumper = Dumper(loader.save_paths)

    d = loader.get_save('save')

    be = AdvancedEditor(*d)
    be.load_external_data('data.json')
    be.location_set('strange_merchant')

    dumper.dump('save', be.original_save_data, be.save_data)

