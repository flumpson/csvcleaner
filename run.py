from lib import clean
from lib import data
import xlrd
import os

def csv(filename, regex=None):
	cleanObj = clean.Clean(filename)
	cleanObj.cleanCsvCells()
	if regex is not None:
		cleanObj.cleanCsvDoc(regex)

def csvCells(filename,headers):
	cleanObj = clean.Clean(filename)
	cleanObj.writeCellString(headers)

# takes a list of indices representing sheets in the workbook
def xlsx(filename, index, regex=None):
	for x in index:
		print "beginning sheet", x
		try:
			cleanObj = clean.Clean(filename, x)
			cleanObj.cleanCsvCells()
			if regex is not None:
				cleanObj.cleanCsvDoc(regex)
		except StopIteration:
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

	idx = [3]
	subdirectory = "input"
        try:
            os.mkdir(subdirectory)
        except Exception:
            pass
	files = [f for f in os.listdir("./input")]
	for file in files:
		if ".xlsx" in str(file):
			print "Beginning clean of ",file
			xlsx(file, idx)
		if ".csv" in str(file):
			print "Beginning clean of ",file
			csv(file)

	