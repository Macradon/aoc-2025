
def check_palindrome(num) -> bool:
    number_string = str(num)
    string_length = len(number_string)
    if string_length < 2:
        return False
    for Length in range(1, string_length // 2 + 1):
        if string_length % Length == 0:
            if number_string == number_string[:Length] * (string_length // Length):
                return True
    return False

with open("day-2/input.txt", "r") as file:
    total = 0
    for raw in file:
        line = raw.strip()
        ranges = line.split(",")
        for rng in ranges:
            bounds = rng.split("-")
            start = int(bounds[0])
            end = int(bounds[1])
            while start <= end:
                if check_palindrome(start):
                    total += int(start)
                start += 1
                
    print(total)