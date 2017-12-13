import csv
import sys
import numpy as np
import random as r
import re
import xlrd


class Data:

    def __init__(self, filename=None, index=None):

        # fields
        self.headers = []
        self.data = []
        self.header2data = {}

        # read in a file if provided
        if (filename != None):
            if ".csv" in filename:
                self.readCsvData(filename)
            if ".xlsx" in filename and index != None:
                self.readXlsxData(filename, index)

    def readXlsxData(self, filename, index):
        workbook = xlrd.open_workbook(filename, on_demand=True)
        sheet = workbook.sheet_by_index(index)
        self.headers = sheet.row_values(0)
        for rowx in range(1, sheet.nrows):
            cols = sheet.row_values(rowx)
            self.data.append(cols)
        workbook.release_resources()
        del workbook

    # reads the csv data from a file
    def readCsvData(self, filename):
        # read the file lines
        fp = file(filename, "rU")
        lines = fp.readlines()
        fp.close()
        # create a csv object
        csvr = csv.reader(lines)
        # set raw_headers to first line
        self.headers = csvr.next()
        for i in range(len(self.headers)):
            self.headers[i] = self.headers[i].strip()
        # loop through the rest of csvr and append each list to raw_data
        for thing in csvr:
            self.data.append(thing)
        # loop through the headers and k,v pair them w/ the corresponding index
        c = 0
        for i in range(len(self.headers)):
            self.header2data[self.headers[i]] = c
            c += 1

    # returns a list of the raw headers
    def get_headers(self):
        return self.headers

    # returns the number of raw columns
    def get_num_columns(self):
        return len(self.headers)

    # returns the number of rows
    def get_num_rows(self):
        return len(self.data)

    # returns a row of raw data with the specified row number
    def get_row(self, rowNum):
        return self.data[rowNum]

    # returns a column of data with the specified header string
    def get_column(self, header):
        # list to column values
        col = []
        # header index
        ind = self.header2data.get(header)
        # adding data to column list
        for row in self.data:
            col.append(row[ind])
        return col

    # returns the raw data at the given header, with the given row number
    def get_value(self, rowNum, header):
        return self.data[rowNum][self.header2data.get(header)]

    # sets the value at the given header, with the given row number
    def set_value(self, rowNum, header, value):
        self.data[rowNum][self.header2data.get(header)] = value

    # adds a column to the data set require a header, a type, and the correct
    # number of points
    def add_column(self, header, plist=None):
        # adding header to list of headers
        self.headers.append(header)
        # initializing counter
        c = 0
        # loop through raw data
        for row in self.data:
            if plist != None:
                # appending data to end of row
                row.append(plist[c])
                c += 1  # incrementing counter
            else:
                row.append("")
        # adding entry to headers2raw dictionary
        self.header2data[header] = len(self.headers) - 1

    # Mapping function on the data field
    def mapData(self, function):
        for x in range(self.get_num_columns()):
            self.headers[x] = function(
                repr(self.headers[x].encode('utf-8')))
        for x in range(self.get_num_rows()):
            for y in range(self.get_num_columns()):
                self.data[x][y] = function(
                    repr(self.data[x][y].encode('utf-8')))

    def save(self, filename=None):
        if filename == None:
            filename = self.file

        with open(filename, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.headers)
            for row in self.data:
                writer.writerow(row)

    def saveCell(self, headers):
        print len(self.data)
        print self.header2data
        filenameIdx = self.header2data.get(headers[0])
        fieldIdx = self.header2data.get(headers[1])
        for x in range(len(self.data)):
            print self.data[x][filenameIdx]
            if fieldIdx == None or filenameIdx == None:
                return
            filename = "txt/" + self.data[x][filenameIdx]
            with open(filename, 'wb') as csvfile:
                csvfile.write(self.data[x][fieldIdx])

    # prints the raw data
    def printData(self):
        print self.headers
        for thing in self.data:
            print thing
