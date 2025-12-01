def dial_rotation(direction: str, rotation: int, current_dial: int) -> int:
    if direction == "L":
        # Calculate the new dial position using modulo arithmetic
        return (current_dial - rotation) % 100
    elif direction == "R":
        # Calculate the new dial position using modulo arithmetic
        return (current_dial + rotation) % 100
    return current_dial
    
# Open the file in read mode
with open("day-1/input.txt", "r") as file:
    # Initialize a variable
    zero_count = 0
    current_dial = 50
    
    # Read through each line in the file
    for line in file:
        # Strip whitespace and process the line
        line = line.strip()
        
        # Example adjustment to the variable (you can replace this logic)
        if line.startswith("L"):
            current_dial = dial_rotation("L", int(line[1:]), current_dial)
        elif line.startswith("R"):
            current_dial = dial_rotation("R", int(line[1:]), current_dial)
        
        if current_dial == 0:
            zero_count += 1
    
    # Print the final result
    print("The dial has hit 0 this many times:", zero_count)