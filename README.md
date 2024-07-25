# nato-phonetic-alphabet-converter
 This script converts a user-input word into NATO phonetic alphabet code words. It reads data from nato_phonetic_alphabet.csv, creates a dictionary mapping each letter to its phonetic code, and translates the user's word using this dictionary. Output is a list of phonetic code words for each letter in the input word.

Ensure you have a CSV file named nato_phonetic_alphabet.csv in the project directory with the following format:
letter	code
A	Alfa
B	Bravo
C	Charlie
...	...

Enter a word when prompted. The script will output the corresponding NATO phonetic alphabet code words.
Code Overview

nato_phonetic_converter.py
Read CSV File: Reads nato_phonetic_alphabet.csv into a Pandas DataFrame.
Create Dictionary: Creates a dictionary nato_word_dict mapping each letter to its phonetic code.
User Input: Prompts the user to enter a word.
Convert to Phonetic: Converts the input word to its phonetic code words using the dictionary.
Output: Prints the list of phonetic code words.

If the user inputs:
Enter a word: Hello

The script will output:
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
