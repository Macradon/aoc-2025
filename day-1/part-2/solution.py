def dial_rotation(direction: str, rotation: int, current_dial: int) -> tuple:
    if direction == "L":
        new_dial = (current_dial - rotation) % 100
        # Count how many times we hit 0 when moving left.
        # First step index that lands on 0 is k1 = current_dial (unless current_dial==0 then k1=100).
        k1 = current_dial if current_dial != 0 else 100
        if rotation < k1:
            crossings = 0
        else:
            crossings = (rotation - k1) // 100 + 1
        if crossings > 0:
            print("turning", current_dial, direction, rotation)
            print("new position", new_dial, "crossings", crossings)
    elif direction == "R":
        new_dial = (current_dial + rotation) % 100
        # Count how many times we hit 0 when moving right.
        # First step index that lands on 0 is k1 = (100 - current_dial) if current_dial != 0 else 100.
        k1 = (100 - current_dial) if current_dial != 0 else 100
        if rotation < k1:
            crossings = 0
        else:
            crossings = (rotation - k1) // 100 + 1
        if crossings > 0:
            print("turning", current_dial, direction, rotation)
            print("new position", new_dial, "crossings", crossings)
    
    return new_dial, crossings
    
if __name__ == "__main__":
    with open("day-1/input.txt", "r") as file:
        crossing_count = 0
        current_dial = 50

        for line in file:
            line = line.strip()

            if line.startswith("L"):
                current_dial, crossings = dial_rotation("L", int(line[1:]), current_dial)
                crossing_count += crossings
            elif line.startswith("R"):
                current_dial, crossings = dial_rotation("R", int(line[1:]), current_dial)
                crossing_count += crossings

        print("The dial has crossed the boundary this many times:", crossing_count)