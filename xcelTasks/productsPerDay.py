import xlrd

wb = xlrd.open_workbook('trekking2.xlsx')
sh_per_day = wb.sheet_by_name('Раскладка')
cols_per_day = sh_per_day.col_values(0)
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
cols = sh.col_values(0)
per_day_dict = {}
prod_dict = {}
for i in range(1, len(cols_per_day)):
    per_day_dict[sh_per_day.row_values(i)[0]] = sh_per_day.row_values(i)[1]
print(per_day_dict, sep=' ')
for i in range(1, len(cols)):
    prod_dict[sh.row_values(i)[0]] = sh.row_values(i)[1:]
print(prod_dict)
final_list = [0., 0., 0., 0.]
for product in per_day_dict.keys():
    for i in range(4):
        if prod_dict[product][i] == '':
            prod_dict[product][i] = 0
            print(product, prod_dict[product])
        final_list[i] += float(per_day_dict[product]) * float(prod_dict[product][i]) / 100
print(final_list)
print(*map(int, final_list))
