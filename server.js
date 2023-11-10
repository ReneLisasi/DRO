// server.js
const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const app = express();

const path = require('path');

app.use(bodyParser.json());

// Serve HTML and static files
app.use(express.static(__dirname));

// Serve HTML file for all routes
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.post('/api/findServices', async (req, res) => {
    try {
        const { location, radius } = req.body;
        
        // Log the received data for verification
        console.log('Received Data:', { location, radius });

        // Forward the request to the Python backend
        const pythonResponse = await axios.post('http://localhost:5000/api/findServices', { location, radius });

        // Return the Python backend response to the front end
        res.json(pythonResponse.data);
    // } catch (error) {
    //     console.error('Error:', error);
    //     res.status(500).json({ error: 'Internal Server Error' });
    // }
    console.log(result.response.data);
    }catch (error) {
        console.error(error.response.data);     // NOTE - use "error.response.data` (not "error")
      }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
