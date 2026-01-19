import heapq

goal = (0,1,2,3,4,5,6,7,8)
moves = [(1,0),(-1,0),(0,1),(0,-1)]
pos = {v:(i//3,i%3) for i,v in enumerate(goal)}

def h(s):
    return sum(
        abs(i//3 - (v//3)) + abs(i%3 - (v%3))
        for i, v in enumerate(s)
        if v != 0
    )

def solve(start):
    pq = [(h(start), 0, start, start.index(0))]
    parent = {start: None}
    seen = set()

    while pq:
        f, g, s, z = heapq.heappop(pq)
        if s in seen:
            continue
        seen.add(s)

        if s == goal:
            path = []
            while s:
                path.append(s)
                s = parent[s]
            for s in reversed(path):
                for i in range(0, 9, 3):
                    print(*s[i:i+3])
                print()
            return

        x, y = divmod(z, 3)
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nz = nx * 3 + ny
                ns = list(s)
                ns[z], ns[nz] = ns[nz], ns[z]
                ns = tuple(ns)
                if ns not in seen:
                    parent[ns] = s
                    heapq.heappush(pq, (g + 1 + h(ns), g + 1, ns, nz))

if __name__ == "__main__":
    start = (7,0,5,6,3,1,2,4,8)
    solve(start)
