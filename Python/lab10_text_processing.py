print("TEXT PROCESSING TOOL")
sentence = input("Enter a sentence: ")

print("\nProcessing Results")
idx = int(input("Enter position for indexing: "))
print(f"Character at position : '{sentence[idx]}'")

start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing : "))
print(f"Sliced string [{start}:{end}] : '{sentence[start:end]}'")

print(f"Uppercase : {sentence.upper()}")
print(f"Lowercase : {sentence.lower()}")

old_word = input("Enter word to replace : ")
new_word = input("Enter replacement word : ")
print(f"After replace : {sentence.replace(old_word, new_word)}")
print(f"Length of sentence : {len(sentence)}")

print("\nAnalysis Complete!")
