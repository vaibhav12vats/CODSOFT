import re

# Define the rules for the chatbot
rules = {
    r'.*hello.*': 'Hello! How can I assist you today?',
    r'.*help.*': 'Sure, I can help you. What do you need assistance with?',
    r'.*goodbye.*': 'Goodbye! Have a great day!',
    r'.*age.*': 'I am a computer program, so I don\'t have an age.',
    r'.*name.*': 'My name is ChatBot.',
    r'.*how are you.*': 'I am just a computer program, but I\'m here to assist you!',
    r'.*default.*': "I'm sorry, I don't understand that. How can I assist you?"
}

def chatbot_response(user_input):
    """
    Generate a response from the chatbot based on the user's input.
    """
    for pattern, response in rules.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return response
    return rules['.*default.*']

# Main loop for the chatbot
while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print('ChatBot: Goodbye! Have a great day!')
        break

    response = chatbot_response(user_input)
    print('ChatBot:', response)
