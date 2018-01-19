
import data as d
import re
import csv


class Clean:

    def __init__(self, filenameIn, index=None):
        self.regex = re.compile(r'[^a-zA-Z0-9\.\s]+')
        if index != None:
            self.dataObj = d.Data(filenameIn,index) 
        else:
            self.dataObj = d.Data(filenameIn)
        # self.preMapObj = d.Data(filenameIn)
        if '.csv' in filenameIn:
            arr = filenameIn.split(".")
            self.filenameOut = arr[0] + "_clean.csv"
        else:
            self.filenameOut = filenameIn.replace(".xlsx","") + "_clean_sheet" + str(index) + ".csv" 

    #cleans the interior of each cell
    def cleanCsvCells(self):
        self.dataObj.mapData(self.cleanValue)
        self.dataObj.save(self.filenameOut)

    def writeCellString(self,headers):
        self.dataObj.saveCell(headers)

    def fileChanged(self):
        preHash = str(hash(tuple(map(tuple, self.preMapObj.data))))
        postHash = str(hash(tuple(map(tuple, self.dataObj.data))))
        print preHash + " --> " + postHash
        return postHash != preHash

    def cleanValue(self, val):
        return re.sub(self.regex, '', val)

    #gets rid of blank lines and dangling return and newline characters in the document itself.
    def cleanCsvDoc(self):
        regexCleaned = open(self.filenameOut).read()
        regexCleaned = re.sub(r'(,,,)[,]*[\r]*[\n]*', "", regexCleaned)
        with open(self.filenameOut, 'w') as file:
            file.write(regexCleaned)


if __name__ == '__main__':
    pass

