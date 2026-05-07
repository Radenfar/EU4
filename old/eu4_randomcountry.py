import random

def file_to_list(filename):
    fileobj=open(filename)
    lines=[]
    for line in fileobj:
        lines.append(line.strip())
    return lines

nations = file_to_list("eu4_countries.txt")
while True:
    ui = input("-: ")
    print(random.choice(nations))