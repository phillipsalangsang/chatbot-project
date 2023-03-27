# Import necessary modules and functions from Flask, and from a separate chat module
from flask import Flask, render_template, request, jsonify
from chat import get_response

# Instantiate a Flask application
app = Flask(__name__)

# Define a route for the homepage, which returns an HTML template
@app.get("/")
def index_get():
    return render_template("index.html")

# Define a route for the chatbot prediction API, which expects a POST request containing a JSON payload
@app.post("/predict")
def predict():
    # Extract the message from the JSON payload
    
    text = request.get_json().get("message")
    # TODO: Check if the text is valid

    # Get a response from the chatbot, based on the input message
    response = get_response(text)

    # Package the response into a JSON object
    message = {"answer": response}

    # Return the JSON object as the API response
    return jsonify(message)

# Define the main program to run the Flask application
if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
