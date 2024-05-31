import pyautogui as pag
import time
import pandas as pd
import json

df = pd.read_csv(r'C:\Users\adamc\Documents\Programming\Python\eu4\eu4_prov.csv', encoding='latin-1')

def command(command, id):
    pag.write(command + ' ' + id)


def remove_dupes(a_list):
  return list(dict.fromkeys(a_list))

def print_list(a_list):
    for i in range(len(a_list)):
        print("{} - {}".format(i, a_list[i]))

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
        presets = json.load("presets.json")
    else:
        print('Invalid input, try again.')

col_list = df[col_type].tolist()
col_list = remove_dupes(col_list)
print("Pick a " + col_type + ".")
print("You can enter as many as you want, enter nothing to stop.")
areas = []
print_list(col_list)
while True:
    print("Note: You MUST enter a number!")
    type_pick = input("-: ")
    if type_pick == '':
        break
    else:
        specific_choice = col_list[int(type_pick)]
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

print('You have 10 seconds')
time.sleep(10)
for area in areas:
    for ID in area:
        for com in commands:
            command(com, str(ID))

print('-'*20 + '\n' + 'Done!\n' + '-'*20)