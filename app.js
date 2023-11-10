// app.js

// Initialize the Leaflet map with the initial view centered around your coordinates
const map = L.map('map').setView([33.8802511, -84.5125968], 14);

// Add a tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Create a div to display the clicked coordinates
const coordinatesDisplay = document.createElement('div');
document.body.appendChild(coordinatesDisplay);

// Event listener for the map click
map.on('click', function (e) {
    // Capture the clicked location
    const clickedLocation = e.latlng;
    console.log('Clicked Location:', clickedLocation);

    // Display the coordinates on the front end
    coordinatesDisplay.innerHTML = `Clicked Coordinates: ${clickedLocation.lat.toFixed(6)}, ${clickedLocation.lng.toFixed(6)}`;

    // Set the clicked location in a hidden input field (optional)
    document.getElementById('clickedLocation').value = JSON.stringify(clickedLocation);
});

// Event listener for the button click
document.getElementById('findServices').addEventListener('click', function () {
    // Get the clicked location from the hidden input field
    const clickedLocation = JSON.parse(document.getElementById('clickedLocation').value);

    // Get the radius from the text box
    const radius = document.getElementById('radius').value;

    // Send the location and radius to the backend
    sendToBackend(clickedLocation, radius);
});

// Function to send data to the backend
function sendToBackend(location, radius) {
    axios.post('/api/findServices', { location, radius })
        .then(response => {
            // Handle the response from the server
            console.log(response.data);
        })
        .catch(error => {
            // Handle errors
            console.error('Error:', error);
        });
}
