#Check if number is prime or composite
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == True: 
        print(f"Number \"{number}\" is prime")
    else: print(f"Number \"{number}\" is composite")

prime_checker(int(input("input number: ")))