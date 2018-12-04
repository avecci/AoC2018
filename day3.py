import pandas as pd

input_day3 = pd.read_csv('day3input.txt', sep=' ', names=['index','atsign','coordinates','area'])


def overlap(input):
    '''Day 3: Count overlapping pixels of a cloth. Part 2 of the day solution is missing yet.'''
    def clrdata(input):
        input['coordinates'] = input['coordinates'].str.replace(':','')
        input['area'] = input['area'].str.replace('x',',')
        return input

    area = 1000
    cloth = pd.DataFrame('.', index=[x for x in range(0,area)], columns=[x for x in range(0,area)])

    for runner in range(0,len(input)):
        for areaint in range(runner,runner+1):
            for coordint in range(runner,runner+1):
                for i in range(0, int(clrdata(input)['area'][areaint].split(',')[0])):
                    for j in range(0,int(clrdata(input)['area'][areaint].split(',')[1])):
                        if cloth.at[int(clrdata(input)['coordinates'][coordint].split(',')[1])+j,int(clrdata(input)['coordinates'][coordint].split(',')[0])+i] != '.':
                            cloth.at[int(clrdata(input)['coordinates'][coordint].split(',')[1])+j,int(clrdata(input)['coordinates'][coordint].split(',')[0])+i] = 'T'
                        else:
                            cloth.at[int(clrdata(input)['coordinates'][coordint].split(',')[1])+j,int(clrdata(input)['coordinates'][coordint].split(',')[0])+i] = 'X'

    num = 0
    for i in range(len(cloth)):
        num += cloth[i].str.count('T')
    return sum(num)

if __name__ == '__main__':
    print(overlap(input_day3))
