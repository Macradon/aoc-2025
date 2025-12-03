def find_largest_joltage(battery_bank: str) -> int:
    current_largest_joltage = 0
    first_joltage_digit = 0
    second_joltage_digit = 0
    batteries = list(battery_bank)
    bank_length = len(batteries)
    i = 0
    print("Checking battery bank:", batteries)

    while i < bank_length:
        if i == (bank_length - 1):
            if int(battery_bank[i]) > second_joltage_digit:
                second_joltage_digit = int(battery_bank[i])
        else:
            if int(battery_bank[i]) > first_joltage_digit:
                new_first_joltage_digit = int(battery_bank[i])
                new_second_joltage_digit = 0
                if int(str(new_first_joltage_digit) + str(new_second_joltage_digit)) > current_largest_joltage:
                    first_joltage_digit = new_first_joltage_digit
                    second_joltage_digit = new_second_joltage_digit
            elif int(battery_bank[i]) > second_joltage_digit:
                second_joltage_digit = int(battery_bank[i])
        i += 1
    largest_joltage = str(first_joltage_digit) + str(second_joltage_digit)
    print(largest_joltage)
    print("-----")
    return int(largest_joltage)

with open("day-3/input.txt", "r") as file:
    total = 0
    for line in file:
        total += find_largest_joltage(line.strip())
                
    print(total)