import xlrd

wb = xlrd.open_workbook('trekking3.xlsx')
sh_product = wb.sheet_by_name('Справочник')
sh_schedule = wb.sheet_by_name('Раскладка')
col_product = sh_product.col_values(0)
products_dict = {}
products_per_day_list = []
col_schedule = sh_schedule.col_values(0)
products_per_day = {}
schedule_per_days = {}
for i in range(1, len(col_product)):
    products_dict[sh_product.row_values(i)[0]] = list(map(lambda x: float(x or 0), sh_product.row_values(i)[1:]))
# print(products_dict)
for i in range(1, len(col_schedule)):
    day_num = sh_schedule.row_values(i)[0]
    product_title = sh_schedule.row_values(i)[1]
    amount = sh_schedule.row_values(i)[2]
    if schedule_per_days.keys().__contains__(day_num):
        if not schedule_per_days[day_num].keys().__contains__(product_title):
            schedule_per_days[day_num][product_title] = amount
        else:
            schedule_per_days[day_num][product_title] += amount
    else:
        schedule_per_days[day_num] = {}
        schedule_per_days[day_num][product_title] = amount
print('\n'.join('{}: {}'.format(k, v) for k, v in schedule_per_days.items()))
final_list = [[0.]*4 for i in range(len(schedule_per_days.keys()))]
for day in schedule_per_days.keys():
    for product in schedule_per_days[day].keys():
        for i in range(4):
            final_list[int(day) - 1][i] += float(schedule_per_days[day][product]) * products_dict[product][i] / 100
for i in range(len(final_list)):
    print(*map(int, final_list[i]))
