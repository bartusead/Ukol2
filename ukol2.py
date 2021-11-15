import csv

with open("data.csv", encoding="utf8") as csvinfile,\
        open("vystup_7dni.csv", "w", encoding="utf8") as csvoutfile:
    reader = csv.reader(csvinfile, delimiter = ",")
    writer = csv.writer(csvoutfile)