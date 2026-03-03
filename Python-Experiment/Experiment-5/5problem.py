'''Store details of n movies in a dictionary by taking input from the user. Each movie must 
store details like name,  year, director name, production cost, collection made (earning) 
& perform the following :-
a) print all movie details 
b) display name of movies released before 2015 
c) print movies that made a profit. 
d) print movies directed by a particular director. '''
# Create an empty dictionary to store movie details
movies = {}

n = int(input("Enter number of movies: "))

for i in range(n):
    print(f"\nEnter details for movie {i+1}")
    
    name = input("Movie name: ")
    year = int(input("Release year: "))
    director = input("Director name: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection made (earning): "))
    
    # Store movie details in dictionary
    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

# a) Print all movie details
print("\n--- All Movie Details ---")
for name, details in movies.items():
    print(f"\nMovie Name: {name}")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

# b) Display names of movies released before 2015
print("\n--- Movies Released Before 2015 ---")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

# c) Print movies that made a profit
print("\n--- Movies That Made a Profit ---")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)

# d) Print movies directed by a particular director
search_director = input("\nEnter director name to search: ")

print(f"\n--- Movies Directed by {search_director} ---")
for name, details in movies.items():
    if details["director"].lower() == search_director.lower():
        print(name)