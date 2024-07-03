import csv

with open('C:/Users/Hunter/Downloads/airline_codes.csv') as file:
    csv_reader = csv.reader(file)
    rows = [row for row in csv_reader]
    file2 = open('C:/Users/Hunter/Downloads/airline_codes2.csv', 'w+', newline="")
    csv_writer=csv.writer(file2)
    rowsNoHeader = rows[1:]
    for row in rowsNoHeader:
        csv_writer.writerow(row)
    file2.close()

        


