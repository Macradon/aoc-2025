def check_for_space(lines: list[str], row_index: int, check_symbol: str) -> dict[str, any]:
    total_accessible = 0
    rows = len(lines)
    row = lines[row_index]
    deletion_line = []

    for column, character in enumerate(row):
        if character != check_symbol:
            deletion_line.append(".")
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
            deletion_line.append(".")
            total_accessible += 1
        else:
            deletion_line.append(check_symbol)

    return {"deletion_line": deletion_line, "removed_count": total_accessible}

def pass_grid(grid: list[list[str]], symbol: str) -> dict[str, any]:
    removed_total = 0
    new_grid = []
    for row_index in range(len(grid)):
        check_output = check_for_space(grid, row_index, symbol)
        new_grid.append(check_output["deletion_line"])
        removed_total += check_output["removed_count"]

    return {"new_grid": new_grid, "removed_count": removed_total}

with open("day-4/input.txt", "r") as file:
    lines = file.read().splitlines()
    grid = [line for line in lines]
    stable = False
    removed_total = 0

    while not stable:
        pass_output = pass_grid(grid, "@")
        new_grid = pass_output["new_grid"]
        removed_total += pass_output["removed_count"]
        if new_grid == grid:
            stable = True
        grid = new_grid

    print(removed_total)