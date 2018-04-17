import sys

# problem1
# return your name
def get_name():
    return "Sross Gupta"

# problem2
# return "Information Systems"
def get_major():
    return "Information Systems"


# problem3
# return "Carnegie Mellon University"
def get_university():
    return "Carnegie Mellon University"

# problem4
# name the function get_python_version
# return sys.version
def get_python_version():
    return sys.version

# problem5
# name the function get_greeting
# return "It's nice to meet everyone."
def get_greeting():
    return "It's nice to meet everyone."


# problem6
def main():
    text = []
    text.append("My Name is: {0}".format(get_name()))
    text.append("My Major is: {0}".format(get_major()))
    text.append("My School is: {0}".format(get_university())) # call the approprite function
    text.append("My python version is: {0}".format(get_python_version())) # call the approprite function
    text.append("{0}".format(get_greeting())) # call the approprite function
    return text


if __name__ == "__main__":
    """Do not change or modify this code
    """
    text = main()
    for line in text:
        print(line)
