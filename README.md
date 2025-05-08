# Levenshtein-Distance-based-Word-Correction

## Overview
This script implements a text processing tool for comparing words based on their similarity using Levenshtein Distance (also known as edit distance). The tool can identify and suggest the closest matches for misspelled words by computing the minimum edit distance between words in a sentence and a given dictionary.

## Requirements
- Python 3.x
- **Libraries**:
  - `re`: for regular expressions to clean and preprocess text.

## Functionality

1. **Text Preprocessing**:
   - Converts the input text to lowercase.
   - Removes punctuation marks such as `!:,()".;\'?`.
   - Splits the text into individual words.

2. **Levenshtein Distance Calculation**:
   - The script computes the Levenshtein Distance between two words, which is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other.

3. **Finding Closest Words**:
   - For a given sentence, the script finds words that are not in the provided dictionary and calculates their closest matches based on the Levenshtein Distance.
   - The script outputs the word, the distance to the closest match, and the list of closest words.

4. **Handling Multiple Sentences**:
   - The tool is designed to process multiple sentences and compare their words to a dictionary, identifying possible spelling errors or variations.

## Code Walkthrough

1. **Text Preprocessing**:
   - The `re.sub()` function is used to remove punctuation from the input text, and the `split()` function breaks the text into individual words.

2. **Levenshtein Distance Function**:
   - The `LevenshteinDistance()` function computes the minimum number of operations (insertions, deletions, or substitutions) to convert one word into another. It uses dynamic programming to efficiently calculate the edit distance.

3. **Finding Closest Words**:
   - The `find_min_distance()` function processes each word in the input sentence that is not in the dictionary. It calculates the Levenshtein Distance between each word and all words in the dictionary to find the closest matches. The function returns a list of tuples containing the word, the minimum distance, and the closest words.

4. **Example Sentences**:
   - The script processes two example sentences:
     1. `"The classic example provided in British publications."`
     2. `"Natural selection has gradually done away with them."`
   - For each sentence, it identifies words not present in the dictionary and suggests corrections based on the closest dictionary words.
