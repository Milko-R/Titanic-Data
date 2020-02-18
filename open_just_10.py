import csv
with open('titanic_csv.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for i,row in enumerate(reader):
        print(row['survived'], row['pclass'], row['name'], row['sex'], row['age'])
        if(i >= 9):
            break
