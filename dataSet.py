import csv


def ReadFile(fname):
    with open(fname, 'r') as sf:
        data = sf.read()
        sf.close()
    return data


def ReadCSV(fname):
    with open(fname, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        file.close()

    return data


def getColRows(data):
    cols = data[0]  # columns...
    del data[0]     # remove this row it is content on column name
    # return data
    return cols, data


def getIndex(cols, col):
    for i in range(0, len(cols)):
        if cols[i] == col:
            return i


def mat2dict(data):
    # columns...
    cols    = data[0]
    # len of columns...
    col_len = len(cols)
    # remove this row it is content on column name
    del data[0]
    # rows...
    rows = data
    # len or rows...
    row_len = len(rows)

    # create dictionary name
    ls = []
    dist = {}

    # inject data in dictionary
    for i in range(0, col_len):         # loop to columns
        for j in range(0, row_len):     # loop to rows
            ls.append(rows[j][i])
        dist[cols[i]] = ls
        ls.clear()

    # return data
    return cols, dist
