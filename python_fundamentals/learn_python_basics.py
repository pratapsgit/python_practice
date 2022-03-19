import common as c
import random

print("Hello start here exploring python")


def variables():
    # Variables
    print("variables")
    wallet = 34

    print("wallet = " + str(wallet))

# Integers


def integers():
    age = 42
    weight = 72.3

    print("age " + str(age))
    print("weight " + str(weight))

# String


def strings():
    name = "Harry James"
    print("name " + name)

    movie = "Spider Man."
    print("movie " + movie)

# fstring


def fstrings():
    day = 16
    month = 3
    year = 2022
    temp = 32

    print(
        f"On {day}/{month}/{year} temperature recorded is {temp} degree celcius in Bangalore.")

# booleans


def booleans():
    door_is_close_or_open = False

    if door_is_close_or_open:
        print("Door is open")
    else:
        print("Door is closed")

# comparisions


def comparisions():
    the_matrix_rows = 4
    the_matrix_cols = 5

    if the_matrix_rows == the_matrix_cols:
        print("matrix is a SQUARE MATRIX")
    elif the_matrix_rows > the_matrix_cols:
        print("matrix is a ROW OWNED MATRIX")
    elif the_matrix_cols > the_matrix_rows:
        print("matrix is a COLUMN OWNED MATRIX")

# random exercise


def random_exp():
    ans_list = ["Yes", "No", "May be"]
    answer = random.randint(1, 2)

    print(ans_list[answer])

# fortune cookie problem


def fortune_cookie():
    lucky_number = random.randint(1, 100)

    day_fortuner = random.randint(1, 2)

    if day_fortuner == 1:
        fortune_text = "You will have a great day"
    elif day_fortuner == 2:
        fortune_text = "There is another good day comming soon"
    else:
        fortune_text = "Better luck next time"

    print(f"{fortune_text}. Todays lucky number is {lucky_number}")

# concept of list


def list_idea():
    fav_movies = ["The Dark Knight", "Spiderman", "The Banker"]

    print(fav_movies)

    print("first element in the list \'"+fav_movies[0]+"\'")

    print("Length of the list ", len(fav_movies))

    fav_movies.append("Shooter")

    print(fav_movies)

    print("New length of the list ", len(fav_movies))

    fav_movies.insert(2, "The jurrasic park")

    print(fav_movies)

    print("New length of the list ", len(fav_movies))

    del(fav_movies[2])

    print(fav_movies)

    print("New length of the list ", len(fav_movies))

# loops


def looping():
    title = ['Mr.', 'Mrs.']

    for num in range(10):
        t = random.randint(0, 1)
        print(f"Hello!!!. How are you? {title[t]} {num}")


# dictionaries

def dictionaries():
    animals = {"cat": 10, "dog": 12, "turtle": 70}

    print(animals)

    animals["mouse"] = 7

    print(animals)

    print(f"Total number of pet animals we have {len(animals)}")

    del(animals["mouse"])

    print(animals)

    print(f"Total number of pet animals we have {len(animals)}")

# counting words


def counting_words():
    the_text = """
    
Less acknowledged is that Bhutan is the only country on the planet that is carbon negative. Despite being one of the smallest countries in the world it has one of the largest commitments to conservation, mandating that a minimum of 60 per cent of land must remain under forest cover forever. In travelling here my intention is to understand the meaning of happiness in a society where Buddhism is deeply rooted, but where the temptations (and collateral damage) of a more affluent, fast-paced way of life are also rising. Deep down, and like any other person, I am also curious about what makes for happiness in itself.

The first thing I notice as I disembark is the sweet scent of pine and the occasional musky smell of incense in the air. Prayer flags litter the landscape on every turn and dance in the wind - some mark the dead and others celebrate life. During my ten days here I spend time in the bustling capital city of Thimphu, where development and urbanisation are rampant, before travelling east through Punakha into the flat, earth-coloured Phobjikha Valley, which resembles the landscapes of Mongolia. I'm left speechless by the grand dzongs (fortresses) on the mountaintops - impossibly detailed wall paintings and sculptures depicting half-human, half-animal spirits hang from the walls inside. I encounter the Paro Tsechu Festival, a colourful four-day celebration held in the dzong in Paro that culminates in a throng of masked dancers in yellow robes moving hedonistically to the beat of a drum and the reverberating drone of a dunchen (horn).

    """

    print(the_text)

    print(f"Number of characters present in the text {len(the_text)}")

    print(f"Number of words present in the text {len(the_text.split())}")

    word_dict = {}
    for w in the_text.lower().split():
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1

    for w in word_dict:
        print(w, word_dict[w])

# inputs


def input_use():
    name = input("Enter your name : ")
    print(f"Hello {name}")


# guess the number
def guess_the_number():
    print("Number to be gussed between 1 - 100")
    the_input = int(input("Please guess the number "))
    expected_answer = random.randint(1, 100)
    guesses = 0

    while the_input != expected_answer:
        guesses += 1
        if the_input < expected_answer:
            the_input = int(input("guess higher..Please guess the number "))
        else:
            the_input = int(input("guess lower..Please guess the number "))

    print(f"Yahooo...guess is correct..({guesses})")


def execute_me():
    c.print_module_name()
    # variables()
    # integers()
    # strings()
    # fstrings()
    # booleans()
    # comparisions()
    # random_exp()
    # fortune_cookie()
    # list_idea()
    # looping()
    # dictionaries()
    # counting_words()
    guess_the_number()
