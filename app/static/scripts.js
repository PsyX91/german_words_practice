// Import any needed libraries
const axios = require("axios");

// Function to receive data from Python script
async function receiveData() {
  try {
    // Define variables. Get random index
    const response = await axios.get("http://localhost:5000/data");
    const data = response.data;
    let index = 77;
    while (true) {
      index = getRandomInt(data.length);
      if (getRandomInt(data[index][2]) == 0 || data[index][2] < 0) {
        break;
      }
    }

    // Replace title with word
    document.getElementById("title").textContent = data[index][0];

    // Handle error
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

// Function to send "1" to Python script
function sendOne() {
  axios.post(1).catch((error) => {
    console.error('Error sending "1":', error);
  });
}

// Function to send "0" to Python script
function sendZero() {
  axios.post(0).catch((error) => {
    console.error('Error sending "0":', error);
  });
}

// Add event listeners to buttons
document.getElementById("reveal").addEventListener("click", receiveData);
document.getElementById("correct").addEventListener("click", sendOne);
document.getElementById("wrong").addEventListener("click", sendZero);
