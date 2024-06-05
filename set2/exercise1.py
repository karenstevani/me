"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will assign the list to the variable some_words
some_words = ["what", "does", "this", "line", "do", "?"] # it assigned the list into variable some_words

# I think this will create a loop that reads and calls each item of the some_words list and print that word
for word in some_words: 
    print(word) # it printed "what does this line do ?" with the format of one word per line

# I think this is the same as above and will create a loop that reads and calls each item of the some_words list and print the items
for x in some_words:
    print(x) # it printed "what does this line do?" with the format of one word per line

# I think this will print all the items in the list some_words by calling the print function 
print(some_words) # it printed "['what', 'does', 'this', 'line', 'do', '?']"

# I think this will check if the amount of items in the some_words list is greater than 3, and if so it'll print the phrase by calling the print function
if len(some_words) > 3:
    print("some_words contains more than 3 words") # it printed "some_words contains more than 3 words"

# I think this will define the function usefulFunction() as printing the name, operating system, version, and other details of the computer it's running on
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) # it printed "uname_result(system='Windows', node='Karen', release='11', version='10.0.22631', machine='AMD64')"


usefulFunction()
