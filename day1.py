import pandas as pd

# Day 1:
input_day1 = pd.read_csv('day1input.txt', names=['input'])
values = input_day1['input']
# Part 1: Calculate sum of input, starting from 0.
def day1_part1(input):
    sumofall = sum(input)
    return sumofall


# Part 2: What is the first frequency input reaches twice?
def day1_part2(input):
    frequency = 0
    duplicates = set()
    while True:
        for i in input:
            frequency += i
            if frequency in duplicates:
                return frequency
            else:
                duplicates.add(frequency)

if __name__ == '__main__':
    print(day1_part1(values))
    print(day1_part2(values))
