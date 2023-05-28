from random import *
from generate_romaji_whole import *

print("\n###################")
print("  日本語　Exercise")
print("###################")

# functions:
def initialise():
    print("Choose an option from below：")
    print("A. Whole set B.50 Pronounciations C.Others")

    opt = input("Option: ")
    if opt.title() == 'A':
        return generate_whole()
    elif opt.title() == 'B':
        return generate_romaji_50()
    else:
        return generate_rest() + generate_poly() + generate_special_poly()

def numbers():
    num_sets = int(input("Number of sets: "))
    num_each_set = int(input("Number of Romaji in each set: "))
    return (num_sets, num_each_set)
    
    

def generate_romaji(lst):
    index = randint(0, len(lst) - 1)
    return lst[index]


def get_romaji_set(lst, n):
    result = []
    while len(result) < n:
        new_romaji = generate_romaji(lst)
        if new_romaji not in result:
            result.append(new_romaji)
    return result
            
def get_result(lst, s, n):
    for i in range(s):
        print("Set#", i + 1, ": ")
        romaji_set = get_romaji_set(lst, n)
        for romaji in romaji_set:
            print(f" - ", romaji)

# program body:
while True:
    lst = initialise()
    num_sets, num_each_set = numbers()
    get_result(lst, num_sets, num_each_set)
    next_step = input("Continue? YES/NO  :")
    if next_step.upper().strip() != "YES":
        quit()



