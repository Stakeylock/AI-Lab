def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)

if __name__ == "__main__":
    n = int(input("Enter number of disks: "))
    print(f"\nSteps to solve Tower of Hanoi for {n} disks:\n")
    hanoi(n, 'A', 'B', 'C')
