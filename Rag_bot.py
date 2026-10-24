import streamlit as st
import ollama
import numpy as np

st.title("my chat bot")

with open("info.txt", "r") as file:
    knowledge = file.read()

chunks = knowledge.split("\n\n")

# Create embeddings for all chunks
response = ollama.embed(
    model="nomic-embed-text",
    input=chunks
)

chunk_vectors = response["embeddings"]

# Get user's question
question = st.chat_input("Ask me anything:")

if question:

    with st.chat_message("user"):
        st.write(question)

    # Create embedding for question
    response = ollama.embed(
        model="nomic-embed-text",
        input=question
    )

    question_vector = response["embeddings"][0]

    # Calculate similarity
    scores = []

    for vector in chunk_vectors:
        similarity = np.dot(question_vector, vector) / (
            np.linalg.norm(question_vector) *
            np.linalg.norm(vector)
        )

        scores.append(similarity)

    # Find best chunk
    best_index = np.argmax(scores)

    best_chunk = chunks[best_index]

    # Create prompt
    prompt = f"""
Context:
{best_chunk}

Question:
{question}
"""
    # ask ollama 
    response = ollama.chat(
        model="gemma",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response["message"]["content"]

    #display answer
    with st.chat_message("assistant"):
        st.write(answer)