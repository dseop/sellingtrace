from openpyxl import workbook
from openpyxl import load_workbook as lw

wb = workbook()
ws = wb.active
ws1 = wb.create_sheet("Mysheet")
ws.title = "New Title"
filename=input('new filename?\n')
print(type(filename))
wb.save(filename+'.xlsx')
wb.close()