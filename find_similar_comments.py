from sentence_transformers import SentenceTransformer
import numpy as np

# Load the model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read comments from file
input_file = "data/comments.txt"
output_file = "data/comments-similar.txt"

with open(input_file, "r", encoding="utf-8") as f:
    comments = [line.strip() for line in f.readlines() if line.strip()]

# Compute embeddings
embeddings = model.encode(comments)

# Find most similar pair
max_sim = -1
most_similar_pair = ("", "")

for i in range(len(comments)):
    for j in range(i + 1, len(comments)):
        sim = np.dot(embeddings[i], embeddings[j]) / (np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[j]))
        if sim > max_sim:
            max_sim = sim
            most_similar_pair = (comments[i], comments[j])

# Save most similar comments
with open(output_file, "w", encoding="utf-8") as f:
    f.write(most_similar_pair[0] + "\n" + most_similar_pair[1])

print("Most similar comments saved to:", output_file)
