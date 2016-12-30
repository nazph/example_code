import openpyxl


book = openpyxl.load_workbook('importxl.xlsx')
sheet_name = book.get_sheet_names()
sheet=book.get_sheet_by_name(sheet_name[0])


excel_product=[]
list_product=[]

temp_product=[]
excel_qtys = []
for row in range(2, sheet.max_row + 1):
	product={}
	name_product = sheet['A' + str(row)].value   
	if not name_product:
		continue
	else:
		excel_product.append(name_product)  
		temp_product.append(name_product)

	qty = sheet['C' + str(row)].value or 0
	product[name_product]=qty
	list_product.append(product)


sorted(list_product)

qtys = [i.values()[0] for i in list_product]

for i in qtys:
	print i
	print type(i)




for i in list_product:
	print i
	print type(i)









