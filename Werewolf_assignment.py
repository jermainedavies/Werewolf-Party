import random

#ask how many players
seers = 1
doctors = 1
player_number = int(input("how many players?"))
if player_number >= 7:
    print(f"there are {player_number} players in this game")
    if player_number <16:
        werewolves = 2
        print(f"there are {werewolves} werewolves in this game")
    else:
        werewolves = 3
        print(f"there are {werewolves} werewolves in this game")


    villagers = player_number - seers - doctors - werewolves

    players = [
        ]
    role_numbers = []
    role_numbers_final = []
    role_names = []
    player_number_ask = player_number
    count = player_number
    count2 = player_number
    player_number_append = player_number
    randomised_roles_count = player_number
    temp = None

    while count > 0:  
        temp = random.randint(1,player_number)
        #print(temp)
        if temp not in role_numbers:
            role_numbers.append(temp)
            count -=1
    #print(role_numbers)

    while player_number_append > 0:
        players.append(f"player {player_number_append}")
        player_number_append -= 1

    #print(players)

    #assign random numbers to each player, then assign new numbers to each role (numbers cannot repeat)

    # 1 seer
    while seers >0:
        role_names.append(f"Seer {seers}")
        seers -= 1

    # *werewolves
    while werewolves >0:
        role_names.append(f"Werewolf {werewolves}")
        werewolves -= 1

    # 1 doctor

    while doctors >0:
        role_names.append(f"Doctor {doctors}")
        doctors -= 1

    #remaining players are villagers
    while villagers >0:
        role_names.append(f"Villager {villagers}")
        villagers -= 1


    randomised_roles = random.shuffle(role_names)


    #print(f" randomised roles are {randomised_roles}")

    while count2 > 0:  
        temp2 = random.randint(1,player_number)
        #print(temp2)
        if temp2 not in role_numbers_final:
            role_numbers_final.append(temp2)
            count2 -=1

    while player_number_ask > 0:
        for role in role_names:
            print("you are player ", player_number_ask, " and your role number is ", role)
            player_number_ask -=1
            input("please press enter to confirm your role")
else:
    print("Sorry, you need at least 7 players for this game")

