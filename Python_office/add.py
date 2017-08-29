#! python3
import openpyxl,os
os.chdir('D:\\untitled')
wb = openpyxl.load_workbook('finally.xlsx')
sheet = wb.get_sheet_by_name('轮胎')
for i in range(2, 32):
    w = sheet['C'+str(i)].value
    sheet['C' + str(i)] = str(w) + '( )'
wb.save('finally.xlsx')


