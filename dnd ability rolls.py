import random, math

Abilities = {"Strength":8 ,"Dexterity":8 ,"Constitution":8 ,"Intelligence":8 ,"Wisdom":8 ,"Charisma":8 }

statrolls = []

print(Abilities)

for i in range(1, 7): #operation to roll 4d6 and sum the the 3 highest to produce a statroll and finally add the statroll to the list of statrolls six times.
    d6rolls = list(random.randrange(1, 7) for i in range(4))
    print("roll number", i,":")
    statroll = sorted(d6rolls)[3] + sorted(d6rolls)[2] + sorted(d6rolls)[1]
    print("stat roll:", statroll, "\n")
    statrolls.append(statroll)

print("your ability stat rolls:",statrolls)
while str(input("\n enter r to re-roll otherwise press enter."))=="r":
    statrolls = sorted(sum(sorted(random.randrange(1, 7) for i in range(4)[1:])) for j in range(6)) # this is the same as the operation above
    print("your new statrolls", statrolls)


def assigningrolls():

    print("type in the roll number of the stat roll you would like to assign (a roll number can only be assigned once).\n")
    for Ability in Abilities:

        rollindex = int(input(Ability + ": ")) -1
        print(statrolls[rollindex])

        while 0>rollindex or rollindex>5:
                print("please type one of the roll numbers")
                rollindex = int(input()) -1
        while statrolls[rollindex] == 1:
            print("please type a roll number that has not already been assigned")
            rollindex = int(input()) -1

        Abilities[Ability] = statrolls[rollindex]

        statrolls[rollindex] = 1

assigningrolls()

print(Abilities, "\n")

print("Race options:Human, Elf, Dwarf, Dragonborn, Gnome, Half-Elf, Half-Orc, Halfling and Tiefling \nChoose a race by entering it in now (exactly as it's spelt ^)\n")
Race = str(input())

def race_abilities():
    if Race == "Human":
        for Ability in Abilities:
            Abilities[Ability] = Abilities[Ability] +1
        print("All ablitlities +1")
    if Race == "Elf":
        Abilities["Dexterity"] = Abilities["Dexterity"] +2
        print("Dexterity +2")
    if Race == "Dwarf":
        Abilities["Constitution"] = Abilities["Constitution"] +2
        print("Constitution +2")
    if Race == "Dragonborn":
        Abilities["Strength"] = Abilities["Strength"] +2
        Abilities["Charisma"] = Abilities["Charisma"] +1
        print("Strength +2 and Charisma +1")
    if Race == "Gnome":
        Abilities["Intelligence"] = Abilities["Intelligence"] +2
        print("Intelligence +2")
    if Race == "Half-Elf":
        Abilities["Charisma"] = Abilities["Charisma"] +2
        print("You can choose to increase the Ability Scores of two abilities by +1 apart from Charisma.\n please enter the first ability of your choice (spelling correctly and capitalize the frist letter)")
        x = str(input())
        Abilities[x] = Abilities[x] +1
        print("now please enter the second ability of your choice")
        y = str(input())
        Abilities[y] = Abilities[y] +1
    if Race == "Half-Orc":
        Abilities["Strength"] += 2
        Abilities["Constitution"] += 1
        print("Strength +2 and Constitution +1")
    if Race == "Halfling":
        Abilities["Dexterity"] += 2
        print("Dexterity +2")
    if Race == "Tiefling":
        Abilities["Intelligence"] += 1
        Abilities["Charisma"] += 2
        print("Intelligence +1 and Charisma +2") #race abilities

race_abilities()

print("\nThese are your Ability Scores:\n", Abilities, "\n")

Modifier = {"Strength":-5 ,"Dexterity":-5 ,"Constitution":-5 ,"Intelligence":-5 ,"Wisdom":-5 ,"Charisma":-5 }

def Mod():
    for i in Modifier:
        Modifier[i] += math.floor(Abilities[i]/2)

Mod()

print("These are your Modifiers:\n", Modifier, "\n")

name = input("name your character: ")

with open(str(name) + ".txt", "w") as out_file:

    out_file.write("Character name: " + name + "\nRace: " + Race + "\nAbilities:\n")

    for Ability in Abilities:
        out_string = ""
        out_string += str(Ability) + ":" + str(Abilities[Ability]) + ", "
        out_file.write(out_string)


input("press enter to close")
