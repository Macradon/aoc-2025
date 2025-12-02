with open("day-2/input.txt", "r") as file:
    total = 0
    for raw in file:
        line = raw.strip()
        ranges = line.split(",")
        for range in ranges:
            bounds = range.split("-")
            start = int(bounds[0])
            end = int(bounds[1])
            while start <= end:
                firstpart, secondpart = str(start)[:len(str(start))//2], str(start)[len(str(start))//2:]
                if firstpart == secondpart:
                    print(f"First part: {firstpart}, Second part: {secondpart}")
                    total += int(start)
                start += 1
                
    print(total)
