import csv
import math
points = []  
with open('Coordinate.csv'  , 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if there is one
        for row in reader:
            points.append([float(cord) for cord in row])                
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)   

min_distance = float('inf')
print(min_distance)   
closest_pair = None
for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])   
print("The closest points are:", closest_pair)
print("The distance between them is:", min_distance)




