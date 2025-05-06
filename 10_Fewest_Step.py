"""
Problem:
Separate letters and digits from a given string, sort them individually, and concatenate the result.

Example:
Input : "B4A1D3"
Output: "ABD134"

Approach:
- Traverse the input string.
- Separate letters and digits into two lists.
- Sort both lists individually.
- Concatenate sorted letters followed by sorted digits.
"""

def sort_letters_digits(input_string):
    letters = []
    digits = []

    for ch in input_string:
        if ch.isalpha():
            letters.append(ch)
        elif ch.isdigit():
            digits.append(ch)

    sorted_letters = sorted(letters)
    sorted_digits = sorted(digits)

    return ''.join(sorted_letters + sorted_digits)

if __name__ == "__main__":
    user_input = input("Enter a string with letters and digits: ").strip()
    result = sort_letters_digits(user_input)
    print("Sorted output:", result)
