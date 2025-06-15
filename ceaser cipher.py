letter = input("Enter a single letter (A-Z): ").upper()
if len(letter) == 1 and letter.isalpha() and 'A' <= letter <= 'Z':
    number = ord(letter) - 65
    print(f"{letter} = {number}")
else:
    print("Invalid input! Please enter a single letter from A to Z.")
