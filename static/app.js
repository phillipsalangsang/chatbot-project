// Define a Chatbox class
class Chatbox {
    
    // Constructor function which initializes class properties
    constructor() {
        
        // Define class arguments and assign them to properties
        this.args = {
            openButton: document.querySelector('.chatbox__button'), //Open Chatbox
            chatBox: document.querySelector('.chatbox__support'), //Chatbox Element
            sendButton: document.querySelector('.send__button') //Button to send message
        }

        // Initialize chatbox state
        this.state = false;
        
        // Initialize chat messages
        this.messages = [];
    }

    // Function to display the chatbox
    display() {
        
        // Destructure arguments
        const {openButton, chatBox, sendButton} = this.args;

        // Add event listener to open button to toggle the chatbox state
        openButton.addEventListener('click', () => this.toggleState(chatBox))

        // Add event listener to send button to send messages
        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        // Add event listener to input field to send messages on pressing enter key
        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    // Function to toggle chatbox state
    toggleState(chatbox) {
        
        // Toggle chatbox state
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    // Function to handle sending messages
    onSendButton(chatbox) {
        
        // Get input field and its value
        let textField = chatbox.querySelector('input');
        let text1 = textField.value
        
        // If message is empty, return
        if (text1 === "") {
            return;
        }

        // Create a message object and add to messages array
        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

            // Send message to backend server for processing and get the response
            fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            // mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
            
            // Create a response message object and add to messages array
            let msg2 = { name: "Sarah", message: r.answer };
            this.messages.push(msg2);
            
            // Update chat text and reset input field
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            
            // Update chat text and reset input field
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    // Function to update chat text
    updateChatText(chatbox) {
        let html = '';
        
        // Reverse the order of messages and loop through them to create HTML for chat text
        this.messages.slice().reverse().forEach(function(item, index) {
            
            // If the message was sent by the bot, display it on the right side of the chatbox.
            if (item.name === "Sarah")
            {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            
            // Otherwise, display it on the left side of the chatbox.
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
          });

        // Update the chatbox display with the new HTML.
          const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }

} 

// Create a new Chatbox instance and display it on the page.
const chatbox = new Chatbox();
chatbox.display();