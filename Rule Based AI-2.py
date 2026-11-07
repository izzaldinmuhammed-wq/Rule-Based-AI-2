import random

vocabulary = {
    "hello": [0.9, 0.0, 0.0],
    "hi": [0.8, 0.0, 0.0],
    "hey": [0.85, 0.0, 0.0],
    "joke": [0.0, 0.9, 0.0],
    "funny": [0.0, 0.8, 0.0],
    "goodbye": [0.0, 0.0, 0.9],
    "bye": [0.0, 0.0, 0.8]
}

biases = [0.1, 0.1, 0.1]

responses = [
    "Hello! How can I help you?",
    "Why did the computer go to the doctor? It had a virus!",
    "Goodbye! Have a great day!"
]

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        break

    scores = biases.copy()

    for word in user_input.split():
        if word in vocabulary:
            for i in range(3):
                scores[i] += vocabulary[word][i]

    prediction = scores.index(max(scores))

    print("AI:", responses[prediction])