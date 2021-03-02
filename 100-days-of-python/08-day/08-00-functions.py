#without inputs
def func1():
    print("Hello World!")
    print("How are you?")
func1()

#with inputs
def func2(name):
    print(f"Hello, {name}!")
func2("Mike")

#with multiple inputs
def func3(name, age, adress):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Adress: {adress}")
func3("Mike", "35 y.o.", "Sportivnaya 134/17")