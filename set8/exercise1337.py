# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the setly exercises, fill in the functions,
and test them to see if they work.
You have 2 hours.
"""
import json
import os
import random
import string
import time
from typing import Any
import requests


def give_me_five() -> int:
    the_answer = 5
    """Returns the integer five."""
    return the_answer


def password_please() -> str:
    the_answer = f"Passwordforkaren"
    """Returns a string, 8 or more characters long, contains at
    least one upper case letter and one lowercase letter.
    TIP: don't put in a real password!"""
    return the_answer


def list_please() -> list[Any]:
    """Returns a list, you can put anything in the list."""
    my_list = []
    for i in range(10):
        my_list.append(i)
    return my_list

def int_list_please() -> list[int]:
    my_list = []
    for i in range(10):
        my_list.append(int(10))
    """Returns a list of integers, any integers are fine."""
    return my_list


def string_list_please() -> list[str]:
    my_list = []
    for i in range(5):
        my_list.append(str("mama"))
    """Returns a list of strings, any string are fine."""
    return my_list


def dictionary_please() -> dict:
    momsheight = 150
    dadsheight = 170
    the_answer = {"mom": momsheight, "dad": dadsheight}
    """Returns a dictionary, anything you like."""
    return the_answer


def is_it_5(some_number) -> bool:
    if some_number == 5:
        well_is_it = True
    else:
        well_is_it = False
    """Returns True if the argument passed is 5, otherwise returns False."""
    return well_is_it


def take_five(some_number) -> int:
    value = int(some_number)
    the_answer = value - 5
    """Subtracts 5 from some_number."""
    return the_answer


def greet(name="Towering Timmy") -> str:
    the_answer = f"Well hello, {name}"
    """Return a greeting.
    return a string of "Well hello, " and the name argument.
    E.g. if given as "Towering Timmy" it should
         return "Well hello, Towering Timmy"
    """
    return the_answer


def one_counter(input_list=[1, 4, 1, 5, 1, 1]) -> int:
    count = 0
    for item in input_list:
        if item == 1:
            count = count + 1
    """Count the number of 1s in the input_list.
    Return an integer.
    TIP: the test will use a different input_list, so don't just return 2
    """
    return count


def n_counter(search_for_this, input_list=[1, 4, 1, 5, 1, 1]) -> int:
    """Count the number of times search_for_this shows up in the input_list.
    Return an integer.
    """
    count = 0
    for item in input_list:
        if item == int(search_for_this):
            count = count + 1

    return count


