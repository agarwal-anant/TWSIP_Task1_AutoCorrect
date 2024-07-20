import streamlit as st
import programs as fp


def main():
    st.title("Auto-Correct System")

    # Input for the word to be corrected
    my_word = st.text_input("Enter a word:", "")

    if my_word:
        # Get the corrections for the input word
        corrections = fp.suggest_corrections(my_word, fp.word_probabilities, fp.vocabulary)
        corrections.sort(key=lambda x: x[1], reverse=True)

        if corrections:
            st.write(f"Incorrect word: {my_word}")
            st.write("Suggestions:")

            # Display each suggestion as a button
            for i, (word, probability) in enumerate(corrections):
                if st.button(f"{word}", key=f"suggestion_{i}"):
                    st.write(f"Word {i + 1}: {word} (Probability: {probability:.6f})")
                    st.text_input("Corrected word:", value=word, key="corrected_word")
                    break


if __name__ == "__main__":
    main()
