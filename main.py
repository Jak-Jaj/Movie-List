from random import randint
import time


user_choice = "wrong input"
within_range = False
movie_table = []
watched_movie_table = []


def show_movie_list():
    index_count = 1
    for film in movie_table:
        print( "[" + str(index_count) + "]" + " " + film)
        index_count += 1
    print()


def add_movie_to_list():
    film_choice = input("Jaki film chcesz dodać? ")
    movie_table.append(film_choice)
    print(f"Dodano film: {movie_table[len(movie_table) - 1]} ")
    print()


def picking_action():
    user_choice = input("Co chciałbyś zrobić? ")
    print()

    if user_choice.isdigit() == False:
        print("Wpisz numer!")
        print()

    if user_choice.isdigit() == True:
        if int(user_choice) == 7:
            save_movie_list_to_file()
            time.sleep(0.1)
            quit("Miłego dnia!")
        if int(user_choice) in range(1, 8):
            return int(user_choice)
        else:
            print("Wpisz numer dla jednej z podanych akcji")
            print()


def picking_random_movie():
    randmomized = randint(0, len(movie_table) - 1)
    print(f'Wylosowano: "{movie_table[randmomized]}"')
    print()


def delete_movie_from_list():
    delete_movie = int(input("Wprowadź indeks filmu który chcesz usunąć: "))
    delete_movie -= 1
    print()
    print(f'Usunąłeś: "{movie_table.pop(delete_movie)}" z listy filmów')
    print()


def save_movie_list_to_file():
    file = open("movie.txt", "w+")
    for movie in movie_table:
        file.write(movie + "\n")
    file.close()
    print("Zapisywanie.")
    time.sleep(0.4)
    print("Zapisywanie..")
    time.sleep(0.3)
    print("Zapisiywanie...")
    time.sleep(0.2)
    print("Lista filmów została zapisana!")
    print()


def load_movies_from_file():

    try:
        file = open("movie.txt", "r")
        print("Znaleziono już istniejącą liste filmów")
    except FileNotFoundError:
        file = open("movie.txt", "w+")
        print("Utworzono nową listę")

    print()
    for line in file.readlines():
        movie_table.append(line.strip())
        file.close()


def add_to_watched_movies_file():
    file = open('watched.txt', 'a')

    print("Podaj indeks filmu którego chcesz dodać\ndo listy obejrzanych filmów:")
    watched_index = input()
    indexing = True
    while indexing:
        if watched_index.isdigit():

            watched_indexing = int(watched_index) - 1
            if watched_indexing in range(len(movie_table)):
                watched_movie_table.append(movie_table[watched_indexing])
                print(f"Dodano {movie_table[watched_indexing]} do listy obejrzanych filmów")
                file.write(movie_table[watched_indexing])
                file.write('\n')

                rating_movie(watched_indexing)
                file.write('\n')
                break
            else:
                print('Podano zły indeks')
                print()

                break
        else:
            print("Indeks który podajesz nie istnieje.")
    file.close()


def rating_movie(watched_index):
    file = open('watched.txt', 'a')
    rating = True
    print("Czy chcesz dodać ocenę? T/N")
    want_to_rate = input().lower()

    while rating:
        if want_to_rate == 'n':
            file.write('Brak oceny')
            file.write('\n')
            rating = False

        elif want_to_rate == 't':
            print(f"Jaką ocene chcesz żeby otrzymał film: {movie_table[watched_index]}?")
            print("Skala 0-10")
            rated = input()

            if rated.isdigit():
                file.write(f'Ocena: {rated}/10')
                file.write('\n')
                print("Dodano ocenę!")
                break
            else:
                print("Spróbuj ponownie")
            rating = False

        elif want_to_rate not in ['t', 'n']:
            print("Wpisz T lub N")
            break
    file.close()


load_movies_from_file()

while user_choice not in range(1, 8) or within_range == False:

    print("1. Wyświetl listę filmów.")
    print("2. Dodaj film do listy.")
    print("3. Wylosuj film.")
    print("4. Dodaj do listy obejrzanych filmów.")
    print('5. Pokaż liste obejrzanych filmów. WORK IN PROGRESS')
    print("6. Usuń film z listy.")
    print("7. Zapisz i wyjdź.")
    print()

    user_choice = picking_action()

    if user_choice == 1:
        show_movie_list()
    elif user_choice == 2:
        add_movie_to_list()
    elif user_choice == 3:
        picking_random_movie()
    elif user_choice == 4:
        add_to_watched_movies_file()
    elif user_choice == 5:
        pass

    #DODAJ WYPISANIE LISTY OBEJRZANYCH FILMÓW

    elif user_choice == 6:
        delete_movie_from_list()