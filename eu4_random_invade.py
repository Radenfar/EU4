import random

def open_file(file_name):
    file = open(file_name, "r")
    file_data = file.read()
    file.close()
    return file_data

def data_handle(raw_data, index):
    raw_data = raw_data.split("\n")
    data = []
    for d in raw_data:
        data.append(d.split(",")[index])
    return data

def get_random_nation(already_invaded):
    nation_data = open_file("eu4_nations.csv")
    nations = data_handle(nation_data, 1)
    random_nation = random.choice(nations)
    if random_nation not in already_invaded:
        already_invaded.append(random_nation)
        return random_nation
    else:
        get_random_nation(already_invaded)

if __name__ == "__main__":
    already_invaded = [None, "None"]
    while True:
        print("Press enter to get a random nation to invade.")
        holder = input("-: ")
        new_nation = get_random_nation(already_invaded)
        print(new_nation)
        already_invaded.append(new_nation)