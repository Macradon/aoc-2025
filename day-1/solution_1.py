def dial_rotation(direction: str, rotation: int, current_dial: int) -> int:
    if direction == "L":
        return (current_dial - rotation) % 100
    elif direction == "R":
        return (current_dial + rotation) % 100
    return current_dial
    
with open("day-1/input.txt", "r") as file:
    zero_count = 0
    current_dial = 50
    
    for line in file:
        line = line.strip()
        
        if line.startswith("L"):
            current_dial = dial_rotation("L", int(line[1:]), current_dial)
        elif line.startswith("R"):
            current_dial = dial_rotation("R", int(line[1:]), current_dial)
        
        if current_dial == 0:
            zero_count += 1
    
    print("The dial has hit 0 this many times:", zero_count)