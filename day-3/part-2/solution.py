def find_largest_joltage(battery_bank: str) -> int:
    joltage_stack = []
    joltage_size = 12
    batteries = list(battery_bank)
    bank_length = len(batteries)
    jump_off_point = bank_length - joltage_size
    print("Checking battery bank:", batteries)

    for battery in batteries:
        while joltage_stack and jump_off_point > 0 and joltage_stack[-1] < battery:
            joltage_stack.pop()
            jump_off_point -= 1
        joltage_stack.append(battery)
        
    print(joltage_stack)
    print("-----")
    return int("".join(map(str,joltage_stack[:joltage_size])))

with open("day-3/input.txt", "r") as file:
    total = 0
    for line in file:
        total += find_largest_joltage(line.strip())
                
    print(total)