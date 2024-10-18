# Generera slumpmässiga operationer
import random
# Extraherar data från HTML-och XML dokument
from bs4 import BeautifulSoup
# HTTP-förfrågningar - förenklar processen att skicka/ta emot data från webben
import requests
import json

# Definiera filens sökväg
json_file_path = 'movies.json'

# Försök att ladda JSON-data från filen, eller hämta filmer om filen inte finns
try:
    with open(json_file_path, 'r') as json_file:
        movies_dict = json.load(json_file)
except FileNotFoundError:
    # Om filen inte finns, hämta data från webben
    response = requests.get("https://www.timeout.com/film/the-50-best-christmas-movies")
    to_web_page = response.text

    # Analysera HTML koden
    soup = BeautifulSoup(to_web_page, "html.parser")
    movies_item = soup.find_all("h3", class_="_h3_cuogz_1")

    # Skapa en lista för film datan
    movies_list = []
    for movie in movies_item:
        movie_title = movie.getText().split()  # Dela upp titeln i ord
        if len(movie_title) > 1:  # Kolla om det finns mer än ett ord
            movie_title = ' '.join(movie_title[1:])  # Förena titeln igen utan första ordet
        movies_list.append({"title": movie_title})

    # Skapa en dictionary för att spara filmerna
    movies_dict = {"movies": movies_list}
    # Spara dictionary i en JSON fil
    with open(json_file_path, 'w') as json_file:
        json.dump(movies_dict, json_file, indent=4)

print("Hello! This is the 50 best Christmas Movies.")

def show_movie_list():
    """Skriver ut filmerna i en lista med index och titel"""
    for i, movie in enumerate(movies_dict['movies']):# Loopa igenom dictionary för att få tag på index och objekt
        title = movie['title']  # Hämta titlen
        print(f"{i + 1}. {title}")  # Skriv ut index och titel

show_movie_list()

game_should_continue = True
while game_should_continue:
    print("\n" * 3)
    print("Do you wanna delete a movie that you have already seen? "
          "Or get a random movie choice? ")
    r_or_d = input("Type 'd' for delete or 'r' for random movie:  ")

    if r_or_d == "d":
        while True:  # Loop till giltig input är mottagen
            delete_movie = input("Which movie do you wanna delete? Type the number or 'exit' to go back: ")

            if delete_movie.lower() == "exit":
                print("Returning to main menu.")
                break  # Exit den nestade loopen

            try:
                # Konvertera input till 0-index
                index_to_delete = int(delete_movie) - 1
                # Kontrollerar om det angivna index ligger inom den gilitga intervallen
                if 0 <= index_to_delete < len(movies_dict['movies']):
                    # Ta bort film från listan
                    removed_movie = movies_dict['movies'].pop(index_to_delete)

                    print("\n" * 20)
                    # Visa vilken film som togs bort
                    print(f"You removed: {removed_movie['title']}")
                    print("Updated list:")
                    # Skriv ut den uppdaterade listan
                    show_movie_list()

                    # Spara den uppdaterade listan i JSON-filen
                    with open(json_file_path, 'w') as json_file:
                        json.dump(movies_dict, json_file, indent=4)
                    # Gå ur nestade loopen efter lyckad radering
                    break
                else:
                    print("Invalid number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    elif r_or_d == "r":
        # Använda random för att slumpa en film i dictionary
        if movies_dict['movies']:
            random_movie = random.choice(movies_dict['movies'])
            title_random = random_movie['title']  # Hämta titlen
            print(f"You should watch: {title_random}")
        else:
            print("No movies available to choose from.")

    else:
        game_should_continue = False
        print("Exiting the program. Goodbye!")