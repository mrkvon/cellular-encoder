import cellular

current_row = 2 ** 24
for i in range(25):
    cellular.printRow(current_row, 49)
    current_row = cellular.nextRow(49, current_row, 30)
