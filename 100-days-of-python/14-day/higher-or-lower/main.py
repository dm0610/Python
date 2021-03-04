from game_data import data
from art import logo, vs
import random
import os


def viewer(first_blogger = {}, second_blogger = {}):
    print(logo)
    print(f""" 
    A) name:            {first_blogger['name']}
       description:     {first_blogger['description']}
       country:         {first_blogger['country']}
    {vs}
    B) name:            {second_blogger['name']}
       description:     {second_blogger['description']}
       country:         {second_blogger['country']}
    """)


def controller(first_blogger, second_blogger, win_counter):
    a = first_blogger['follower_count']
    b = second_blogger['follower_count']

    choise = input("Who has more fallovers, 'A' or 'B'? ")
    if a > b:
        if choise.lower() == 'a':
            print("YES!")
            win_counter  = win_counter + 1
            return True, win_counter
        else: 
            print("NO!")
            return False, win_counter

    else:
        if choise.lower() == 'b':
            print("YES!")
            win_counter  = win_counter + 1
            return True, win_counter
        else: 
            print("NO!")
            return False, win_counter


def action_point(ingame, win_counter): 
    if ingame == False:
        print(f"You win {win_counter} times")
    flag = input("Do you want to continue? 'y' or 'n'")
    if flag.lower() == 'y':
        os.system('cls||clear')
        return True, win_counter
    else:
        print(f"You win {win_counter} times")
        return False, win_counter
    

def game(ingame):
    win_counter = 0
    while ingame == True:
        first_blogger_id = random.randint(1,len(data)-1)
        second_blogger_id = random.randint(1,len(data)-1)
        if first_blogger_id == second_blogger_id: 
            while first_blogger_id == second_blogger_id:
                second_blogger_id = random.randint(1,len(data)-1)

        viewer(data[first_blogger_id], data[second_blogger_id])

        ingame, win_counter = controller(data[first_blogger_id], data[second_blogger_id], win_counter)

        if ingame == False:
            print(f"win_counter: {win_counter}")
            break
        
        ingame, win_counter = action_point(ingame, win_counter)

        
game(True)
        

