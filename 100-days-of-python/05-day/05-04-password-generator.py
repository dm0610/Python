##
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#full_lenght = input("What length of password do you want? Minimum 8 simbols\n")
full_lenght = random.randint(14,20)
strong_password = "Yes"
#strong_password = input("strong password? Yes or No:\n")
password = ""
if strong_password == "Yes":
    for i in range (0,int(full_lenght)):
        j = random.randint(1,100)
        if j < 60:
            password += letters[random.randint(1,len(letters)-1)]
        if j > 60 and j <= 80:
            password += numbers[random.randint(1,len(numbers)-1)]
        if j >= 80:
            password += symbols[random.randint(1,len(symbols)-1)]


elif strong_password == "No":
    for i in range (0,int(full_lenght)):
        j = random.randint(1,100)
        if j < 70:
            password += letters[random.randint(1,len(letters)-1)]
        if j >= 70:
            password += numbers[random.randint(1,len(numbers)-1)]
print(password)

    