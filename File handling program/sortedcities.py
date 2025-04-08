def sort_cities(input_file, output_file):
     with open(input_file, 'r') as file:  
        cities = file.readlines( )

    # Strip any whitespace characters (like \n) from the end of each line
       cities = [city.strip() for city in cities]

    # Sort the city names alphabetically
    sorted_cities = sorted(cities)
    print(sorted_cities)

    # Write the sorted city names to the output file
    with open(output_file, 'w') as file:
        for city in sorted_cities:
            file.write(city + '\n' )

if __name__ == "__main__":
    
    input_filename = 'cities.txt'  # Replace with your input file name
    output_filename = 'sorted_cities.txt'  # Replace with your output file name
    sort_cities(input_filename, output_filename)
    print(f'Sorted city names have been written to {output_filename}')



