import pandas as pd
import json
import os 


def remove_dupes(a_list):
  return list(dict.fromkeys(a_list))


def print_list(a_list):
    for i in range(len(a_list)):
        print("{} - {}".format(i, a_list[i]))


def get_choice_from_col_list(type_pick: str, col_list: list[str]) -> str | None:
    """
    Accept either:
    - a numeric index, or
    - the exact item name (case-insensitive, trimmed)
    """
    type_pick = type_pick.strip()

    if type_pick == "":
        return None

    # Try index first
    if type_pick.isdigit():
        idx = int(type_pick)
        if 0 <= idx < len(col_list):
            return col_list[idx]
        return None

    # Try name match
    normalized_pick = type_pick.casefold()
    for item in col_list:
        if str(item).casefold() == normalized_pick:
            return item

    return None


# Set up: Get files
filepath_: str = os.path.join(os.path.dirname(__file__), 'data/eu4_prov.csv')
df = pd.read_csv(filepath_, encoding='latin-1')
# ------------------------------------------------------------------------------
# MAIN ROUTINE
# ------------------------------------------------------------------------------
print("Welcome to the eu4 provinces program")
print("Enter which group of provinces you're looking for:")
print("1 - Continent")
print("2 - Superregion")
print("3 - Region")
print("4 - Area")
print("5 - Preset")
while True:
    group_input = input("-: ")
    if group_input == '1':
        col_type = 'Continent'
        break
    elif group_input == '2':
        col_type = 'Superregion'
        break
    elif group_input == '3':
        col_type = 'Region'
        break
    elif group_input == '4':
        col_type = 'Area'
        break
    elif group_input == '5':
        col_type = None
        presets = json.load("data/presets.json")
    else:
        print('Invalid input, try again.')

col_list = df[col_type].tolist()
col_list = remove_dupes(col_list)
print("Pick a " + col_type + ".")
print("You can enter as many as you want, enter nothing to stop.")
areas = []
print_list(col_list)
while True:
    print("You may enter a number OR the exact name of the option.")
    type_pick = input("-: ")

    if type_pick == '':
        break
    else:
        specific_choice = get_choice_from_col_list(type_pick, col_list)

        if specific_choice is None:
            print("Invalid input, try again.")
            continue

        x = df.loc[df[col_type] == specific_choice]
        y = x['ID'].tolist()
        areas.append(y)

print('Finally, enter the command you want to use:')
print('You may keep entering commands, enter nothing to stop.')
commands = []
while True:
    command_ = input('-: ')
    if command_ == '':
        break
    else:
        commands.append(command_)

final_location: str = r"D:\Documents\Paradox Interactive\Europa Universalis IV\custom.txt"
lines: list[str] = []
for area in areas:
    for ID in area:
        for com in commands:
            lines.append(com + ' ' + str(ID) + '\n')

with open(final_location, 'w') as gamefile:
    gamefile.writelines(lines)

print('-'*20 + '\n' + 'Done!\n' + '-'*20)
print('You may now run your command with the following line: "run_commands custom.txt"')