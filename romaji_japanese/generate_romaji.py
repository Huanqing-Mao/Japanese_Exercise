from random import *
from generate_romaji_whole import *

print("平仮名 Exercise")

# functions:
def initialise():
    print("Choose an option from below：")
    print("A. Whole set B.50 Pronounciations C.Others")

    opt = input("Option: ")
    if opt == 'A':
        return generate_whole()
    elif opt == 'B':
        return generate_romaji_50()
    else:
        return generate_rest() + generate_poly() + generate_special_poly()

def generate_romaji(lst):
    index = randint(0, len(lst) - 1)
    return lst[index]


def get_romaji_set(lst):
    result = []
    while len(result) < 5:
        new_romaji = generate_romaji(lst)
        if new_romaji not in result:
            result.append(new_romaji)
    return result
            
def get_result(lst):
    for i in range(5):
        print("Set#", i + 1, ": ")
        romaji_set = get_romaji_set(lst)
        for romaji in romaji_set:
            print("  - ", romaji)

# program body:
while True:
    lst = initialise()
    get_result(lst)
    next_step = input("Continue? YES/NO  :")
    if next_step != "YES":
        quit()



