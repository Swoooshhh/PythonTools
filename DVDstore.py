#If you see a few random characters before the Titles it's because your terminal does not support the way i'm inserting colors.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def displayer():
    try:
        dvd_file = open('dvds.txt', 'r')
    except FileNotFoundError:
        print("I cannot find 'dvds.txt', Please use the file given by my Github project.")
    print('\n'*100)
    try:
        with open('dvds.txt') as dvds:
            for line in dvd_file.readlines():
                print('------------------------------------------------------------------------|')
                print(f'|{line}')
                print('------------------------------------------------------------------------|')
    except FileNotFoundError:
        print("I cannot find 'dvds.txt', Please use the file given by the Github project.")
def dvdsearch():
    global movie_description, selection
    movie_check = False
    FirstLoop = True
    dvd_file = open('dvds.txt', 'r')
    dvdselect = input("Name or index of DVD? : ")
    with open('dvds.txt') as dvds:
        dvdcount = 0
        for line in dvd_file.readlines():
            if dvdselect.lower() in line:

                if FirstLoop:
                    print("What would you like to retrieve from your search?")
                    print("1 : Title + Description")
                    print("2 : Title + genre(s)")
                    print("3 : Title + genre(s) + description")
                    selection = input("Selection : ")
                    FirstLoop = False
                else:
                    pass

                movie_description = line.split(",")
                dvdcount += 1
                movie_check = True


                if selection == '1':
                    print(
                        f"{bcolors.OKCYAN} Title: {movie_description[1]}, Description: {movie_description[4]}{bcolors.ENDC}")
                elif selection == '2':
                    print(
                        f"{bcolors.OKCYAN} Title: {movie_description[1]}, Genre(s): {movie_description[2]}, {movie_description[3]} {bcolors.ENDC}")
                elif selection == '3':
                    print(
                        f"{bcolors.OKCYAN} Title: {movie_description[1]}, Genre(s): {movie_description[2]}, {movie_description[3]}, Description: {movie_description[4]}{bcolors.ENDC}")
                else:
                    print(f"{bcolors.FAIL}Not a valid selection.{bcolors.ENDC}")
                    break
            else:
                pass
        if not movie_check:
            print('DVD not found.')
        else:
            pass
            #movie_description = line.split(",")


def another_search():
    again = input('Would you like to search for anything else? Y or N ')
    while True:
        if again.lower() == 'y':
            dvdsearch()
            return False
        elif again.lower() == 'n':
            print('Bye!')
            return False
        else:
            again = input('Would you like to search for anything else? Y or N')
            displayer()
    dvdsearch()
displayer()
dvdsearch()
another_search()