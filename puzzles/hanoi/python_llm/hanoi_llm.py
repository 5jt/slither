def print_towers(towers):
    print("\nCurrent Towers State:")
    for name in "ABC":
        print(f"{name}: {towers[name]}")
    print("-" * 30)

def move(n, source, target, auxiliary, towers):
    if n == 1:
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Move disk {disk} from {source} to {target}")
        print_towers(towers)
    else:
        move(n - 1, source, auxiliary, target, towers)
        move(1, source, target, auxiliary, towers)
        move(n - 1, auxiliary, target, source, towers)

def tower_of_hanoi(n):
    # Initialize towers
    towers = {
        "A": list(reversed(range(1, n + 1))),  # Start with all disks on tower A
        "B": [],
        "C": []
    }

    print("Initial Towers State:")
    print_towers(towers)

    # Start the recursive process
    move(n, "A", "C", "B", towers)

# Example usage:
if __name__ == "__main__":
    height = int(input("Enter the height of the tower: "))
    tower_of_hanoi(height)
