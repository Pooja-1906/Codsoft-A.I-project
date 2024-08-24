# chat board with rule based aalgoritham 
import random


def get_response(user_message):
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you": "I'am good, thank you!",
        "bye": "Good bye!",
        "default": "I'm sorry, I don't understand pleace try again.",
    }

    # Convert the user message to lowercase for case insensitivity
    message = user_message.lower()

    # Check for specific patterns in the user message
    if message in responses:
        return responses[message]
    else:
        return responses["default"]

def main():
    print("ChatBot: Hello! How can I assist you today?")
    while True:
        user_input = input("User: ")
        response = get_response(user_input)
        print("ChatBot:", response)

        # Exit the loop if the user says "bye"
        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    main()
