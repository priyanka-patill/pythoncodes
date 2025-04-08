
import csv

# Replace 'your_file.csv' with the path to your CSV file
#with open('Coordinate.csv', mode='r') as file:
file=open ('Coordinate.csv', mode='r')
x= csv.reader(file)
#header = next(x)
#print(f"Header: {header}")
    
for row in x:
        print(row)
       


# Replace 'your_file.csv' with the path to your CSV file
with open('abk.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Writing the header
    header = ['Column1', 'Column2', 'Column3']
    csv_writer.writerow(header)
    
    # Writing the data
    data = [
        [1, 'A', 3.14],
        [2, 'B', 2.71],
        [3, 'C', 1.62]
    ]
    
    csv_writer.writerows(data)
