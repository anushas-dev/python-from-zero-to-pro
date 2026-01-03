"""
This script takes a hyphen-separated list of hobbies from user input,
prints each hobby on a new line prefixed with a *, and then
joins the hobbies into a single string separated by commas.
"""

def join_list_items(items):
    return ", ".join(items)

if __name__ == "__main__":
    hobbies = input("Enter a list of hobbies separated by hyphens (e.g., reading-cycling-cooking): ")
    print("Your hobbies are:")
    for item in hobbies.split("-"):
        print(f"* {item}")
    result = join_list_items(hobbies.split("-"))
    print(f"Listing hobbies as comma-separated string: {result}")