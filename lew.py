import toa_lib
import os
import sys
import traceback

class Saves:
    def __init__(self, dyn_files: list[toa_lib.DynamicFile]) -> None:
        self.files = dyn_files

    def available_saves(self):
        return [file.name.split('.')[0] for file in self.files['json'] if 'save' in file.name]
    
    def get_save(self, save_name: str):
        return [file for file in self.files['json'] if f"{save_name}.json" == file.name][0]

class Editor:
    def __init__(self, saves: Saves, running = True) -> None:
        self.saves = saves
        self.save_name = saves.available_saves()[0]               if running else None
        self.save_data = saves.get_save(self.save_name).as_json() if running else None
        self.player_data = self.save_data['player']               if running else None
        
        self.last_result = None
        self.debug_out = None

        self.command_state = 'basic'
        self.running = running
    
    def switch_save(self, save_name: str):
        if save_name in self.saves.available_saves():
            self.save_name = save_name
            self.save_data = self.saves.get_save(save_name).as_json()
            self.player_data = self.save_data['player']
            self.last_result = f'Switched to {save_name}.'
        else:
            self.last_result = f'Save {save_name} does not exist.'
    
    def set(self, key, value, cast_as):
        if vtype := type(self.player_data.get(key)):
            self.debug_out = f"Cast Type Matches: {vtype == cast_as}({vtype.__name__} == {cast_as.__name__})"

        try:
            self.last_result = f"Set '{key}' to {value}. [{self.player_data.get(key)} -> {value}]"
            self.player_data[key] = cast_as(value)
        except ValueError:
            self.last_result = f"Invalid value input. '{value}' is not a '{cast_as.__name__}'"

    def get(self, key):
        return self.player_data.get(key, 'Does not exist/None.')

class Menu:
    def __init__(self, editor: Editor) -> None:
        self.editor = editor
        self.catgories = []

    def add_category(self, header, aliases: list):
        attributes = {}
        for index, pair in enumerate(aliases):
            attributes[f"{index+1}. {pair[0]}"] = pair[1]

        self.catgories.append((header, attributes))
    
    def display(self):
        for header, attributes in self.catgories:
            print(f"\n=== {header} ===")
            for attribute, key in attributes.items():
                print(f"{attribute}: {self.editor.get(key)}")
        

def init_editor():
    if all(data := toa_lib.init_data()):
        return Editor(Saves(data))
    else:
        has_data, has_game = data
        print(f"Found Game: {has_game}\nFound Data: {has_data}\nEnsure 'TalesOfAndrogyny.jar' is in the same directory as this editor & that the game has been run at least once.")
    input("Press ENTER to exit.")
    return Editor(None, False)

def print_help():
    if sys.argv[0].endswith('lewd.exe'): # Even when compiled to .exe, the file name is still 'l3w.py'. (pyinstaller --onefile)
        print("\n=== {-_-} ===")
    else:
        print("\nEditing Instructions:")
        print("- To modify an attribute: Select the number corresponding to the attribute, followed by the desired value.")
        print("  Example: To change the level to 5, type '2 5'.")
        print("  Some commands require no value, such as '9' to save changes. These commands will be noted as such using brackets [].")
        print("\nSaving and Exiting:")
        print("- To save your changes, simply type the appropriate save command for the menu you're in.")
        print("- Press ENTER or type 'exit' to leave the application without saving.")
        print("\nHelp Menu:")
        print("- If you would no longer like to see this information, change the name of this file to 'lewd.exe'. (If you have file extensions hidden, it will appear as 'lewd')")

