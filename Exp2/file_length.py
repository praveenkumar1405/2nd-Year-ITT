with open("document.txt", "r") as file:
    text = file.read().lower() 
    words = text.split()       

print(f"Total Word Count: {len(words)}")

longest_word = max(words, key=len)
print(f"Longest Word: {longest_word}")
print(f"Reversed Longest Word: {longest_word[::-1]}")

# 4. Find and display repeated words
print("\nRepeated Words and their Counts:")
unique_words = set(words)  
for word in unique_words:
    count = words.count(word)
    if count > 1:
        print(f"{word}: {count}")
