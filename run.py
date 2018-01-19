from lib import clean
from lib import data
import xlrd
import os

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
		print x,"cur"
		try:
			cleanObj = clean.Clean(filename, x)
			cleanObj.cleanCsvCells()
			cleanObj.cleanCsvDoc()
		except:
			print "Issue with page ", x
			continue

def xlsxToCsv(filename, index):
	for x in index:
		filenameOut = filename.replace(".xlsx","") + "_clean_sheet" + str(x) + ".csv"
		dataObj = data.Data(filename,x)
		dataObj.encodeAllUnicode()
		dataObj.save(filenameOut)

#takes an already initialized data object, not a filename
def removeColumn(data, header):
	if str(type(data)) != "<type 'instance'>":
		print type(data)," is incorrect parameter"
		return
	data.removeColumn(unicode(header))

if __name__ == '__main__':

	idx = [1,2,3,4,5,6]
	files = [f for f in os.listdir(".")]
	for file in files:
		print file
		if "xlsx" in str(file):
			xlsx(file, idx)
			



	# input2 = "LSS Data for Mosaic 01Jul2017-31Oct2017.xlsx"
	# xlsx(input2,[1])

	# csv(input1)
	# xlsxToCsv(input2,[2])
	# xlsx(input1, [2])


	