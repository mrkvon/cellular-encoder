import cellular
import search


def automaton(rule: int, rows: int, character: chr):
    "print automaton with rule and amount of rows"

    # set to default view
    current_row = 2 ** (rows - 1)
    for i in range(rows):
        out = search.search(current_row, character)
        if out > -1:
            print(out, i)
            return
        current_row = cellular.nextRow(rows * 2 + 1, current_row, rule)

def encode(rule: int, rows: int, character: chr):
    "print automaton with rule and amount of rows"

    # amount of cells in each row
    # we make them intentionally wider so the outcome is not influenced by edges
    cells_no = 4 * rows - 3

    # the first row has 1 in the middle
    current_row = 2 ** (2 * rows - 2)

    for i in range(rows):
        trimmed_row = (current_row >> (rows - 1)) % (2 ** (2 * rows - 1))
        out = search.search(trimmed_row, character)
        if out > -1:
            print(character, rows - (out - 3), i)
            return
        current_row = cellular.nextRow(cells_no, current_row, rule)
    

def encodeString(rule: int, rows: int, text: str):
    "encode a string with a cellular automaton"

    for i in range(len(text)):
        encode(rule, rows, text[i])

