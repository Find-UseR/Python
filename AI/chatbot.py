import random


chatbot_responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm doing well , How can I help you?", "I'm feeling great today, How can I help you?"],
    "what is your name": ["My name is Chatbot!", "You can call me Chatbot!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm sorry, I don't understand. Could you please rephrase your question?"]
}


def generate_response(user_input):
   
    user_input = user_input.lower()

    
    for input_pattern, output_patterns in chatbot_responses.items():
        if input_pattern in user_input:
          
            return random.choice(output_patterns)

  
    return random.choice(chatbot_responses["default"])

print("Welcome to the Chatbot! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    chatbot_response = generate_response(user_input)

  
    print("Chatbot:", chatbot_response)

    
    if "bye" in user_input.lower():
        break
