import re

# For loop
def for_loop():
    result = ""
    numbers = [1,2,3,4]

    for item in numbers:
        result += str(item)

    print("For loop: " + result)

# While loop
def while_loop():
    run = True
    current = 1
    result = ""

    while run:
        if current == 10:
            run = False
        else:
            result += str(current)
            current += 1

    print("While loop: " + result)


# Undefined arguments
def print_people(*people):
    result = ""
    for person in people:
        result += str(person) + " "

    print("Undefined arguments: " + result)



# Using regex
def use_regex():
    text = "I AM NOT YELLING, she said. But it was not true."

    # Remove capital letters.
    new_text = re.sub('[A-Z]', '', text)
    print ("Removed capital letters: " + new_text)

    # Remove lower case letters.
    new_text = re.sub('[a-z]', '', text)
    print ("Removed lower case letters: " + new_text)

    # Remove punctuation.
    new_text = re.sub('[.,\']', '', text)
    print ("Removed punctuation: " + new_text)

    # Remove punctuation and lower case letters.
    new_text = re.sub('[.,\'a-z]', '', text)
    print ("Removed punctuation and lower case letters: " + new_text)

    # Remove punctuation, lower case letters and blank spaces.
    new_text = re.sub('[.,\'a-z+" "]', '', text)
    print ("Removed punctuation, lower case letters and blank spaces: " + new_text)

    # Remove everything but numbers.
    text += "6, 345 - 789"
    new_text = re.sub('[^0-9]', '', text)
    print ("Removed everything but numbers: " + new_text)
    

# Call for_loop
# for_loop()

# Call while_loop
# while_loop()

# Call print_people
# print_people("George", "Mary", "Dick", "Eve")

# Call use_regex
use_regex()

