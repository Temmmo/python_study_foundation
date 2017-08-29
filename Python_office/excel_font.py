import openpyxl
from openpyxl.styles import Font, Style
wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')

italic24Font = Font(size=24, italic=True)
styleObj = Style(font=italic24Font)
sheet['A1'].style = styleObj
sheet['A1'] = 'Hello world!'

fontObj1 = Font(name='Times New Roman', bold=True)
styleObj1= Style(font=fontObj1)
sheet['A7'].style = styleObj1
sheet['A7'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
styleObj2 = Style(font=fontObj2)
sheet['B3'].style = styleObj2
sheet['B3'] = '24 pt Italic'
wb.save('styled.xlsx')

wb2 = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb2.get_active_sheet()
sheet.freeze_panes = 'A2'
wb2.save('freezeExample.xlsx')

