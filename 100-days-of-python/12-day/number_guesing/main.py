from hello import hello
import random
from art import logo

choose_a_difficulty = 0
rand = int(random.randint(1,101))
def choose_difficulty():
    difficulty = input("Choose_a_difficulty. Type 'easy' or 'hard'")
    if difficulty.lower() == "easy":
        print("You have 10 attempts remaining to guess the number")
        return 10
    elif difficulty.lower() == "hard":
        print("You have 5 attempts remaining to guess the number")
        return 5
    else:
        print("Invalid difficulty")
        choose_difficulty()

def choose_number():
    global choose_a_difficulty
    global rand
    number = int(input("Make a guess: "))
    if number == rand:
        print("You are win!")
    elif number > rand:
        choose_a_difficulty = choose_a_difficulty - 1
        print(f"Too High. You have {choose_a_difficulty} chances")
        return choose_a_difficulty, choose_number()
    elif number < rand:
        choose_a_difficulty = choose_a_difficulty - 1
        print(f"Too Low. You have {choose_a_difficulty} chances")
        return choose_a_difficulty, choose_number()
    else:
        choose_a_difficulty = choose_a_difficulty - 1
        print(f"Something Wrong!. You have {choose_a_difficulty} chances")
        return choose_a_difficulty, choose_number()
    if choose_a_difficulty == 0:
        print("You are fail")

def main():
    print(logo)    
    hello()
    global choose_a_difficulty
    choose_a_difficulty = choose_difficulty()
    choose_number()

main()