def basic_commands(editor: Editor):
    print("\n=== Basic Attributes ===")
    print(f"1. Name: {editor.get('name')}")
    print(f"2. Level: {editor.get('level')}")
    print(f"3. Money: {editor.get('money')}")
    print(f"4. Crystals: {editor.get('magicPoints')}")
    print(f"5. Food: {editor.get('food')}")
    print(f"6. Willpower: {editor.get('willpower')}")
    print("\n=== Commands ===")
    print(f"7. Load Save: '{editor.save_name}' - Available saves: {', '.join(editor.saves.available_saves())}")
    print(f"[8.] Advanced Commands (Detailed Stats, Skillpoints, etc.)")
    print(f"[9.] Save Changes (Current Save: {editor.save_name})")


    print_help()    
    command = input("> ").split() or ['exit']
    primary = command[0].lower()

    match primary:
        case 'exit':
            return False
        case '1':
            editor.set('name', command[1], str)
            return True
        case '2':
            editor.set('level', command[1], int)
            return True
        case '3':
            editor.set('money', command[1], int)
            return True
        case '4':
            editor.set('magicPoints', command[1], int)
            return True
        case '5':
            editor.set('food', command[1], int)
            return True
        case '6':
            editor.set('willpower', command[1], int)
            return True
        case '7':
            editor.switch_save(command[1])
            return True
        case '8':
            editor.command_state = 'advanced'
            return True
        case '9':
            editor.saves.get_save(editor.save_name).save(editor.save_data)
            editor.last_result = f'Saved {editor.save_name}.'
            return True
        case _:
            editor.last_result = 'Invalid command.'
            return True

def advanced_commands(editor: Editor):
    print("\n=== Advanced Stats ===")
    print(f"1. Strength: {editor.get('baseStrength')}")
    print(f"2. Endurance: {editor.get('baseEndurance')}")
    print(f"3. Agility: {editor.get('baseAgility')}")
    print(f"4. Perception: {editor.get('basePerception')}")
    print(f"5. Magic: {editor.get('baseMagic')}")
    print(f"6. Charisma: {editor.get('baseCharisma')}")
    print(f"7. Skillpoints: {editor.get('skillPoints')}")
    print(f"8. Perkpoints: {editor.get('perkPoints')}")
    print("\n=== Commands ===")
    print("[9.] Unlock All (Outfits, Achievements, Gallery, etc. - Effective Immediately)")
    print("[10.] Return to Basic Commands (Name, Level, Money, etc.)")
    print(f"[11.] Save Changes (Current Save: {editor.save_name})")

    print_help()
    command = input("> ").split() or ['exit']
    primary = command[0].lower()

    match primary:
        case 'exit':
            return False
        case '1':
            editor.set('baseStrength', command[1], int)
            return True
        case '2':
            editor.set('baseEndurance', command[1], int)
            return True
        case '3':
            editor.set('baseAgility', command[1], int)
            return True
        case '4':
            editor.set('basePerception', command[1], int)
            return True
        case '5':
            editor.set('baseMagic', command[1], int)
            return True
        case '6':
            editor.set('baseCharisma', command[1], int)
            return True
        case '7':
            editor.set('skillPoints', command[1], int)
            return True
        case '8':
            editor.set('perkPoints', command[1], int)
            return True
        case '9':
            editor.saves.get_save('profile').save(toa_lib.build_profile(), str_type = True)
            editor.last_result = 'Unlocked all.'
            return True
        case '10':
            editor.command_state = 'basic'
            return True
        case '11':
            editor.saves.get_save(editor.save_name).save(editor.save_data)
            editor.last_result = f'Saved {editor.save_name}.'
            return True
        case _:
            editor.last_result = 'Invalid command.'
            return True

def main():
    editor = init_editor()
    while editor.running:
        os.system('cls')
        if editor.last_result:
            print(f">>> {editor.last_result}")

        if editor.debug_out:
            print(f"DEBUG: {editor.debug_out}")
            editor.debug_out = None

        if editor.command_state == 'basic':
            editor.running = basic_commands(editor)
        elif editor.command_state == 'advanced':
            editor.running = advanced_commands(editor)


if __name__ == "__main__":
    # editor = init_editor()
    # menu = Menu(editor)
    # menu.add_category("Basic Attributes", [
    #     ('Name', 'name'), ('Level', 'level'),
    #     ('Money', 'money'), ('Crystals', 'magicPoints'),
    #     ('Food', 'food'), ('Willpower', 'willpower')
    # ])
    # menu.add_category("Commands", [
    #     (f"Load Save: '{editor.save_name}'", 'load'),
    #     (f"Advanced Commands", 'advanced'),
    #     (f"Save Changes (Current Save: {editor.save_name})", 'save')
    # ])
    # menu.display()
    try:
        # ...
        main()
    except:
        traceback.print_exc() 
        input("\nPlease screenshot or copy the above error to be used when reporting.\nPress ENTER to exit.\n>>> ")
        exit(0)
