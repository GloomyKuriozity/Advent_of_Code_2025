#Advent of Code 1#

point = 50
password = 0

with open('/home/robdev/Desktop/Advent of Code/Advent_of_Code_Rotation_List.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    line = line.strip()
    if not line:
        continue

    direction = line[0]
    distance = int(line[1:])

    start = point

    match direction:
        case 'R':
            # how many times we land on 0 while going right
            if start == 0:
                first = 100
            else:
                first = 100 - start

            if distance >= first:
                password += 1 + (distance - first) // 100

            point += distance

        case 'L':
            # how many times we land on 0 while going left
            if start == 0:
                first = 100
            else:
                first = start

            if distance >= first:
                password += 1 + (distance - first) // 100

            point -= distance 

        case _:
            continue

    # wrap into 0 - 99
    point = (point % 100 + 100) % 100
    
    
print("Password:", password)