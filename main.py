import programs as fp

def main():
    my_word = input("Enter a word: ")

    # Get suggestions for the entered word
    corrections = fp.suggest_corrections(my_word, fp.word_probabilities, fp.vocabulary)
    corrections.sort(key=lambda x: x[1], reverse=True)

    # Display the suggestions
    for i, (word, probability) in enumerate(corrections):
        print(f"word {i}: {word} (Probability: {probability:.6f})")

if __name__ == "__main__":
    main()
