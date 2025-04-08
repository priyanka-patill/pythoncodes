import csv
import math

def read_csv(filename):
    points = []
    print(points)
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if there is one
        for row in reader:
            try:
                points.append([float(coord) for coord in row])
                print(f" printing coordinates {points}")
            except ValueError:
                print(f"Skipping row: {row} - Could not convert to float.")
                
    return points

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def find_closest_points(points):
    min_distance = float('inf')
    
    closest_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])
    return closest_pair, min_distance

if __name__ == "__main__":
    filename = 'Coordinate.csv'  
    points = read_csv(filename)
    closest_pair, min_distance = find_closest_points(points)
    print("The closest points are:", closest_pair)
    print("The distance between them is:", min_distance)


