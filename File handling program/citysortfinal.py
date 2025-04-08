def sort_cities(input_filename, output_filename):
    # Open the input file with the correct encoding
    with open(input_filename, 'r') as file:
        cities = file.readlines()
        print (cities)

    

    # Sort the cities
    cities.sort()
    print (cities)

  
 # Sort the city names alphabetically
    #sorted_cities = sorted(cities)
    #print(sorted_cities)
    # Write the sorted cities to the output file
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.writelines(cities)
    # Strip any whitespace characters (like \n) from the end of each line
    cities = [city.strip() for city in cities]
    print (cities)

# Define the input and output filenames
input_filename = 'demofile.txt'
output_filename = 'sorted_cities.txt'

# Call the function to sort the cities
sort_cities(input_filename, output_filename)
