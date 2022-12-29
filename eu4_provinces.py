import pyautogui as pag
import time
import pandas as pd
df = pd.read_csv('eu4_prov.csv', encoding='latin-1')
import win32api
import win32con


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
    else:
        print('Invalid input, try again.')

col_list = df[col_type].tolist()
col_list = remove_dupes(col_list)
print("Pick a " + col_type + ".")
print_list(col_list)
print("Note: You MUST enter a number!")
type_pick = int(input("-: "))
specific_choice = col_list[type_pick]

x = df.loc[df[col_type] == specific_choice]
y = x['ID'].tolist()

print('Finally, enter the command you want to use:')
command_ = input('-: ')
print('You have 10 seconds')
time.sleep(10)
for ID in y:
    command(command_, str(ID))

print('-'*20 + '\n' + 'Done!\n' + '-'*20)