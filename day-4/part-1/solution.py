def check_for_space(lines: list[str], row_index: int, check_symbol: str) -> int:
    total_accessible = 0
    rows = len(lines)
    row = lines[row_index]

    for column, character in enumerate(row):
        if character != check_symbol:
            continue

        neighbor_count = 0
        for row_delta in (-1, 0, 1):
            for column_delta in (-1, 0, 1):
                if row_delta == 0 and column_delta == 0:
                    continue

                neighbor_row = row_index + row_delta
                neighbor_column = column + column_delta
                if 0 <= neighbor_row < rows and 0 <= neighbor_column < len(lines[neighbor_row]) and lines[neighbor_row][neighbor_column] == check_symbol:
                    neighbor_count += 1

        if neighbor_count < 4:
            total_accessible += 1

    return total_accessible

with open("day-4/input.txt", "r") as file:
    lines = file.read().splitlines()

    total = 0
    for row_index in range(len(lines)):
        total += check_for_space(lines, row_index, "@")

    print(total)