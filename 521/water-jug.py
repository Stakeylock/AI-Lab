def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def pour(toCap, fromCap, d):
    fromJug = fromCap
    toJug = 0
    steps = [(fromJug, toJug)]

    while fromJug != d and toJug != d:
        temp = min(fromJug, toCap - toJug)

        toJug += temp
        fromJug -= temp
        steps.append((fromJug, toJug))

        if fromJug == d or toJug == d:
            break

        if fromJug == 0:
            fromJug = fromCap
            steps.append((fromJug, toJug))

        if toJug == toCap:
            toJug = 0
            steps.append((fromJug, toJug))

    return steps

def min_steps(n, m, d):
    if d > max(n, m):
        return None

    if d % gcd(n, m) != 0:
        return None

    s1 = pour(n, m, d)
    s2 = pour(m, n, d)

    return s1 if len(s1) <= len(s2) else s2

if __name__ == "__main__":
    n = int(input("Enter capacity of jug 1: "))
    m = int(input("Enter capacity of jug 2: "))
    d = int(input("Enter required amount: "))

    steps = min_steps(n, m, d)

    if steps is None:
        print("\nNo solution possible")
    else:
        print("\nSteps (Jug1, Jug2):")
        for i, (a, b) in enumerate(steps):
            print(f"Step {i}: ({a}, {b})")
        print("\nMinimum number of steps required:", len(steps) - 1)
