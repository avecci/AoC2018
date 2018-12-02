import pandas as pd
import collections
from collections import Counter, defaultdict
from functools import reduce

input_day2 = pd.read_csv('day2input.txt', names=['input'])

values = input_day2['input']
values = values.tolist()

#Day 2 part 1: Calculate checksum by counting the unique occurrence of characters in each input string and multiplying result
def checksum(input):
    occurrences = []
    for element in input:
        lista = list(collections.Counter(element).items())
        lista = dict(lista)
        lista = dict((key,value) for key,value in lista.items() if value > 1)
        occurrences += sorted(set([i for i in lista.values()]))

    count_of_occurrences = Counter(occurrences).values()
    result = reduce(lambda x, y: x*y, count_of_occurrences)
    return result

#print('Checksum:',checksum(values))

# Part 2: First find the most common boxes - ones that differ least.
#Then print the letters that do not differ.
def findboxes(input):
    for i,firstbox in enumerate(input[:-1]):
        for secondbox in input[i+1:]:
            similarities = [t for t, s in zip(firstbox,secondbox) if t==s]
            return 'Boxes that have similar id:', firstbox,secondbox, 'Common characters:', ''.join(similarities)

#print(findboxes(values))
