def Sort(s):
    # Split the string into four categories
    #Creating arrays
    lower = []
    upper = []
    odd_digits = []
    even_digits = []
    
    # Categorize each character in the string
    for char in s:
        if char.islower():
            lower.append(char)
        elif char.isupper():
            upper.append(char)
        elif char.isdigit():
            # Determine if it's an odd or even digit
            if int(char) % 2 == 1:
                odd_digits.append(char)
            else:
                even_digits.append(char)
    
    # Sort each category individually
    lower.sort()
    upper.sort()
    odd_digits.sort()
    even_digits.sort()
    
    # Combine the sorted results in the specified order
    result = "".join(lower + upper + odd_digits + even_digits)
    
    return result

# Example input and output
if __name__ == '__main__':
    S = input("Enter a string to sort: ")
    print(Sort(S))


