import bisect

with open("/home/robdev/Desktop/Advent of Code/Advent_of_Code_ingredients.txt") as f:
    sections = f.read().strip().split("\n\n")

ranges_part = sections[0].splitlines()
ranges_part = [p.split('-') for p in ranges_part]
ranges_part = [list(map(int,pair)) for pair in ranges_part]
ids_part    = sections[1].splitlines()

result = 0

def merge_ranges(ranges):
    if not ranges:
        return []

    ranges = sorted(ranges, key=lambda x: x[0])
    merged = [list(ranges[0])] 

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end + 1:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return [tuple(r) for r in merged]


def id_in_ranges(id_value, merged):
    starts = [r[0] for r in merged]

    idx = bisect.bisect_right(starts, id_value) - 1

    if idx < 0:
        return False

    start, end = merged[idx]
    return start <= id_value <= end


merge = merge_ranges(ranges_part)

for i in range(len(merge)):
    result += merge[i][1] - merge[i][0] + 1
    

print(result)