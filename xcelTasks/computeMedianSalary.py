import xlrd

wb = xlrd.open_workbook('salaries.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
max_med = 0
max_med_territory = ''
max_avg = 0
max_avg_job = ''
for i in range(1, 9):
    row = sh.row_values(i)
    row_values = row[1:]
    med = sorted(row_values)[len(row_values) // 2]
    if med > max_med:
        max_med = med
        max_med_territory = row[0]

for i in range(1, 8):
    column = sh.col_values(i)
    col_values = column[1:]
    avg = sum(col_values) / len(col_values)
    if avg > max_avg:
        max_avg = avg
        max_avg_job = column[0]
print(max_med_territory, max_avg_job)
