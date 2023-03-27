# Import necessary modules from PyTorch
import torch
import torch.nn as nn

# Define a neural network model class, which inherits from the PyTorch Module class
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()

        # Define the layers of the neural network, as PyTorch Linear modules
        self.l1 = nn.Linear(input_size, hidden_size)  # input layer
        self.l2 = nn.Linear(hidden_size, hidden_size)  # hidden layer
        self.l3 = nn.Linear(hidden_size, num_classes)  # output layer

        # Define the activation function to use between the hidden layers
        self.relu = nn.ReLU()

    # Define the forward pass through the neural network
    def forward(self, x):
        out = self.l1(x)   # Apply the first linear layer to the input
        out = self.relu(out)  # Apply the activation function to the output of the first layer
        out = self.l2(out)  # Apply the second linear layer to the output of the first layer
        out = self.relu(out)  # Apply the activation function to the output of the second layer
        out = self.l3(out)  # Apply the third linear layer to the output of the second layer

        return out  # Return the final output of the third linear layer
