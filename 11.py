from functools import lru_cache

result = []

def parse_graph(text: str) -> dict[str, list[str]]:
    g = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        left, right = line.split(":", 1)
        src = left.strip()
        outs = right.strip().split() if right.strip() else []
        g[src] = outs
    return g

def count_paths(graph: dict[str, list[str]], start="you", end="out") -> int:
    @lru_cache(None)
    def ways(node: str) -> int:
        if node == end:
            return 1
        return sum(ways(nxt) for nxt in graph.get(node, []))

    return ways(start)

def count_paths_with_constraints(graph, start="svr", end="out",
                                  must1="dac", must2="fft"):
    @lru_cache(None)
    def ways(node, seen1, seen2):
        # Update flags when entering node
        if node == must1:
            seen1 = True
        if node == must2:
            seen2 = True

        if node == end:
            return 1 if (seen1 and seen2) else 0

        return sum(
            ways(nxt, seen1, seen2)
            for nxt in graph.get(node, [])
        )

    return ways(start, False, False)

with open('C:/Users/melan/Desktop/SoftDev/Advent of Code/11_data.txt') as f:
    text = f.read()

g = parse_graph(text)

print(count_paths_with_constraints(g))
#print(count_paths(g, "you", "out"))