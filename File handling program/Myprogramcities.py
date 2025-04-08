
    # Open the input file with the correct encoding
with open('demofile.txt', 'r') as file:
    cities = file.readlines()
    print (cities)      
    

    # Sort the cities
cities.sort()
print (cities)


    # Write the sorted cities to the output file
with open( 'sorted_cities.txt', 'w', encoding='utf-8') as file:
    file.writelines(cities)
        
    # Strip any whitespace characters (like \n) from the end of each line
cities = [city.strip() for city in cities]
print (cities)




  
 
