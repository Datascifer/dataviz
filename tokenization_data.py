import numpy as np
import pandas as pd
import random
import string

# Set seed for reproducibility (optional)
np.random.seed(42)
random.seed(42)

# Number of synthetic text records
num_records = 1000

# A small collection of excerpts from "The Souls of Black Folk" by W.E.B. Du Bois (1903)
dubois_excerpts = [
    "Between me and the other world there is ever an unasked question.",
    "One ever feels his twoness,—an American, a Negro.",
    "He would not bleach his Negro soul in a flood of white Americanism.",
    "They approach me in a half-hesitant sort of way, eye me curiously or compassionately.",
    "They speak in tones of careful courtesy, or in chilly distance.",
    "The exchange was merry, till one girl, a tall newcomer, refused my card.",
    "Why did God make me an outcast and a stranger in mine own house?",
    "Here, then, is the end of that compromise spirit.",
    "The power of the ballot we need in sheer self-defense.",
    "Freedom, too, the long-sought, we still seek—the freedom of life and limb.",
    "It is the spirit of the fathers that call us, from the blood and dust of the past.",
    "But alas, while sociologists gleefully count his bastards and his prostitutes, the very soul of the toiling, sweating black man is dark.",
    "How does it feel to be a problem?",
    "Our song, our toil, our cheer, and our tears will all be with the truth.",
    "In vain do we cry this our vast sorrow into the ears of the world."
]

# Possible languages (though Du Bois wrote in English, we might introduce variation)
languages = ["English", "Spanish", "French", "German"]

# Possible sentiments for demonstration
sentiments = ["Positive", "Negative", "Neutral"]

# Lists to store generated data
text_ids = []
texts = []
token_counts = []
avg_token_lengths = []
language_assignments = []
sentiment_assignments = []

for i in range(1, num_records + 1):
    # Randomly pick a sentence from Du Bois excerpts
    text = random.choice(dubois_excerpts)
    
    # Tokenize by splitting on space
    tokens = text.split()
    
    # Calculate token count and average token length
    token_count = len(tokens)
    avg_length = sum(len(token.strip(string.punctuation)) for token in tokens) / token_count
    
    # Randomly assign a language and sentiment
    lang = random.choice(languages)
    sentiment = random.choice(sentiments)
    
    # Append to lists
    text_ids.append(i)
    texts.append(text)
    token_counts.append(token_count)
    avg_token_lengths.append(avg_length)
    language_assignments.append(lang)
    sentiment_assignments.append(sentiment)

# Create the DataFrame
df_tokenization = pd.DataFrame({
    "text_id": text_ids,
    "text": texts,
    "token_count": token_counts,
    "average_token_length": avg_token_lengths,
    "language": language_assignments,
    "sentiment": sentiment_assignments
})

# Preview the first few rows
print(df_tokenization.head())

# Save to CSV (remove or comment out if not needed)
df_tokenization.to_csv("tokenization_data.csv", index=False)
