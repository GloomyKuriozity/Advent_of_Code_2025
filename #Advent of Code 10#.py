import time
import re
from itertools import combinations

timed = time.time()

import re

def apply_switch(state, switch):
    return [b ^ s for b, s in zip(state, switch)]

def apply_combo(start, switches, combo):
    state = start[:] 
    for idx in combo:
        state = apply_switch(state, switches[idx])
    return state

def find_min_solution(record):
    n = len(record["start"])  
    start = [0] * n          
    target = record["start"]    
    switches = record["switches"]

    n = len(switches)

    for r in range(1, n + 1):          
        for combo in combinations(range(n), r):
            end_state = apply_combo(start, switches, combo)
            if end_state == target:
                return combo  

    return None 

def pattern_to_bits(p: str) -> list[int]:
    return [1 if c == "#" else 0 for c in p]

def indices_to_mask(indices: list[int], n: int) -> list[int]:
    mask = [0] * n
    for i in indices:
        if 0 <= i < n:
            mask[i] = 1
        else:
            raise ValueError(f"Index {i} out of range for n={n}")
    return mask

def parse_lines(text: str):
    records = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        m = re.search(r"\[([.#]+)\]", line)
        if not m:
            raise ValueError(f"No [pattern] found in line: {line}")
        pattern = m.group(1)
        n = len(pattern)
        start_bits = pattern_to_bits(pattern)

        parens = re.findall(r"\(([^)]*)\)", line)
        switches = []
        for group in parens:
            group = group.strip()
            if group == "": 
                idxs = []
            else:
                idxs = [int(x.strip()) for x in group.split(",")]
            switches.append(indices_to_mask(idxs, n))

        records.append({
            "start": start_bits,
            "switches": switches,
        })

    return records


with open('/home/robdev/Desktop/Advent of Code/Advent_of_Code_diagrams.txt') as f:
    text = f.read()

data = parse_lines(text)

total = 0
for record in data:
    combo = find_min_solution(record)
    total += len(combo)
print(total)