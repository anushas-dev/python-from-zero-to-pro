"""
Basic example demonstrating vowel and consonant identification in a string.
"""

def count_vowels_and_consonants(input_string):
    """Counts the number of vowels and consonants in the given string."""
    vowels = "aeiouAEIOU"
    vowel_count = 0  # Initialize vowel count
    consonant_count = 0 # Initialize consonant count

    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1 # Increment vowel count
            else:
                consonant_count += 1 # Increment consonant count

    print(f"Vowels count: {vowel_count}, Consonants count: {consonant_count}")
    return vowel_count, consonant_count

if __name__ == "__main__":
    test_string = input("Enter a test string: ")
    count_vowels_and_consonants(test_string)