import csv

def read_file(path):
    movies = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            movies = list(reader)
        
        # Convert fields as needed
        for movie in movies:
            movie["Year"] = int(movie["Year"])
            movie["Rating"] = float(movie["Rating"])
        return movies
    
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def display_menu():
    print("\n========== Movie Analyzer Menu ==========")
    print("1. Display summary statistics")
    print("2. Display movies sorted by rating (descending)")
    print("3. Display movies sorted by year (ascending)")
    print("4. Exit program")

def display_stats(movies):
    if not movies:
        print("No movie data available.")
        return
    
    ratings = [m["Rating"] for m in movies]
    avg_rating = sum(ratings) / len(ratings)
    max_rating = max(ratings)
    highest_rated = [m for m in movies if m["Rating"] == max_rating]
    min_rating = min(ratings)
    lowest_rated = [m for m in movies if m["Rating"] == min_rating]
    
    print("\n----- Summary Statistics -----")
    print(f"Number of movies: {len(movies)}")
    print(f"Average rating: {avg_rating:.2f}")
    print(f"\nHighest rated movie(s) (Rating: {max_rating:.1f}):")
    for movie in highest_rated:
        print(f'  "{movie["Title"]}" ({movie["Year"]})')
    print(f"\nLowest rated movie(s) (Rating: {min_rating:.1f}):")
    for movie in lowest_rated:
        print(f'  "{movie["Title"]}" ({movie["Year"]})')
        
def rating_sort(movies):
    if not movies:
        print("No movie data available.")
        return
    
    sorted_movies = sorted(movies, key=lambda x: x["Rating"], reverse=True)
    print("\n----- Movies Sorted by Rating (In descending order) -----")
    for m in sorted_movies:
        print(f"{m['Rating']:.1f} - {m['Title']} ({m['Year']})")

def year_sort(movies):
    if not movies:
        print("No movie data available.")
        return
    
    sorted_movies = sorted(movies, key=lambda x: x["Year"])
    print("\n----- Movies Sorted by Year (In ascending order) -----")
    for m in sorted_movies:
        print(f"{m['Year']} - {m['Title']} (Rating: {m['Rating']:.1f})")

def main():
    print("Welcome to the Movie Analyzer!")
    path = input("Enter the path for the movie CSV data file: ").strip()
    movies = read_file(path)
    
    if movies is None:
        print("No data was read. Exiting program.")
        return
    
    while True:
        display_menu()
        option = input("Choose an option (1-4): ").strip()
        
        if option == "1":
            display_stats(movies)
        elif option == "2":
            rating_sort(movies)
        elif option == "3":
            year_sort(movies)
        elif option == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
