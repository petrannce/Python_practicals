from textblob import TextBlob

# Misspelled text
blob = TextBlob("I havv goood speling")

# Correct the spelling
corrected_blob = blob.correct()

# Print the corrected text
print("Original Text: ", blob)
print("Corrected Text: ", corrected_blob)

