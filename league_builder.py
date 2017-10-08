#Let's get started

import csv, random


players_list = []

#convert csv to list of dictionaries
def csv_converter():
    with open("soccer_players.csv") as csvfile:
        soccer_reader = csv.reader(csvfile, delimiter = ",")
        first_line = False
        for line in soccer_reader:
            if first_line == False:
                first_line = True
                continue
            else:
                players_list.append({"name":line[0],
                                     "height":line[1],
                                     "experience":line[2],
                                     "guardian":line[3]
                                     })
        return players_list

def experience(players_list):


    experienced = []
    inexperienced = []

    for kid in players_list:
        if kid["experience"] == "YES":
            experienced.append(kid)
        else:
            inexperienced.append(kid)
    return experienced, inexperienced


def build_list():

    players = csv_converter()

    experienced, inexperienced = experience(players)

    Raptors = []
    Sharks = []
    Dragons = []

    #randomly assign experienced kids to teams
    while experienced:
        if len(Raptors) < 2:
            Raptors.append(experienced.pop(random.randint(0,len(experienced)-1)))
        elif len(Raptors) == 2 and len(Sharks) < 2:
            Sharks.append(experienced.pop(random.randint(0,len(experienced)-1)))
        else:
            Dragons.append(experienced.pop(random.randint(0,len(experienced)-1)))

    #randomly assign inexperienced kids to teams
    while inexperienced:
        if len(Raptors) < 6:
            Raptors.append(inexperienced.pop(random.randint(0,len(inexperienced)-1)))
        elif len(Raptors) == 6 and len(Sharks) < 6:
            Sharks.append(inexperienced.pop(random.randint(0,len(inexperienced)-1)))
        else:
            Dragons.append(inexperienced.pop(random.randint(0,len(inexperienced)-1)))









