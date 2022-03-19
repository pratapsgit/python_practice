import common as c

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


def execute_me():
    c.print_module_name()
    variables()
    integers()
    strings()
    fstrings()
