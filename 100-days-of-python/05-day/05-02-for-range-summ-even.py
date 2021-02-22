total = 0 

for number in range(0, 101):
    if number%2 == 0:
        total += number
        #print("number:", number, "; total:", total )

for number in range(0, 101, 2):
        total += number
        print("number:", number, "; total:", total )