import csv
file = open('stations-filtered.csv', encoding='utf-8')
with open('drainage-area-avg.txt', mode='w') as fileCopy:
    count = 0
    total = 0
    csv_reader = csv.reader(file, delimiter=',')
    #csv_writer = csv.writer(fileCopy, delimiter=',')
    for row in csv_reader:
        if row[7] != "DrainageAreaMeasure/MeasureValue":    
            total+=float(row[7])
            count+=1
    average = total / count
    fileCopy.write(str(average))
file.close()

