"""
Example of using f-strings for formatted string literals in Python.
"""

name = input("Enter your name: ")
color = input("Enter your favorite color: ")

def greet(name, color):
    print(f"Hello, my name is {name} and I like the color {color}")

if __name__ == "__main__":
    greet(name, color)