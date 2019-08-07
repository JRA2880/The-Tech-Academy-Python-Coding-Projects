#
# Python 3.7
#
# Author: John R. Adams
#
# Purpose: The Tech Academy - Python Course, Creating our first program together.
# Demonstrating how to pass variables from function to function while
# producting a functional game.

# Remember, function_name(variable)_means that we pass in the variable.
# return variable means that we are returning the variable to back to the
# calling function.

def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name,l_name,age,gender)


def get_info(f_name,l_name,age,gender):
    print("My name is {0} {1}. I am a {2} years old {3}.".format(f_name,l_name,age,gender))


if __name__== "__main__":
    start()
