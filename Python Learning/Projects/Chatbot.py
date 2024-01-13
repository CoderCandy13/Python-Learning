import nltk
from nltk.chat.util import Chat, reflections

# Define the chat pairs for the chatbot
pairs = [
    ["hello|hi|hey", ["Hi there!", "Hello!", "Hey!"]],
    ["how are you", ["I'm doing well, thank you!", "I'm good, how about you?"]],
    ["what's your name", ["I'm a chatbot created with NLTK.", "You can call me ChatGPT."]],
    ["quit", ["Goodbye!", "It was nice chatting with you."]],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Run the chatbot
def chat_with_bot():
    print("Hello! I'm a simple chatbot. You can start chatting with me. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    nltk.download("punkt")  # Download the Punkt tokenizer
    chat_with_bot()
