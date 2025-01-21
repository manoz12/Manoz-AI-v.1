document.getElementById('send-btn').addEventListener('click', async function() {
    const messageInput = document.getElementById('message');
    const userMessage = messageInput.value.trim();
    if (userMessage) {
        displayMessage('You: ' + userMessage);
        messageInput.value = '';

        try {
            const response = await fetch('http://127.0.0.1:5000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: userMessage })
            });

            const data = await response.json();
            const botReply = data.reply || "Sorry, I couldn't understand that.";
            displayMessage('Bot: ' + botReply);
        } catch (error) {
            displayMessage('Bot: Oops! Something went wrong.');
        }
    }
});

function displayMessage(message) {
    const chatBox = document.getElementById('chat-box');
    const messageElem = document.createElement('p');
    messageElem.textContent = message;
    chatBox.appendChild(messageElem);
    chatBox.scrollTop = chatBox.scrollHeight;
}
