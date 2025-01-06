import openpyxl

file = '/Users/gauravmaan/Downloads/demo.xlsx'
workbook = openpyxl.load_workbook(file)

sheet = workbook.active

# Iterate over all rows and columns
for r in range(1, 6):
    for c in range(1, 4):
        cell = sheet.cell(r, c)

        # Check if the current cell is part of a merged range
        if cell.coordinate in sheet.merged_cells:
            continue  # Skip the merged cells

        # Assign value to the cell
        cell.value = "❤"

workbook.save(file)