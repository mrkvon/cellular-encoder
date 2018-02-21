def nextCell(rule: int, three: int):
    "given a rule and three original cells, count the outcome of the automaton"
    return (rule >> three) % 2

def nextRow(length: int, row: int, rule: int):
    "given a row lenght, representation of its state sa integer and rule"
    "count the next row"
    next = 0
    row = row << 1
    
    for i in range(length):
        next += nextCell(rule, row % 8) * 2 ** i
        row = row >> 1

    return next

def printRow(row: int, length: int):
    "print a cellular automaton row"

    a = '{0:0' + str(length) + 'b}'
    print(a.format(row))

def automaton(rule: int, rows: int):
    "print automaton with rule and amount of rows"

    # amount of cells in each row
    # we make them intentionally wider so the outcome is not influenced by edges
    cells_no = 4 * rows - 3

    # the first row has 1 in the middle
    current_row = 2 ** (2 * rows - 2)

    for i in range(rows):
        trimmed_row = (current_row >> (rows - 1)) % (2 ** (2 * rows - 1))
        printRow(trimmed_row, 2 * rows - 1)
        current_row = nextRow(cells_no, current_row, rule)
