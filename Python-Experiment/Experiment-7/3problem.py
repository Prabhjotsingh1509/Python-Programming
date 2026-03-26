'''Assume a file city.txt with details of 5 cities in given format (cityname population(in 
lakhs) area(in sq KM) ): 
Example: 
Dehradun 5.78 308.20 
Delhi 190 1484 
…………… 
Open file city.txt and read to: 
a. Display details of all cities 
b. Display city names with population more than 10Lakhs 
c. Display sum of areas of all cities'''
file = open("city.txt", "r")

total_area = 0

print("Details of all cities:\n")

for line in file:
    city, population, area = line.split()
    
    population = float(population)
    area = float(area)
    print(city, population, area)

    if population > 10:
        print("City with population >10 lakhs:", city)
    total_area += area

file.close()

print("\nTotal area of all cities:", total_area)