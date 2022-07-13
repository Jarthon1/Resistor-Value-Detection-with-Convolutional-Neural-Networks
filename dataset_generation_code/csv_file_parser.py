# collects data from csv file and retrieves ohms tolerance and temperature 
import csv

with open('/Users/golden/Desktop/through_hole_resistors.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # image:
        # label:
        label = (f'\t{row[14]} {row[15]} {row[19]}')
        print(label)
        
    print(f'Processed {line_count} lines.')