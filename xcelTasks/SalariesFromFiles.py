import xlrd

files = []
for i in range(1, 1001):
    files.append('salaries//' + str(i) + '.xlsx')

result_list = []
for file in files:
    wb = xlrd.open_workbook(file)
    sh_title = wb.sheet_names()[0]
    sh = wb.sheet_by_name(sh_title)
    row = sh.row_values(1)
    result_list.append((row[1], row[3]))
print('\n'.join('{} {}'.format(x[0], int(x[1])) for x in sorted(result_list, key=lambda x: x[0])))
