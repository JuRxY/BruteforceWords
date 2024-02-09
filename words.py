import itertools
import math


def generate(list, word_length):
    yield from itertools.permutations(list, word_length)

def generate_possibilities(letters: str):
    #open("possibilities.txt", "w").close()
    letters = letters.lower()

    slovar = []
    with open('sbsj.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() != "": slovar.append(line.strip())

    possibilities_list = []
    length = len(letters)
    total_possibilities = sum(math.factorial(length) // math.factorial(length - i) for i in range(3, length + 1))
    #? print(f"There are `{total_possibilities}` possibilities")
    #with open("wordlist.txt", "r") as f:
    #    global seznam_besed
    #    seznam_besed = f.read().splitlines()

    for i in range(3, length + 1):
        for j in generate(letters, i):
            word = "".join(j)
            possibilities_list.append(word) #! ig da to converta use tuple u en list povn stringou
            #with open("possibilities.txt", "a") as f:
            #    f.write("".join(j) + "\n")

    #return list(set(possibilities_list)-(set(possibilities_list) - set(slovar)))
    return list(set(possibilities_list)-(set(possibilities_list) - set(slovar)))

# pos = generate_possibilities("")
# print(longest)