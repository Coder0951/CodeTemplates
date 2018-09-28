import glob
import csv
import codecs

rowcounter = 0
# import csv files from folder
path = r'\\ent.core.company.com\mit-city01\City Public\NPS\RecievedProponisi'
allFiles = glob.glob(path + "/CSAT_*.csv")
with open(r'\\ent.core.company.com\mit-city01\City Public\NPS\combined.csv', 'wt') as outfile:
    writer = csv.writer(outfile)
    for i, fname in enumerate(allFiles):
        indirowcount = 0
        csv_f = csv.reader(x.replace('\0', '') for x in codecs.open(fname, 'rU', 'utf-16'))
        print(fname.replace(
            r'\\ent.core.company.com\mit-city01\City Public\NPS\RecievedProponisi', ''), 'file:' + str(i))
        if i != 0:
            for x, row in enumerate(csv_f):
                if x > 1:
                    writer.writerow(row)
                    rowcounter = rowcounter + 1
                    indirowcount = indirowcount + 1
                elif x == 0:
                    print('Skipped Header Row')
                elif x == 1:
                    print('Skipped First Row')
        else:
            for x, row in enumerate(csv_f):
                if x != 1:
                    writer.writerow(row)
                    indirowcount = indirowcount + 1
                    rowcounter = rowcounter + 1
                elif x == 1:
                    print('Skipped First Row')
        print('rows ' + str(indirowcount) + ' of ' + str(x+1), 'Total Rows ' + str(rowcounter))
