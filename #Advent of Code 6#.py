from math import prod

with open("/home/robdev/Desktop/Advent of Code/Advent_of_Code_worksheet.txt") as f:
    rows = [line.rstrip('\n') for line in f]

#Part 1
""" columns = list(map(list, zip(*rows)))

columns = columns[::-1]

parsed_columns = []
for col in columns:
    nums = list(map(int, col[:4]))
    sign = col[4]
    parsed_columns.append(nums + [sign])


result = 0

for nums0, nums1, nums2, nums3, sign in parsed_columns:
    nums = [nums0, nums1, nums2, nums3] 
    match sign:
        case '+':
            result += sum(nums[:4])
        case '*':
            result += prod(nums[:4]) """

#Part 2
H = len(rows)
W = len(rows[0])
digit_rows = H - 1

result = 0
c = W - 1

while c >= 0:
    if all(rows[r][c] == ' ' for r in range(H)):
        c -= 1
        continue

    numbers = []
    op = None

    while c >= 0 and not all(rows[r][c] == ' ' for r in range(H)):
        digits = [rows[r][c] for r in range(digit_rows)]
        num_str = ''.join(ch for ch in digits if ch != ' ')
        numbers.append(int(num_str))

        if rows[H - 1][c] != ' ':
            op = rows[H - 1][c]

        c -= 1

    if op == '+':
        result += sum(numbers)
    elif op == '*':
        result += prod(numbers)
    else:
        raise ValueError("No operator found for a problem block")

print(result)