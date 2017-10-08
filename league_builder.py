#Let's get started

import csv, random


#convert csv to list of dictionaries
def csv_converter():
    players_list = []
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

    #make separate lists for kids with experience and kids w/o experience
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
        if len(Raptors) < 3:
            Raptors.append(experienced.pop(random.randint(0,len(experienced)-1)))
        elif len(Raptors) == 3 and len(Sharks) < 3:
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

    write_team_list(Raptors, Sharks, Dragons)

    write_welcome_letters(Raptors, Sharks, Dragons)


#write teams to team list
def write_team_list(Raptors, Sharks, Dragons):
    with open("teams.txt", "w") as team_list:
        team_list.write("This is the list for this year's teams. \n")

    with open("teams.txt", "a") as team_list:
        team_list.write("Raptors \n")
        for player in Raptors:
            team_list.write(player["name"]+", " + player["experience"] + ", " + player["guardian"] + "\n")
        team_list.write("\n")

        team_list.write("Sharks \n")
        for player in Sharks:
            team_list.write(player["name"]+", " + player["experience"] + ", " + player["guardian"] + "\n")
        team_list.write("\n")

        team_list.write("Dragons \n")
        for player in Dragons:
            team_list.write(player["name"]+", " + player["experience"] + ", " + player["guardian"] + "\n")
        team_list.write("\n")

#create welcome list for parents
def write_welcome_letters(Raptors, Sharks, Dragons):
    for player in Raptors:
        with open(str(player["name"].replace(" ","_")) + ".txt", "w") as letter:
            letter.write("Dear {guardian},\nYour child, {name}, will be playing on the Raptors this year. \n"
                         "You will meet the team's coach and the other kids on the team at the team's \n"
                         "first practice on October 15th, 4:00 PM at the Beach Chalet Fields in Golden Gate Park. \n"
                         "Practice will last one hour.".format(**player))

    for player in Sharks:
        with open(str(player["name"].replace(" ", "_")) + ".txt", "w") as letter:
            letter.write("Dear {guardian},\nYour child, {name}, will be playing on the Sharks this year. \n"
                         "You will meet the team's coach and the other kids on the team at the team's \n"
                         "first practice on October 15th, 5:00 PM at the Beach Chalet Fields in Golden Gate Park. \n"
                         "Practice will last one hour.".format(**player))

    for player in Dragons:
        with open(str(player["name"].replace(" ", "_")) + ".txt", "w") as letter:
            letter.write("Dear {guardian},\nYour child, {name}, will be playing on the Dragons this year. \n"
                         "You will meet the team's coach and the other kids on the team at the team's \n"
                         "first practice on October 15th, 6:00 PM at the Beach Chalet Fields in Golden Gate Park. \n"
                         "Practice will last one hour.".format(**player))




if __name__ == "__main__":
    build_list()








