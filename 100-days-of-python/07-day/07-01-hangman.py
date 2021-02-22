import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#word = list(word_list[random.randint(0,len(word_list)-1)])
word = list(random.choice(word_list))

empty_list = []
for i in range(0,len(word)):
    empty_list.append("_")
print(word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

while '_' in empty_list:
    letter = input("Input letter: ")
    while letter in word:
        #print(word.index(letter))
        empty_list[word.index(letter)] = letter
        word[word.index(letter)] = "_"
    print(empty_list)