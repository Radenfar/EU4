import pandas as pd
import numpy as np
import random
import os
import sys

def remove_dupes(a_list):
  return list(dict.fromkeys(a_list))

def print_list(a_list):
    for i in range(len(a_list)):
        print("{} - {}".format(i, a_list[i]))

def get_random(df):
    return df.iloc[np.random.randint(0, len(df))]

def get_random_formable(df):
    while True:
        new_random = df.iloc[np.random.randint(0, len(df))]
        if "Formable" in str(new_random["Type"]):
            return new_random

def file_to_list(filename="countries.txt") -> list[str]:
    countries = []
    with open(filename, 'r') as file:
        for line in file:
            countries.append(line.strip())
    return countries

def formable_challenge(df):
    random_1 = get_random(df)
    random_2 = get_random_formable(df)
    print("As " + str(random_1["Name"]) + " from " + str(random_2["Name"]))

def migration_challenge(df):
    random_1 = get_random(df)
    random_2 = get_random(df)
    print("As " + str(random_1["Name"]) + " migrate to " + str(random_2["Name"]))
    

def modern_country_challenge(df):
    modern_countries: list[str] = file_to_list()
    random_row = get_random(df)
    print("As " + str(random_row["Name"]) + " form " + random.choice(modern_countries) + " with modern borders.")

def random_country(df):
    random_row = get_random(df)
    print("Your random country to play is: " + str(random_row["Name"]))


df = pd.read_csv('eu4_nations.csv', encoding='latin-1')
os.system('cls' if os.name == 'nt' else 'clear')

print("Enter which type of challenge you're after:")
print("1 - Formable Challenge")
print("2 - Migration Challenge")
print("3 - Modern Country Challenge")
print("4 - Random Country")
print("q - Quit Program")
while True:
    group_input = input("-: ")
    if group_input == '1':
        formable_challenge(df)
    elif group_input == '2':
        migration_challenge(df)
    elif group_input == '3':
        modern_country_challenge(df)
    elif group_input == '4':
        random_country(df)
    elif group_input == 'q':
        sys.exit()
    else:
        print('Invalid input, try again.')
