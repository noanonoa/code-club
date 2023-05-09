# Refactor the following code.

hair = input("What color hair [brown]? ")
if hair == '':
    hair = 'brown'
print('You chose', hair)

hair_length = input("What hair length [short]? ")
if hair_length == '':
    hair_length = 'short'
print('You chose', hair_length)

eyes = input("What eye color [blue]? ")
if eyes == '':
    eyes = 'blue'
print('You chose', eyes)

gender = input("What gender [female]? ")
if gender == '':
    gender = 'female'
print('You chose', gender)

has_glasses = input("Has glasses [no]? ")
if has_glasses == '':
    has_glasses = 'no'
print('You chose', has_glasses)

has_beard = input("Has beard [no]? ")
if has_beard == '':
    has_beard = 'no'
print('You chose', has_beard)


# The functionality here is asking users for their preference.
# While the functionality is repeatable, the question being asked is not.
# While an answer can be provided by the user, it is not always a guarantee.
# While having a default answer is nice, it is not always the same default.
# With these concerns, one way to refactor could be providing two variables,
# question and default. Now we can ask a user for their preference with a
# custom question and default. The functionality is repeated with different
# outcomes like so:
def preference(question, default):

    # prompt user with the question (which ultimately is the answer)
    # add a space after the question for a nicer prompt
    answer = input(question + " ")

    # if no user input is provided, assign the default
    if answer == '':
        answer =  default

    # print the resulting choice
    return print("You chose", answer)

# The options are hair, hair_length, eyes, gender, has_glasses, and has_beard.
# assign a user preference to each of these options by invoking the preference
# method
hair = preference("What color hair [brown]?", "brown")
hair_length = preference("What hair length [short]?", "short")
eyes = preference("What eye color [blue]?", "blue")
gender = preference("What gender [female]?", "female")
has_glasses = preference("Has glasses [no]?", "no")
has_beard = preference("Has beard [no]?", "no")

