sentence = input("Enter a sentence: ")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        special += 1

total_letters = vowels + consonants
vowel_pct = (vowels / len(sentence) * 100) if len(sentence) > 0 else 0

print("\nDOCUMENT ANALYSIS REPORT")
print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")

print("\nCharacter Breakdown")
print(f"Words: {words}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special characters: {special}")

print("\nSummary")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_pct:.1f}%")
print("\nAnalysis Complete!")
