import xlrd

excel = xlrd.open_workbook('../testdata/usermessage.txt')
table = excel.sheets()[0]
