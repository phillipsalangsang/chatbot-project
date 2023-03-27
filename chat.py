import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Check if a GPU is available, and set the device to use accordingly
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the intents from a JSON file into a Python dictionary
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

# Load the trained model data from a saved file
FILE = "data.pth"
data = torch.load(FILE)

# Extract relevant information from the trained model data
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Instantiate a neural network model with the extracted information
model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Load the saved model state into the model
model.load_state_dict(model_state)

# Set the model to evaluation mode
model.eval()

# Define the name of the chatbot
bot_name = "Sarah"

# Define a function to get a response from the chatbot
def get_response(msg):
    # Tokenize the user's input message and convert it to a bag-of-words representation
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    # Use the model to predict the tag for the input message
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    # If the model is confident enough, randomly select a response from the corresponding intent
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    # If the model is not confident enough, return a default response
    return "I do not understand..."

# Define the main program to run the chatbot
if __name__ == "__main__":
    # Prompt the user to start the conversation
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # Get the user's input message and check if they want to quit
        sentence = input("You: ")
        if sentence == "quit":
            break

        # Get a response from the chatbot and display it to the user
        resp = get_response(sentence)
        print(resp)