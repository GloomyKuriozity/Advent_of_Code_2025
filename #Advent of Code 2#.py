with open('/home/robdev/Desktop/Advent of Code/Advent_of_Code_ID_List.txt') as f:
    lines = f.read().split(',')

stripped = [p.split(',') for p in lines]
results = 0

def is_invalid(n):
    s = str(n)
    L = len(s)

    for k in range(1, L):
        if L % k == 0:                 
            block = s[:k]
            if block * (L // k) == s:     
                return True

    return False

def find_invalid_in_range(start, end):
    tab = [n for n in range(start, end+1) if is_invalid(n)]
    if tab != []:
        return sum(tab)
    return 0


for element in stripped:
    cleaned = [p.split('-') for p in element]

    start = int(cleaned[0][0])
    end = int(cleaned[0][1])

    results += find_invalid_in_range(start, end)

print(results)
