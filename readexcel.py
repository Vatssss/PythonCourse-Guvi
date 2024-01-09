import xlrd

loc = "C:\\Users\\KIIT\\OneDrive\\Desktop\\readexcelpy.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

print(sheet.cell_value(0, 0))
print(sheet.cell_value(1, 3))

print(sheet.nrows)
print(sheet.ncols)

for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))

print(sheet.row_values(1))
