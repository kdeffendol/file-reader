import csv
 
#file = open("station.csv", encoding="utf-8") #line 8

file = open('station.csv', encoding='utf-8')
with open('stations-filtered.csv', mode='w') as fileCopy:
    csv_reader = csv.reader(file, delimiter=',')
    csv_writer = csv.writer(fileCopy, delimiter=',')
    for row in csv_reader:
        if row[7] != "":
            csv_writer.writerow(row)
file.close()