def fizz_buzz() -> list:
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!

       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."

    from https://blog.codinghorror.com/why-cant-programmers-program/

    Return a list that has an integer if the number isn't special,
    and a string if it is. E.g.
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
         'Fizz', 'Buzz',  11, 'Fizz', 13, 14,
         'FizzBuzz', 16, 17, ...]
    """
    fizz_buzz_list = []
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz_list.append(f"FizzBuzz")
        elif i % 3 == 0:
            fizz_buzz_list.append(f"Fizz")
        elif i % 5 == 0:
            fizz_buzz_list.append(f"Buzz")
        else:
            fizz_buzz_list.append(i)
    # your code here

    return fizz_buzz_list


def set_it_on_fire(input_string="very naughty boy") -> str:
    """Interleave the input_string with the 🔥 emoji.

    Given any string, interleave it with 🔥. Also make it be upper case.
    e.g. "very naughty boy" should return the string
    "🔥V🔥E🔥R🔥Y🔥 🔥N🔥A🔥U🔥G🔥H🔥T🔥Y🔥 🔥B🔥O🔥Y🔥"
    TIP: strings are pretty much lists of chars.
         If you list("string") you get ['s', 't', 'r', 'i', 'n', 'g']
    TIP: consider using the 'join' method in Python.
    TIP: make sure that you have a 🔥 on both ends of the string.
    """
    upper_string = input_string.upper()
    the_answer = "🔥" + '🔥'.join(upper_string) + "🔥"

    return the_answer


def the_chain_gang_5(the_value) -> bool:
    """Take the_value, subtract 5 from it, and return True if the value we end up with it 5.

    You don't get anything for free this far into the quiz, you can't
    use the == operator or the - operator, and you must use two of the
    functions you've already written.

    TIP: you've already written a function that returns True if the value is 5
    TIP: you've already written a function that subtracts 5
    """

    return is_it_5(take_five(the_value))


def pet_filter(letter="a") -> list:
    """Return a list of pets whose name contains the character 'letter'"""
    # fmt: off
    pets = [
        "dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken", 
        "guinea pig", "donkey", "duck", "water buffalo", "python", "scorpion",
        "western honey bee", "dromedary camel", "horse", "silkmoth", 
        "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca", 
        "guineafowl", "ferret", "muscovy duck", "barbary dove", "cichlid",
        "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi", 
        "canary", "society finch", "fancy mouse", "siamese fighting fish", 
        "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"
    ]
    # fmt: on
    filtered = []
    for item in pets:
        if letter in item:
            filtered.append(item)

    return filtered


def best_letter_for_pets() -> str:
    """Return the letter that is present at least once in the most pet names.

    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    TIP: use the function you just wrote to help you here!
    TIP: you've seen this before in the pokedex.
    """
    import string

    the_alphabet = string.ascii_lowercase
    most_popular_letter = None

    alphabet_list = list(the_alphabet)
    longest_count = 0

    for letter in alphabet_list:
        current_list = pet_filter(letter)
        if len(current_list) > longest_count:
            longest_count = len(current_list)
            most_popular_letter = letter
    
    return most_popular_letter


def make_filler_text_dictionary() -> dict:
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4
    If we set wordlength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"

    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    {
        3: ['Seb', 'the', 'yob', "boy"],
        4: ['aaaa', 'bbbb', 'cccc', "ddd"],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc', 'ddddddd']
    }
    Use the API to get the 4 words.

    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 4 words for each)
    TIP: you'll need the requests library
    """
    wd = {}
    length = 3
    while length < 8:
        no_of_words = 0
        url = f"https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}"
        list_of_words = []
        while no_of_words < 4:
            r = requests.get(url).text
            for i in range(1):
                list_of_words.append(r)
            no_of_words = no_of_words + 1
        new_dict={f"{length}":list_of_words}
        wd={**wd,**new_dict}
        length = length + 1
    return wd


def random_filler_text(number_of_words=200) -> str:
    """Make a paragraph of random filler text.
    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library,
        e.g. random.randint(low, high)
    """ 

    my_dict = make_filler_text_dictionary()
    words = []

    for _ in range(number_of_words):
        length = str(random.randint(3, 7))
        word = random.randint(0,3)
        words.append(my_dict[length][word])
    return " ".join(words)


def fast_filler(number_of_words=200) -> str:
    """Makes filler text, but really fast.

    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run, if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_cache.json"
    TIP: you'll need the os and json libraries
    TIP: This is making sentences. Make the first letter capital, and add a full stop to the end.
    TIP: you'll probably want to use json dumps and loads to get the
    dictionary into and out of the file. Be careful when you read it back in,
    it'll convert integer keys to strings.
    If you get this one to work, you are a Very Good Programmer™!
    """

    fname = "dict_cache.json"

    return None


if __name__ == "__main__":
    print("give_me_five", give_me_five(), type(give_me_five()))
    print(
        "strong_password_please",
        password_please(),
        type(password_please()) == str,
    )
    print("int_list_please", int_list_please(), type(int_list_please()) == list)
    print(
        "string_list_please", string_list_please(), type(string_list_please()) == list
    )
    print("dictionary_please", type(dictionary_please()) == dict)
    print("is_it_5", is_it_5(5))
    print("is_it_5", is_it_5(6))
    print("take_five", take_five(5))
    print("take_five", take_five(3))
    print("greet:", greet())
    print("three_counter:", one_counter())
    print("n_counter:", n_counter(7))
    print("fizz_buzz:", fizz_buzz())
    print("put_behind_bars:", set_it_on_fire())
    print("chaing gang 5", the_chain_gang_5(5))
    print("chaing gang 5", the_chain_gang_5(10))
    print("pet_filter:", pet_filter())
    print("best_letter_for_pets:", best_letter_for_pets())
    print("make_filler_text_dictionary:", make_filler_text_dictionary())
    print("random_filler_text:", random_filler_text())
    print("fast_filler:", fast_filler())
    for i in range(4):
        print(i, fast_filler(number_of_words=20), "\n")
    print(
        "These are mini tests, they show you some output.",
        "\nDon't forget to run the real tests.",
        "\nThey test your code against the non-default arguments",
    )
