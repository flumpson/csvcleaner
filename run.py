from lib import clean
from lib import data
import xlrd

def csv(filename):
	cleanObj = clean.Clean(filename)
	cleanObj.cleanCsvCells()
	cleanObj.cleanCsvDoc()

def csvCells(filename,headers):
	cleanObj = clean.Clean(filename)
	cleanObj.writeCellString(headers)

# takes a list of indices representing sheets in the workbook
def xlsx(filename, index):
	for x in index:
		cleanObj = clean.Clean(filename, x)
		cleanObj.cleanCsvCells()
		cleanObj.cleanCsvDoc()

def xlsxToCsv(filename, index):
	for x in index:
		filenameOut = filename.replace(".xlsx","") + "_clean_sheet" + str(x) + ".csv"
		dataObj = data.Data(filename,x)

		dataObj.save(filenameOut)

if __name__ == '__main__':
	input1 = "test.xlsx"
	xlsxToCsv(input1,[0])
	# csv(input2)
	# xlsx(input1, [2])


	