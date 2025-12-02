import numpy as np

with open('/home/robdev/Desktop/Advent of Code/Advent_of_Code_ID_List.txt') as f:
    lines = f.read().split(',')

stripped = [p.split(',') for p in lines]

def is_invalid(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

def find_invalid_in_range(start, end):
    return [n for n in range(start, end+1) if is_invalid(n)]

for element in stripped:
    cleaned = [p.split('-') for p in element]

    start = int(cleaned[0][0])
    end = int(cleaned[0][1])

    print(find_invalid_in_range(start, end))
