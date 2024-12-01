// Fetch messages from messages.json
const fetchMessages = async () => {
    const response = await fetch("data/messages.json");
    return response.json();
};

// Show popup with a random message
const showPopup = (messages) => {
    const popup = document.getElementById("popup");
    const randomMessage = messages[Math.floor(Math.random() * messages.length)].message;
    popup.textContent = randomMessage;

    popup.classList.add("visible"); // Show popup
    setTimeout(() => popup.classList.remove("visible"), 7000); // Hide after 7 seconds
};

// Main function to handle popup display
const initPopup = async () => {
    const messages = await fetchMessages();

    // Show popup every 10 seconds
    setInterval(() => showPopup(messages), 10000);
};

// Initialize the popup logic
initPopup();
