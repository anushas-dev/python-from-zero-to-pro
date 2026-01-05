"""
This script takes a list of hobbies from user input,prints each hobby on a new line prefixed with *
"""

def print_list_items(hobbies):
    for hobby in hobbies:
        print(f"* {hobby}") # Print each hobby with * prefix

if __name__ == "__main__":
    hobbies = input("Enter a list of hobbies separated by commas (e.g., reading,cycling,cooking): ").split(",")
    # print("Hobby List:", hobbies) # Debugging line to check the list
    print("Your hobbies are:")
    print_list_items(hobbies)