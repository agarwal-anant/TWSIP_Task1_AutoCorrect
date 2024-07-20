import re
from collections import Counter

# Function to process data from a text file and extract words
def load_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    words = re.findall(r'\w+', text)
    return words

# Function to get word count dictionary from a list of words
def count_words(word_list):
    return Counter(word_list)

# Function to calculate the probability of each word in the word count dictionary
def calculate_probabilities(word_count_dict):
    total_words = sum(word_count_dict.values())
    return {word: count / total_words for word, count in word_count_dict.items()}

# Function to generate words by deleting one letter at each position
def delete_characters(word):
    return [word[:i] + word[i+1:] for i in range(len(word))]

# Function to generate words by replacing each letter with every other letter
def replace_characters(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return [word[:i] + l + word[i+1:] for i in range(len(word)) for l in letters if l != word[i]]

# Function to generate words by inserting every letter at each position
def insert_characters(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return [word[:i] + l + word[i:] for i in range(len(word) + 1) for l in letters]

# Function to generate words by switching adjacent letters
def swap_adjacent_characters(word):
    return [word[:i] + word[i+1] + word[i] + word[i+2:] for i in range(len(word) - 1)]

# Function to generate all possible words that are one edit away from the input word
def edit_one_letter(word, allow_swaps=True):
    edits = set(delete_characters(word))
    edits.update(replace_characters(word))
    edits.update(insert_characters(word))
    if allow_swaps:
        edits.update(swap_adjacent_characters(word))
    return edits

# Function to generate all possible words that are two edits away from the input word
def edit_two_letters(word, allow_swaps=True):
    edits = set()
    one_edit_words = edit_one_letter(word, allow_swaps)
    for w in one_edit_words:
        edits.update(edit_one_letter(w, allow_swaps))
    return edits

# Function to get the best corrections for a given word
def suggest_corrections(word, word_probabilities, vocabulary):
    suggestions = (
        [word] if word in vocabulary else
        list(edit_one_letter(word).intersection(vocabulary)) or
        list(edit_two_letters(word).intersection(vocabulary))
    )
    best_suggestions = sorted([(s, word_probabilities.get(s, 0)) for s in suggestions], key=lambda x: x[1], reverse=True)
    return best_suggestions

# Load and process the data
word_list = load_words("Data/big.txt")
vocabulary = set(word_list)
word_count_dict = count_words(word_list)
word_probabilities = calculate_probabilities(word_count_dict)
