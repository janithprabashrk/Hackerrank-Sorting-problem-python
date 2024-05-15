# Hackerrank-Sorting-problem-python
String Sorting Algorithm
This Python function Sort(s) sorts a given string s into four categories: lowercase letters, uppercase letters, odd digits, and even digits. It then sorts each category individually and combines the results into a single string following a specific order. Below is a breakdown of how the code works:

Algorithm Explanation:
Input String: The user is prompted to input a string.

Categorization:

The function categorizes each character in the string into one of four arrays: lower for lowercase letters, upper for uppercase letters, odd_digits for odd digits, and even_digits for even digits.
Sorting:

Each category array is sorted individually using the sort() method.
Combination:

The sorted arrays are concatenated together in the specified order: lowercase letters, uppercase letters, odd digits, and even digits.
Output:

The function returns the sorted string.
Usage:
python
Copy code
S = input("Enter a string to sort: ")
print(Sort(S))
Simply run the script, input the desired string when prompted, and it will output the sorted string according to the specified categories.

Example:
Input: "aB2C1"
Output: "aBC12"
This means that lowercase letters ('a'), uppercase letters ('B'), odd digits ('1'), and even digits ('2') are sorted and combined into the final output string.
