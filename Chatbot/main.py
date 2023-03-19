import random

# Greeting messages
greetings = ["Hello! How can I help you?", "Good day! How can I help you?", "Welcome! How can I help you?"]

# Question options
questions = {
    "1": "What is your name?",
    "2": "How are you?",
    "3": "What do you do?",
    "4": "Can you help me with something?",
    "5": "Goodbye"
}

# Response messages
responses = {
    "What is your name?": "My name is ChatBot.",
    "How are you?": "I'm doing well, thank you for asking!",
    "What do you do?": "I am a chatbot and am available to answer your questions.",
    "Can you help me with something?": "Of course! Please let me know how I can assist you.",
    "Goodbye": "Goodbye! See you next time.",
}

# Function to get a response
def get_response(message):
    if message in responses:
        return responses[message]
    else:
        return "I don't understand your question."

# Chatbot loop
while True:
    print("Please choose a question:")
    for key, value in questions.items():
        print(key + ": " + value)
    option = input("Option: ")
    if option.lower() == "exit":
        break
    elif option in questions:
        print("You: " + questions[option])
        print("ChatBot: " + get_response(questions[option]))
    else:
        print("Invalid option. Please try again.")