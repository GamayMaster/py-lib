# -------------------------------------- #
# create table from data set (csv file)  #
# with python                            #
# and write table in html file           #
# -------------------------------------- #

from sys import argv
from dataSet import *
import csv


if len(argv) == 1:
    exit()

cols, rows = getColRows(ReadCSV(argv[1]))
header = ReadFile('header.html')
footer = ReadFile('footer.html')

head = '<table>\n<tr><th>No</th>'
for c in cols:
    head += '<th>' + c + '</th>'
head += '</tr>'

i = 1
body = str()

for r in rows:
    row = str()
    row += '<tr><td>' + str(i) + '</td>'
    for n in range(0, len(r)):
        if r[n] == '':
            continue
        else:
            row += '<td>' + str(r[n]) + '</td>'
    row += '</tr>\n'
    body += row
    i += 1
    del row

body += '\n</table>'
with open(argv[1] + '.html', 'w') as fw:
    fw.write(header)
    fw.write(head)
    fw.write('\n')
    fw.write(body)
    fw.write(footer)
    fw.close()
