import xlrd

wb = xlrd.open_workbook('trekking1.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
cols = sh.col_values(0)
prod_cal_list = []
for i in range(1, len(cols)):
    prod_cal_list.append(tuple(sh.row_values(i)[:2]))
prod_cal_list.sort(key=lambda x: (-int(x[1]), x[0]))
for i in range(len(prod_cal_list)):
    print(prod_cal_list[i][0])
