#! python
import openpyxl
wb = openpyxl.Workbook()
print(wb.get_sheet_names())
sheet = wb.get_active_sheet()
print(sheet.title)
sheet.title = 'Span Bacon Eggs Sheet'
print(wb.get_sheet_names())

wb1 = openpyxl.load_workbook('example.xlsx')
sheet = wb1.get_active_sheet()
sheet.title = 'Spam Spam Spam'
wb1.save('example_copy.xlsx')

