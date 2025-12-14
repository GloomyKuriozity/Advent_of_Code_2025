import time
import re
from itertools import combinations

timed = time.time()

"""def apply_switch(state, switch):
    return [b ^ s for b, s in zip(state, switch)]

def apply_combo(start, switches, combo):
    state = start[:] 
    for idx in combo:
        state = apply_switch(state, switches[idx])
    return state"""

def press_once(state, switch, target):
    nxt = []
    for v, inc, t in zip(state, switch, target):
        nv = v + inc
        if nv > t:    
            return None
        nxt.append(nv)
    return nxt

"""def find_min_solution(record):
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

    return None """

def find_min_presses(record):
    from ortools.sat.python import cp_model

    target = record["target"]
    switches = record["switches"]
    n = len(target)
    m = len(switches)

    model = cp_model.CpModel()
    ub = max(target)

    x = [model.NewIntVar(0, ub, f"x{j}") for j in range(m)]
    for i in range(n):
        model.Add(sum(switches[j][i] * x[j] for j in range(m)) == target[i])
    model.Minimize(sum(x))

    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = 8
    solver.parameters.max_time_in_seconds = 10.0

    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None

    return int(solver.Value(sum(x)))


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

        tm = re.search(r"\{([^}]*)\}", line)
        if not tm:
            raise ValueError(f"No {{target}} found in line: {line}")
        target = [int(x.strip()) for x in tm.group(1).split(",") if x.strip()]

        if len(target) != n:
            raise ValueError(f"Target length {len(target)} != pattern length {n} in line: {line}")

        

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
            "n": n,
            "target": target,
            "switches": switches,
        })       

    return records


with open('C:/Users/melan/Desktop/SoftDev/Advent of Code/10_data.txt') as f:
    text = f.read()

data = parse_lines(text)

total = 0
for record in data:
    presses = find_min_presses(record)
    if presses is None:
        raise RuntimeError("No solution")
    tim = time.time() - timed
    total += presses

print(total)
print("Time:", time.time() - timed)
