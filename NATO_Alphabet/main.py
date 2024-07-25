import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Creating a list in this format:
# {"A": "value", "B": "value"}

nato_word_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Ask user for word
user_name = input("Enter a word: ").upper()
word_split = [word for word in user_name]

# Create a list of the phonetic code word from a word that the user input.
phonetic_word = [nato_word_dict[word] for word in word_split]
print(phonetic_word)
