def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = [' '.join(str(rod) for rod in rods)]

    def move(disks, source, auxiliary, target):
        if disks == 0:
            return
        move(disks - 1, source, target, auxiliary)
        rods[target].append(rods[source].pop())
        states.append(' '.join(str(rod) for rod in rods))
        move(disks - 1, auxiliary, source, target)

    move(n, 0, 1, 2)
    return '\n'.join(states)


# Example usage
if __name__ == "__main__":
    print(hanoi_solver(3))