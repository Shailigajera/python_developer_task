
"""
Problem:
Given a text file, analyze its content to:
- Count the total number of words.
- Calculate word frequency.
- Identify the top 5 most common words.

Approach:
- Read and clean the text (convert to lowercase and remove punctuation).
- Split the text into words.
- Use collections.Counter to count word frequencies.
- Return total words and top 5 most common words.
"""

import string
from collections import Counter

def clean_text(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation))

def analyze_text(text):
    words = clean_text(text).split()
    total_words = len(words)
    frequency = Counter(words)
    most_common = frequency.most_common(3)
    return total_words, frequency, most_common

if __name__ == "__main__":
    try:
        with open("sample.txt", "r") as file:
            content = file.read()
        total, freq, common = analyze_text(content)
        print("Total Words:", total)
        print("Top 3 Most Common Words:")
        for word, count in common:
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("Error: 'sample.txt' not found. Please ensure the file exists in the current directory.")
