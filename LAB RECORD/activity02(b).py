def word_count(sentence):
    words = sentence.split()
    word_freq = {}

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    return len(words), word_freq

# Test the function
sentence = input("Enter a sentence: ")
count, frequencies = word_count(sentence)

print(f"The number of words in the sentence is: {count}")
print("Word frequencies:", frequencies)

