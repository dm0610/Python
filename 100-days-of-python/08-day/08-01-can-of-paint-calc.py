
import math

def canOfPaintCalc(heihgt, width, coverage):
    numOfCans = math.ceil((heihgt * width) / coverage)
    print(f"You need {numOfCans} cans of paint")

parameters = list(input("Input height, width, coverage-per-can: ").split())

canOfPaintCalc(heihgt=float(parameters[0]), width=float(parameters[1]), coverage=float(parameters[2]))

