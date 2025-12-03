import time
timed =time.perf_counter()
with open('/home/robdev/Desktop/Advent of Code/Advent_of_Code_Joltage_List.txt') as f:
    lines = [line.strip() for line in f]

result = 0

for line in lines:
    digits = [int(c) for c in line.strip()]
    n = len(digits)
    k = 12 

    chosen = []
    start = 0  

    for remaining in range(k, 0, -1):
        end = n - remaining

        max_digit = -1
        max_pos = -1
        for i in range(start, end + 1):
            d = digits[i]
            if d > max_digit:
                max_digit = d
                max_pos = i
                if d == 9: 
                    break

        chosen.append(max_digit)
        start = max_pos + 1  

    bank_value = 0
    for d in chosen:
        bank_value = bank_value * 10 + d

    result += bank_value

print("Finnished in ", (time.perf_counter()-timed)*1000, " ms")
print(result)
